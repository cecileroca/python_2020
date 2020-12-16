#!/usr/bin/python

import serial
import sys
import time
import string 
from serial import SerialException

class PhSensor:
  def __init__(self, port_):
    self.usbport = port_
    try:
      self.ser = serial.Serial(self.usbport, 9600, timeout=0)
      self.configured = True
    except serial.SerialException as e:
      self.configured = False

  def configured(self):
    return self.configured

  def readValue(self):
    if not self.configured:
      return -1

    self._send_cmd("R")
    # give the sensor time to respond
    time.sleep(1.5)
    lines = self._read_lines()
    for i in range(len(lines)):
      if lines[i][0] != b'*'[0]:
        #print(lines[i].decode('utf-8'))
        return float(lines[i].decode('utf-8'))

  def _read_line(self):
    """
    taken from the ftdi library and modified to 
    use the ezo line separator "\r"
    """
    lsl = len(b'\r')
    line_buffer = []
    while True:
      next_char = self.ser.read(1)
      if next_char == b'':
        break
      line_buffer.append(next_char)
      if (len(line_buffer) >= lsl and
          line_buffer[-lsl:] == [b'\r']):
        break
    return b''.join(line_buffer)
  
  def _read_lines(self):
    """
    also taken from ftdi lib to work with modified readline function
    """
    lines = []
    try:
      while True:
        line = self._read_line()
        if not line:
          break
          self.ser.flush_input()
        lines.append(line)
      return lines
    
    except SerialException as e:
      print( "Error, ", e)
      return None 

  def _send_cmd(self, cmd):
    """
    Send command to the Atlas Sensor.
    Before sending, add Carriage Return at the end of the command.
    :param cmd:
    :return:
    """
    buf = cmd + "\r"      # add carriage return
    try:
      self.ser.write(buf.encode('utf-8'))
      return True
    except SerialException as e:
      print ("Error, ", e)
      return None

      
if __name__ == "__main__":
  sensor = PhSensor("/dev/ttyAMA0")
  print(sensor.readValue())
  

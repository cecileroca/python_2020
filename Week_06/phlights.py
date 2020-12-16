import readph

phSensor = readph.PhSensor("/dev/ttyAMA0")
print(phSensor.readValue())

import time
import RPi.GPIO as GPIO
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup (19, GPIO.OUT)
GPIO.output(19, GPIO.HIGH)



while True:
    if phSensor.readValue() > 5:
        GPIO.output (19, GPIO.HIGH)
    else:
        GPIO.output (19, GPIO.LOW)



#Determinate and set the led lights as outputs
#Set the  button as input
import time
import RPi.GPIO as GPIO
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup (6, GPIO.OUT)
GPIO.setup (4, GPIO.OUT)
GPIO.setup (23, GPIO.OUT)
GPIO.setup (27, GPIO.OUT)
GPIO.setup(20, GPIO.IN, pull_up_down=GPIO.PUD_UP)
#Determine start time 
start_time = time.time()
#Set the star point of the lights
GPIO.output(6, GPIO.LOW)
GPIO.output(4, GPIO.LOW)
GPIO.output(27, GPIO.HIGH)
GPIO.output(23, GPIO.HIGH)

while True:
    #Determine ellapse time 
    ellapsed_time = time.time() - start_time
    #Determine the button  
    button_value = GPIO.input(20)
    #Button will set the lights to low (turn off lights)
    if button_value == GPIO.LOW:
        GPIO.output(6, GPIO.LOW)
        GPIO.output(4, GPIO.LOW)
        GPIO.output(27, GPIO.LOW)
        GPIO.output(23, GPIO.LOW)
    #Based on time the lights will be low (off) or high(on)
    else:
        if ellapsed_time > 5:
            GPIO.output(6, GPIO.LOW)
            GPIO.output(4, GPIO.LOW)
            GPIO.output(27, GPIO.HIGH)
            GPIO.output(23, GPIO.HIGH)

        else:
            GPIO.output(6, GPIO.HIGH)
            GPIO.output(4, GPIO.HIGH)
            GPIO.output(27, GPIO.LOW)
            GPIO.output(23, GPIO.LOW)
    
    




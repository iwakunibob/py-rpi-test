import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

ledPorts = [23, 24, 25, 26]
for port in ledPorts :
        GPIO.setup(port, GPIO.OUT)

for loop in range(1, 5):
        for port in ledPorts :  
                GPIO.output(port, True)
                time.sleep(0.5)
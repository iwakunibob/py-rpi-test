import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

ledPorts = [23, 24, 25, 26]
bitMasks = [0b0001, 0b0010, 0b0100, 0b1000]

for port in ledPorts :
    GPIO.setup(port, GPIO.OUT)

for num in range(65) :
    for mask in range (4) :
        if  num & bitMasks[mask] == 0 :
            GPIO.output(ledPorts[mask], False)
        else :
            GPIO.output(ledPorts[mask], True)
    time.sleep(1)


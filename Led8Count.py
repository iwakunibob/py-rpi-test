# led8bin.py
import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

ledPorts = [16, 17, 22, 23, 24, 25, 26, 27]
bitMasks = [0x01, 0x02, 0x04, 0x08, 0x10, 0x20, 0x40, 0x80]

for port in ledPorts :
    GPIO.setup(port, GPIO.OUT)

for num in range(257) :
    for mask in range (8) :
        if  num & bitMasks[mask] == 0 :
            GPIO.output(ledPorts[mask], False)
        else :
            GPIO.output(ledPorts[mask], True)
    time.sleep(0.2)         

time.sleep(4)            
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      
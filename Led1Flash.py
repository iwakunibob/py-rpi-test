import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(23, GPIO.OUT)

while True:
        GPIO.output(23, True)
        time.sleep(0.5)
        GPIO.output(23, False)
        time.sleep(0.5)

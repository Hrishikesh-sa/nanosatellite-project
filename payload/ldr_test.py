GNU nano 8.4                                                 ldr_test.py
import RPi.GPIO as GPIO
import time

ldr_pin = 18

GPIO.setmode(GPIO.BCM)
GPIO.setup(ldr_pin, GPIO.IN)

while True:
    if GPIO.input(ldr_pin):
        print("Bright")
    else:
        print("Dark")

    time.sleep(1)
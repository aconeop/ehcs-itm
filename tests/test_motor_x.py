# test_motor_x.py
import Jetson.GPIO as GPIO
import time

# Pines físicos en modo BOARD
STEP_PIN = 32  # STEP del motor X
DIR_PIN = 18   # DIR del motor X

GPIO.setmode(GPIO.BOARD)
GPIO.setup(STEP_PIN, GPIO.OUT)
GPIO.setup(DIR_PIN, GPIO.OUT)

def mover(pasos=200, sentido="adelante", delay=0.001):
    if sentido == "adelante":
        GPIO.output(DIR_PIN, GPIO.HIGH)
    else:
        GPIO.output(DIR_PIN, GPIO.LOW)

    for _ in range(pasos):
        GPIO.output(STEP_PIN, GPIO.HIGH)
        time.sleep(delay)
        GPIO.output(STEP_PIN, GPIO.LOW)
        time.sleep(delay)

try:
    print("Moviendo adelante...")
    mover(200, "adelante")
    time.sleep(1)
    print("Moviendo atrás...")
    mover(200, "atras")
finally:
    GPIO.cleanup()
    print("GPIO liberado.")
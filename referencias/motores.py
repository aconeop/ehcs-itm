
import RPi.GPIO as GPIO
import time




#ENA = 33
IN1 = 24
IN2 = 32#pwm

# set pin numbers to the board's
GPIO.setmode(GPIO.BOARD)
GPIO.setup(IN1, GPIO.OUT, initial=GPIO.HIGH)
GPIO.setup(IN2, GPIO.OUT, initial=GPIO.HIGH)
while True:
    #print('corriendo')
    GPIO.setup(IN2, GPIO.OUT, initial=GPIO.LOW)
    time.sleep(0.01)
    GPIO.setup(IN2, GPIO.OUT, initial=GPIO.HIGH)
    time.sleep(0.01)





# set pin numbers to the board's

#GPIO.setup(24, GPIO.OUT, initial=GPIO.LOW)
#GPIO.setup(33 , GPIO.OUT, initial=GPIO.LOW)

#while True:
#    GPIO.setup(pwm, GPIO.OUT, initial=GPIO.LOW)
#    GPIO.setup(pwm, GPIO.OUT, initial=GPIO.HIGH)
    



# motor_control.py
try:
    import Jetson.GPIO as GPIO
    HARDWARE_DISPONIBLE = True
except ImportError:
    print("⚠️ Jetson.GPIO no disponible. Entrando en modo simulación.")
    HARDWARE_DISPONIBLE = False

import time

STEP_PIN = 32
DIR_PIN = 24

def inicializar_gpio():
    if not HARDWARE_DISPONIBLE:
        return
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(STEP_PIN, GPIO.OUT, initial=GPIO.LOW)
    GPIO.setup(DIR_PIN, GPIO.OUT, initial=GPIO.LOW)

def move_one_step():
    if not HARDWARE_DISPONIBLE:
        print("⚠️ Mover paso omitido. Hardware no disponible.")
        return
    GPIO.output(STEP_PIN, GPIO.HIGH)
    time.sleep(0.001)
    GPIO.output(STEP_PIN, GPIO.LOW)
    time.sleep(0.001)

def set_direccion_avanzar():
    if not HARDWARE_DISPONIBLE:
        print("⚠️ Dirección no cambiada. Hardware no disponible.")
        return
    GPIO.output(DIR_PIN, GPIO.HIGH)

def set_direccion_retroceder():
    if not HARDWARE_DISPONIBLE:
        print("⚠️ Dirección no cambiada. Hardware no disponible.")
        return
    GPIO.output(DIR_PIN, GPIO.LOW)

def mover_arriba():
    set_direccion_avanzar()
    move_one_step()

def mover_abajo():
    set_direccion_retroceder()
    move_one_step()

def mover_izquierda():
    set_direccion_avanzar()
    move_one_step()

def mover_derecha():
    set_direccion_retroceder()
    move_one_step()

def limpiar_gpio():
    if HARDWARE_DISPONIBLE:
        GPIO.cleanup()

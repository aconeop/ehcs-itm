import RPi.GPIO as GPIO
import time

# Configuración de pines para el controlador A4988
STEP_PIN = 35
DIR_PIN = 37
ENABLE_PIN = 33
GPIO.setmode(GPIO.BOARD)
GPIO.setup(STEP_PIN, GPIO.OUT, initial=GPIO.LOW)
GPIO.setup(DIR_PIN, GPIO.OUT, initial=GPIO.LOW)
GPIO.setup(ENABLE_PIN, GPIO.OUT, initial=GPIO.LOW)
# Función para mover el motor un paso
def move_one_step():
    GPIO.output(STEP_PIN, GPIO.HIGH)
    time.sleep(0.001)  # Ajusta el tiempo de espera según la velocidad deseada
    GPIO.output(STEP_PIN, GPIO.LOW)
    time.sleep(0.001)  # Ajusta el tiempo de espera según la velocidad deseada
try:
    # Configurar dirección (puedes ajustar según tu necesidad)
    GPIO.output(DIR_PIN, GPIO.HIGH)  # Cambia a GPIO.LOW si quieres mover en la dirección opuesta
    # Movimiento continuo del motor (puedes ajustar según tu necesidad)
    while True:
        move_one_step()
except KeyboardInterrupt:
    print("Movimiento detenido manualmente")
finally:
    # Limpiar los pines GPIO al finalizar
    GPIO.cleanup()


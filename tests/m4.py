import Jetson.GPIO as GPIO
import tkinter as tk

# Configuración de pines
STEP_PIN = 32
DIR_PIN = 24

# Configuración de la ventana
window = tk.Tk()
window.title("Control de Motor Paso a Paso")
window.geometry("300x150")

# Configuración de pines GPIO
GPIO.setmode(GPIO.BOARD)
GPIO.setup(STEP_PIN, GPIO.OUT, initial=GPIO.HIGH)
GPIO.setup(DIR_PIN, GPIO.OUT, initial=GPIO.HIGH)

# Variables para el control del motor
step_count = 0
direction = GPIO.HIGH

# Función para mover el motor un paso
def move_one_step():
    global step_count
    
    GPIO.output(DIR_PIN, direction)
    GPIO.output(STEP_PIN, GPIO.HIGH)
    GPIO.output(STEP_PIN, GPIO.LOW)
    
    step_count += 1
    steps_label.config(text="Pasos: " + str(step_count))
    
# Función para cambiar la dirección de giro del motor
def change_direction():
    global direction
    
    direction = GPIO.HIGH if direction == GPIO.LOW else GPIO.LOW
    direction_label.config(text="Dirección: " + ("Avanzar" if direction == GPIO.HIGH else "Retroceder"))
    
# Crear componentes de la interfaz
steps_label = tk.Label(window, text="Pasos: 0")
steps_label.pack()

direction_label = tk.Label(window, text="Dirección: Avanzar")
direction_label.pack()

step_button = tk.Button(window, text="Dar un paso", command=move_one_step)
step_button.pack()

direction_button = tk.Button(window, text="Cambiar dirección", command=change_direction)
direction_button.pack()

# Ejecutar la aplicación
window.mainloop()

# Limpiar los pines GPIO al cerrar la aplicación
GPIO.cleanup()


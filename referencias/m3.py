import RPi.GPIO as GPIO
import tkinter as tk

# Configuración de pines
STEP_PIN = 32
DIR_PIN = 24

# Configuración de la ventana
window = tk.Tk()
window.title("Control de Motor Paso a Paso")
window.geometry("300x150")



GPIO.setmode(GPIO.BOARD)
GPIO.setup(STEP_PIN, GPIO.OUT, initial=GPIO.HIGH)
GPIO.setup(DIR_PIN, GPIO.OUT, initial=GPIO.HIGH)

# Función para mover el motor
def move_motor():
    steps = int(steps_entry.get())
    direction = GPIO.HIGH if direction_var.get() == 1 else GPIO.LOW
    
    GPIO.output(DIR_PIN, direction)
    
    for _ in range(steps):
        GPIO.output(STEP_PIN, GPIO.HIGH)
        GPIO.output(STEP_PIN, GPIO.LOW)
    
# Crear componentes de la interfaz
#steps_label = tk.Label(window, text="Pasos:")
#steps_label.pack()
#steps_entry = tk.Entry(window, width=10)
#steps_entry.insert(0, "100")
steps_entry.pack()

direction_label = tk.Label(window, text="Dirección:")
direction_label.pack()
direction_var = tk.IntVar()
forward_radio = tk.Radiobutton(window, text="Avanzar", variable=direction_var, value=1)
forward_radio.pack()
backward_radio = tk.Radiobutton(window, text="Retroceder", variable=direction_var, value=0)
backward_radio.pack()

start_button = tk.Button(window, text="Iniciar", command=move_motor)
start_button.pack()

# Ejecutar la aplicación
window.mainloop()

# Limpiar los pines GPIO al cerrar la aplicación
GPIO.cleanup()



import numpy as np
import cv2
from PIL import Image
import math
import os

# Modo simulación si no hay tensorflow disponible
try:
    import tensorflow as tf
    import tensorflow.experimental.numpy as tnp
    from tensorflow.python.ops.numpy_ops import np_config
    np_config.enable_numpy_behavior()
    SIMULACION = False
except ImportError:
    print("⚠️ TensorFlow no disponible. Modo simulación activado.")
    SIMULACION = True

# ==================== Filtros y herramientas ====================

def filtcosenoF(par, fi, co):
    [xfc, yfc] = np.meshgrid(np.linspace(1-co/2, co/2, co), np.linspace(fi/2, 1-fi/2, fi))
    fc1 = np.cos(xfc*(math.pi/par)*(1/np.max(xfc)))**2
    fc2 = np.cos(yfc*(math.pi/par)*(1/np.max(yfc)))**2
    fc = (fc1 > 0)*fc1*(fc2 > 0)*fc2
    return fc/np.max(fc)

def prepairholoF_remap(CH_m, dx, L):
    n = CH_m.shape[0]
    k = 2*math.pi/L
    fx = np.linspace(-1/(2*dx), 1/(2*dx), n)
    [FX, FY] = np.meshgrid(fx, fx)
    H = np.exp(1j * k * (1 - (L*FX)**2 - (L*FY)**2)**0.5)
    CH = np.fft.fftshift(np.fft.fft2(CH_m))
    U1 = CH * H
    u = np.fft.ifft2(np.fft.ifftshift(U1))
    return np.abs(u)

# ==================== Función principal ====================

def reconstruir_desde_archivo(ruta_imagen):
    if SIMULACION:
        print("🔁 Modo simulación: devolviendo imagen en escala de grises.")
        img = cv2.imread(ruta_imagen, cv2.IMREAD_GRAYSCALE)
        return img

    # Leer y preparar la imagen
    img = Image.open(ruta_imagen).convert('L')
    img_np = np.array(img)
    img_tf = tf.convert_to_tensor(img_np / 255.0, dtype=tf.float32)

    # Parámetros
    dx = 1.12e-6
    L = 633e-9

    # Filtro y reconstrucción
    fcos = filtcosenoF(0.48, img_tf.shape[0], img_tf.shape[1])
    holo_filtrada = img_tf * fcos
    reconstruida = prepairholoF_remap(holo_filtrada.numpy(), dx, L)

    # Normalizar y convertir a uint8
    reconstruida = cv2.normalize(reconstruida, None, 0, 255, cv2.NORM_MINMAX)
    return reconstruida.astype(np.uint8)

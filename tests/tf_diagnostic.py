import tensorflow as tf

# Obtener la lista de dispositivos visibles (incluyendo GPUs)
devices = tf.config.experimental.list_physical_devices('GPU')

# Comprobar si hay al menos una GPU disponible
if len(devices) > 0:
    # Configurar TensorFlow para utilizar todas las GPUs disponibles
    tf.config.experimental.set_visible_devices(devices, 'GPU')

    # Configurar TensorFlow para permitir el crecimiento de la memoria de la GPU
    for device in devices:
        tf.config.experimental.set_memory_growth(device, True)

    # Verificar que se están utilizando todas las GPUs disponibles
    strategy = tf.distribute.MirroredStrategy()
    print("Número de GPUs utilizadas: {}".format(strategy.num_replicas_in_sync))

    # Código adicional para construir y entrenar tu modelo con múltiples GPUs
    # ...
else:
    print("No se encontraron GPUs disponibles.")


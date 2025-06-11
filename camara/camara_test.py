import cv2
cap = cv2.VideoCapture(0)  # El número 0 indica la primera cámara disponible
while True:
    # Capturar fotograma por fotograma
    ret, frame = cap.read()

    # Mostrar el fotograma
    cv2.imshow('Camera', frame)

    # Salir del bucle si se presiona la tecla 'q'
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
# Liberar la cámara y cerrar las ventanas
cap.release()
cv2.destroyAllWindows()


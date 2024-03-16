import cv2

# Inicializar la webcam
captura = cv2.VideoCapture(1)

# Verificar si la webcam se abrió correctamente
if not captura.isOpened():
    print("No se pudo abrir la webcam")
    exit()

# Bucle principal para capturar y mostrar la transmisión de la webcam
while True:
    # Capturar un fotograma de la webcam
    ret, frame = captura.read()

    # Verificar si se capturó correctamente el fotograma
    if ret:
        # Mostrar el fotograma en una ventana
        cv2.imshow('Webcam', frame)

    # Esperar 1 milisegundo y verificar si se presiona la tecla 'q' para salir del bucle
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Liberar la webcam y cerrar todas las ventanas
captura.release()
cv2.destroyAllWindows()

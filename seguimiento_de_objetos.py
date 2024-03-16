import cv2

# Inicializar la webcam
captura = cv2.VideoCapture(2)

# Verificar si la webcam se abrió correctamente
if not captura.isOpened():
    print("No se pudo abrir la webcam")
    exit()

# Inicializar el objeto tracker KCF
tracker = cv2.TrackerKCF_create()

# Inicializar la región de interés (ROI) y las coordenadas anteriores
bbox = None
prev_coords = None

# Bucle principal
while True:
    # Capturar un fotograma de la webcam
    ret, frame = captura.read()

    # Verificar si la captura del fotograma fue exitosa
    if not ret:
        print("No se pudo capturar el fotograma")
        break

    # Si no hay una región de interés, seleccionar una ROI
    if bbox is None:
        bbox = cv2.selectROI('Webcam', frame, False)
        # Inicializar el tracker con la ROI seleccionada
        tracker.init(frame, bbox)
        # Establecer las coordenadas anteriores como las actuales
        prev_coords = bbox
    else:
        # Actualizar el tracker con el fotograma actual
        ret, bbox = tracker.update(frame)

        # Dibujar el rectángulo de seguimiento en el fotograma
        if ret:
            x, y, w, h = [int(i) for i in bbox]
            cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
            # Comparar las coordenadas actuales con las anteriores
            curr_coords = (x, y, w, h)
            if curr_coords != prev_coords:
                print("Ubicación del objeto:", curr_coords)
                print("Tamaño del objeto:", w*h/1000, 'cm2')
                prev_coords = curr_coords

    # Mostrar el fotograma con el rectángulo de seguimiento
    cv2.imshow('Webcam', frame)

    # Esperar 1 milisegundo y verificar si se presionó la tecla 'q' para salir
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Liberar la webcam y cerrar todas las ventanas
captura.release()
cv2.destroyAllWindows()

import cv2
import mediapipe as mp
import serial
import time

# Configurar conexión serial
arduino = serial.Serial('COM4', 9600)  # Cambia al puerto correcto
time.sleep(2)

# Inicializar MediaPipe
mp_hands = mp.solutions.hands
hands = mp_hands.Hands(
    
    max_num_hands=1,
    min_detection_confidence=0.7,
    min_tracking_confidence=0.7
)
mp_draw = mp.solutions.drawing_utils

# Función para contar dedos levantados
def count_fingers(hand_landmarks):
    fingers = []

    # Coordenadas importantes
    tip_ids = [4, 8, 12, 16, 20]

    # Pulgar (eje X para decidir si está levantado)
    if hand_landmarks.landmark[tip_ids[0]].x < hand_landmarks.landmark[tip_ids[0] - 1].x:
        fingers.append(1)
    else:
        fingers.append(0)

    # Otros 4 dedos (eje Y para decidir)
    for id in range(1, 5):
        if hand_landmarks.landmark[tip_ids[id]].y < hand_landmarks.landmark[tip_ids[id] - 2].y:
            fingers.append(1)
        else:
            fingers.append(0)

    return sum(fingers)

# Captura de video
cap = cv2.VideoCapture(0)

last_count = -1

while True:
    ret, frame = cap.read()
    if not ret:
        break

    frame = cv2.flip(frame, 1)  # Reflejar imagen para mejor control
    frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    results = hands.process(frame_rgb)

    count = 0  # Asumir 0 dedos si no se detecta nada

    if results.multi_hand_landmarks:
        for hand_landmarks in results.multi_hand_landmarks:
            mp_draw.draw_landmarks(frame, hand_landmarks, mp_hands.HAND_CONNECTIONS)
            count = count_fingers(hand_landmarks)

    # Mostrar conteo
    cv2.putText(frame, f'Dedos: {count}', (10, 50),
                cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)

    # Solo enviar si cambia
    if count != last_count:
        arduino.write(f"{count}\n".encode())
        last_count = count

    cv2.imshow('Contador de Dedos', frame)

    if cv2.waitKey(1) & 0xFF == 27:  # Esc para salir
        break

cap.release()
cv2.destroyAllWindows()
arduino.close()

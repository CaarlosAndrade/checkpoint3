import cv2
import mediapipe as mp
import serial
import time

# instanciando variaveis
mp_drawing = mp.solutions.drawing_utils
mp_drawing_styles = mp.solutions.drawing_styles
mp_hands = mp.solutions.hands
hands = mp_hands.Hands(
    model_complexity=0, 
    min_detection_confidence=0.3, 
    min_tracking_confidence=0.3,
    max_num_hands=1
)

font = cv2.FONT_HERSHEY_SIMPLEX
font_scale = 1
thickness = 1

video_capture = cv2.VideoCapture(0)

def setMove(landmark):
    if (landmark[9].y > landmark[12].y):
        return '1'
    elif (landmark[9].x < landmark[12].x):
        return '0'

def main():
    ser = serial.Serial('COM3', 9600) # Altere 'COM3' para a porta serial do seu Arduino
    time.sleep(2) # Dá tempo para a conexão ser estabelecida

    while video_capture.isOpened():
        ret, video = video_capture.read()

        if not ret:
            break

        video = cv2.resize(video, (500,400))
        h, w, _ = video.shape

         # processando o video usando mediapipe
        video = cv2.cvtColor(video, cv2.COLOR_BGR2RGB)
        video.flags.writeable = False
        results = hands.process(video)
        video.flags.writeable = True
        video = cv2.cvtColor(video, cv2.COLOR_RGB2BGR)

         # recuperando os pontos para identificar mão no video
        hand_landmarks = results.multi_hand_landmarks
        if hand_landmarks and len(hand_landmarks):

            for landmarks in hand_landmarks:
                # capturando os pontos de uma mão
                landmark = landmarks.landmark

                move = setMove(landmark)
                
                cv2.putText(video, move, (50,100), font, font_scale, (0,0,0), thickness, cv2.LINE_AA)
                if(move):
                    ser.write(move.encode()) # Envia a mensagem para o Arduino
                    time.sleep(1)

        cv2.imshow("Arduino", video)        

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    video_capture.release()

if __name__ == "__main__":
    main()

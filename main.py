import cv2
import mediapipe as mp
import constants
import controller as cnt

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

move_player_1 = ""
move_player_2 = ""

last_move_player_1 = None
last_move_player_2 = None
winner = None  
scores = [0, 0]

font = cv2.FONT_HERSHEY_SIMPLEX
font_scale = 1
thickness = 1

# atribui jogadas mão direita (player_1) mão esquerda (player_2)
def setMove(landmark):
        if (landmark[9].y > landmark[12].y):
            cnt.led(1)
        elif (landmark[9].x < landmark[12].x):
            cnt.led(0)                 
        
# Definindo ganhador da partida 
def setMatchWinner(move_player_1, move_player_2):
        
        if move_player_1 == move_player_2:
            return 0
        elif move_player_1 == constants.PAPEL:
            return 1 if move_player_2 == constants.PEDRA else 2
        elif move_player_1 == constants.PEDRA:
            return 1 if move_player_2 == constants.TESOURA else 2
        elif move_player_1 == constants.TESOURA:
            return 1 if move_player_2 == constants.PAPEL else 2

# capturando video do desafio
# video_capture = cv2.VideoCapture("pedra-papel-tesoura.mp4")
video_capture = cv2.VideoCapture(0)

while video_capture.isOpened():
    ret, video = video_capture.read()
    if not ret:
        break

    video = cv2.resize(video, (1000,600))
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

            player_1_hand_landmark = landmark
            move_player_1 = setMove(player_1_hand_landmark)
            cv2.putText(video, "Jogador 1", (50,70), font, font_scale, (0,0,0), thickness, cv2.LINE_AA)
            cv2.putText(video, move_player_1, (50,100), font, font_scale, (0,0,0), thickness, cv2.LINE_AA)
            
    cv2.imshow("Game - Rock, Paper, Scissors", video)

   # Esperar pela tecla 'q' para sair
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

video_capture.release()
cv2.destroyAllWindows()
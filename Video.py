# importa a biblioteca principal do OpenCV
import cv2
# define o caminho onde est´a o v´ıdeo que deseja exibir
VIDEO_PATH = " Videos/paisagem01.mp4"
# captura o v´ıdeo
cap = cv2.VideoCapture(VIDEO_PATH)

while True:
    ret, frame = cap.read()
    # verifica se o frame foi lido corretamente
    if not ret:
        break
    # mostra o frame capturado
    cv2.imshow("Video", frame)
    # espera 25 milisegundos
    if cv2.waitKey(25) & 0xFF == ord('q'): break
    
# libera a mem´oria dos frames lidos
cap.release()
# apaga as janelas criadas e encerra o programa
cv2.destroyAllWindows()
import cv2
import numpy as np
# define o caminho e a imagem onde o OpenCv vai encontr´a-la
PATH = "Images-RGB/imco193.jpg"
# Lˆe a imagem
img = cv2.imread(PATH, cv2.IMREAD_GRAYSCALE)

img_normalizada = img.astype(np.float32) /255.0

img_negativo = 1 - img_normalizada



# define uma janela de visualiza¸c˜ao
cv2.namedWindow("Imagem", cv2.WINDOW_NORMAL)
cv2.namedWindow("Negativo", cv2.WINDOW_NORMAL)
# exibe a imagem na janela definida
cv2.imshow("Imagem", img)
cv2.imshow("Negativo", img_negativo)
# aguarda at´e uma tecla ser acionada
cv2.waitKey(0)
# encerra todas as janelas definidas at´e aqui
cv2.destroyAllWindows()

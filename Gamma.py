import cv2
import numpy as np
# define o caminho e a imagem onde o OpenCv vai encontr´a-la
PATH = "ImagensTestes/figura13.png"
# Lˆe a imagem
img = cv2.imread(PATH, cv2.IMREAD_GRAYSCALE)


img_normalizada = img.astype(np.float32) /255.0

c = 1
gamma = 0.5  # < 1 clareia, > 1 escurece

img_gamma = c * np.power(img_normalizada,gamma)
img_final = np.clip(img_gamma * 255,0,255).astype(np.uint8)


# define uma janela de visualiza¸c˜ao
cv2.namedWindow("Imagem", cv2.WINDOW_NORMAL)
cv2.namedWindow("Gama", cv2.WINDOW_NORMAL)
# exibe a imagem na janela definida
cv2.imshow("Imagem", img)
cv2.imshow("Gama", img_final)
# aguarda at´e uma tecla ser acionada
cv2.waitKey(0)
# encerra todas as janelas definidas at´e aqui
cv2.destroyAllWindows()

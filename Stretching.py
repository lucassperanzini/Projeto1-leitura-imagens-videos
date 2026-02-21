import cv2
import numpy as np
# define o caminho e a imagem onde o OpenCv vai encontr´a-la
PATH = "Images-RGB/imco56.jpg"
# Le a imagem
img = cv2.imread(PATH, cv2.IMREAD_GRAYSCALE)

p_min = np.min(img)
p_max = np.max(img)

# 3. Aplica a fórmula de stretching
# Subtraímos o mínimo, dividimos pela amplitude e multiplicamos por 255
img_stretched = (img - p_min) / (p_max - p_min) * 255

# 4. Converte de volta para inteiros de 8 bits
img_stretched = img_stretched.astype(np.uint8)


# define uma janela de visualiza¸c˜ao
cv2.namedWindow("Imagem", cv2.WINDOW_NORMAL)
cv2.namedWindow("Imagem_stretching", cv2.WINDOW_NORMAL)
# exibe a imagem na janela definida
cv2.imshow("Imagem", img)
cv2.imshow("Imagem_stretching", img_stretched)


# aguarda at´e uma tecla ser acionada
cv2.waitKey(0)
# encerra todas as janelas definidas at´e aqui
cv2.destroyAllWindows()

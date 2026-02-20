import cv2
import numpy as np
# define o caminho e a imagem onde o OpenCv vai encontr´a-la
PATH = "Images-RGB/imco14.jpg"
# Lˆe a imagem
img = cv2.imread(PATH)
img_gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
L = 128

altura,largura = img_gray.shape



#matriz vazia com o tamanho da imagem
img_bin = np.zeros((altura,largura),dtype=np.uint8)



# para cada pixel de altura e largura

for i in range(altura):
    for j in range(50):
        if img_gray[i,j] >= L:
            img_bin[i,j] = 255
        else:
            img_bin[i,j] = 0


# Cria Janelas para exibir os resultados
cv2.namedWindow("Original Gray", cv2.WINDOW_NORMAL)
cv2.namedWindow("Binaria", cv2.WINDOW_NORMAL)
# Exibe os resultados nas janelas criadas
cv2.imshow("Original Gray", img_gray)
cv2.imshow("Binaria", img_bin)
# aguarda at´e uma tecla ser acionada
cv2.waitKey(0)
# apaga as janelas criadas e encerra o programa
cv2.destroyAllWindows()

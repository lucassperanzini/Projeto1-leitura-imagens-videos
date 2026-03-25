import cv2
import numpy as np
import sys

# Definir o caminho da imagem
PATH = "ImagensTestMorfologia/region01.png"

# Carregar a imagem em escala de cinza
img = cv2.imread(PATH, cv2.IMREAD_GRAYSCALE)

# Verificação de segurança: evita erro se a imagem não for encontrada
if img is None:
    sys.exit(f"Erro: Não foi possível carregar a imagem em {PATH}. Verifique o caminho.")

# Criar o elemento estruturante (Kernel)
# Um kernel 3x3 de uns é o padrão para operações morfológicas simples
kernel = np.ones((3, 3), np.uint8)

# Aplicar a dilatação
# iterations=1 define quantas vezes a operação será repetida
img_dilate = cv2.dilate(img, kernel, iterations=8)
img_erosao = cv2.erode(img, kernel, iterations=8)


# Configurar as janelas de visualização
# cv2.WINDOW_NORMAL (ou 2) permite redimensionar a janela manualmente
cv2.namedWindow("Original", cv2.WINDOW_NORMAL)
cv2.namedWindow("Dilatada", cv2.WINDOW_NORMAL)
cv2.namedWindow("Erosao", cv2.WINDOW_NORMAL)
# Exibir as imagens
cv2.imshow("Original", img)
cv2.imshow("Dilatada", img_dilate)
cv2.imshow("Erosao", img_erosao)

# Aguarda uma tecla ser pressionada e fecha tudo
cv2.waitKey(0)
cv2.destroyAllWindows()
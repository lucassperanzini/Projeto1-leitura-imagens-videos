import cv2
import numpy as np

PATH = "ImagensTestes/figura09.png"

img = cv2.imread(PATH, cv2.IMREAD_GRAYSCALE)

if img is None:
    print("Erro: Não foi possível carregar a imagem. Verifique o caminho!")
else:
    # 3. Aplica o histograma local

    gaussian_blur =  cv2.GaussianBlur(img, (5, 5), 0)
    
    cv2.imshow("Original (Cinza)", img)
    cv2.imshow("gaussian", gaussian_blur)

   

    cv2.waitKey(0) 
    cv2.destroyAllWindows()
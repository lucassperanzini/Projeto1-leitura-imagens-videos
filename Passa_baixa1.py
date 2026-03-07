import cv2
import numpy as np

PATH = "ImagensTestes/figura09.png"

img = cv2.imread(PATH, cv2.IMREAD_GRAYSCALE)

if img is None:
    print("Erro: Não foi possível carregar a imagem. Verifique o caminho!")
else:
    # 3. Aplica o histograma local
    img_media = cv2.blur(img, (9,9))

    imagem_filtrada = cv2.medianBlur(img, 5)

    kernell3_3 = (1.0 /16.0) * np.array([[1,2,1],
                                         [2,4,2],
                                         [1,2,1]   
                                        ], dtype=np.float32)
    
    img_filt = cv2.filter2D(img, ddepth=-1,kernel=kernell3_3)

    gaussian_blur =  cv2.GaussianBlur(img, (5, 5), 0)
    
    cv2.imshow("Original (Cinza)", img)
    cv2.imshow("mÉDIA", img_media)
    cv2.imshow("Mediana", imagem_filtrada)
    cv2.imshow("gaussian", gaussian_blur)
    cv2.imshow("img filtro", img_filt)
   

    cv2.waitKey(0) 
    cv2.destroyAllWindows()
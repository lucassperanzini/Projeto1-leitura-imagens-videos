import cv2
import numpy as np

PATH = "ImagensTestes/figura09.png"

img = cv2.imread(PATH, cv2.IMREAD_GRAYSCALE)

if img is None:
    print("Erro: Não foi possível carregar a imagem. Verifique o caminho!")
else:


    #Imagem
    #↓
    #Suavização (Gaussian)
    #↓
    #Gradiente (Sobel)
    #↓
    #Refinamento (Canny)


    #quanto o pixel central difere dos vizinhos
    # Laplaciano é sensivel a ruido entao usamos gaussian blur para tirar os ruidos
    gaussian_blur =  cv2.GaussianBlur(img, (3, 3), 0)

    #detectar bordas rapidamente
    #realçar detalhes (sharpening)
    lap = cv2.Laplacian(gaussian_blur, ddepth=cv2.CV_16S,ksize=3)
    lap_abs = cv2.convertScaleAbs(lap)
    g16 = img.astype(np.int16) - lap
    g =np.clip(g16,0,255).astype(np.uint8)



    #como a intensidade muda em uma direção

    #mudanças da esquerda → direita
    #ordas verticais
    sobelx = cv2.Sobel(gaussian_blur, cv2.CV_16S, 1, 0, ksize=3)
    sobel_x = cv2.convertScaleAbs(sobelx)
    #mudanças de cima → baixo
    #bordas horizontais
    sobely = cv2.Sobel(gaussian_blur, cv2.CV_16S, 0, 1, ksize=3)
    sobel_y = cv2.convertScaleAbs(sobely)


  #Força da borda = √(Gx² + Gy²)

    #É um processo completo de detecção de borda
    
    #Imagem
    #↓
    #Suavização (Gaussian)
    #↓
    #Gradiente (Sobel)
    #↓
    #Refinamento (Canny)

    
    canny = cv2.Canny(img, 100, 200)
    #  5️⃣ Threshold duplo
    #👉 separa:

    #bordas fortes
    #bordas fracas

    cv2.imshow("Sobel X", sobel_x)
    cv2.imshow("Sobel Y", sobel_y)
 
    cv2.imshow("Cany", canny)


  
    cv2.imshow("Original (Cinza)", img)
    cv2.imshow("lap", g)
   

    cv2.waitKey(0) 
    cv2.destroyAllWindows()
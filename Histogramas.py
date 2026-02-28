import cv2

PATH = "ImagensTestes/figura08.png"

img = cv2.imread(PATH, cv2.IMREAD_GRAYSCALE)

if img is None:
    print("Erro: Não foi possível carregar a imagem. Verifique o caminho!")
else:
    clahe = cv2.createCLAHE(clipLimit=1.0, tileGridSize=(50, 50))
    
    # 3. Aplica o histograma local
    img_local = clahe.apply(img)

    img_equalizada = cv2.equalizeHist(img)

    cv2.imshow("Original (Cinza)", img)
    cv2.imshow("Imagem Equalizada", img_equalizada)
    cv2.imshow("local",img_local)

    cv2.waitKey(0) 
    cv2.destroyAllWindows()
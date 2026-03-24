import cv2


"""

🎯 Imagine essa imagem 3x3 (9 pixels)
100 100 100
100 120 120
130 130 140

Total de pixels = 9

🧠 PASSO 1 — Contar quantas vezes cada valor aparece

100 aparece 4 vezes

120 aparece 2 vezes

130 aparece 2 vezes

140 aparece 1 vez

🧠 PASSO 2 — Acumular (somar progressivamente)

Agora vamos acumulando:

Até 100 → 4

Até 120 → 4 + 2 = 6

Até 130 → 6 + 2 = 8

Até 140 → 8 + 1 = 9

Tabela:

Valor	Acumulado
100	4
120	6
130	8
140	9
🧠 PASSO 3 — Dividir pelo total (9 pixels)

Agora dividimos cada acumulado por 9:

Valor	Acumulado	÷9
100	4	0.44
120	6	0.66
130	8	0.88
140	9	1.00
🧠 PASSO 4 — Multiplicar por 255

Agora multiplicamos por 255 (porque imagem real vai até 255):

100 → 0.44 × 255 ≈ 112

120 → 0.66 × 255 ≈ 168

130 → 0.88 × 255 ≈ 224

140 → 1.00 × 255 = 255

🎯 Resultado final

A imagem original:

100 100 100
100 120 120
130 130 140

Depois da equalização:

112 112 112
112 168 168
224 224 255

"""


PATH = "ImagensTestes/figura13.png"

img = cv2.imread(PATH, cv2.IMREAD_GRAYSCALE)

if img is None:
    print("Erro: Não foi possível carregar a imagem. Verifique o caminho!")
else:
    clahe = cv2.createCLAHE(clipLimit=2.0, tileGridSize=(5, 5))
    
    # 3. Aplica o histograma local
    img_local = clahe.apply(img)

    img_equalizada = cv2.equalizeHist(img)

    cv2.imshow("Original (Cinza)", img)
    cv2.imshow("Imagem Equalizada", img_equalizada)
    cv2.imshow("local",img_local)

cv2.waitKey(0) 
cv2.destroyAllWindows()
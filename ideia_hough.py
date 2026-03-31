import cv2
import numpy as np

# ============================
# 1. Leitura da imagem (RGB)
# ============================
PATH = "hough/casa04.png"  # <-- troque aqui

img_bgr = cv2.imread(PATH)

if img_bgr is None:
    print("Erro ao carregar a imagem.")
    exit()

# OpenCV lê em BGR → vamos manter assim para desenhar
img_out = img_bgr.copy()

# ============================
# 2. Conversão para grayscale
# ============================
gray = cv2.cvtColor(img_bgr, cv2.COLOR_BGR2GRAY)

# ============================
# 3. Detecção de bordas
# ============================
edges = cv2.Canny(gray, 100 ,200)

# ============================
# 4. Transformada de Hough
# ============================
lines = cv2.HoughLines(
    edges,
    rho=0.5,
    theta=np.pi/180,
    threshold=250
)

# ============================
# 5. Plot das linhas
# ============================
if lines is not None:
    for line in lines:
        rho, theta = line[0]

        # Conversão polar → cartesiano
        a = np.cos(theta)
        b = np.sin(theta)

        x0 = a * rho
        y0 = b * rho

        # Dois pontos distantes na reta
        x1 = int(x0 + 500 * (-b))
        y1 = int(y0 + 500 * (a))

        x2 = int(x0 - 500 * (-b))
        y2 = int(y0 - 500 * (a))

        # Desenha a linha
        cv2.line(img_out, (x1, y1), (x2, y2), (0, 0, 255), 2)

# ============================
# 6. Exibição
# ============================
cv2.namedWindow("Original", cv2.WINDOW_NORMAL)
cv2.imshow("Original", img_bgr)

cv2.namedWindow("Edges", cv2.WINDOW_NORMAL)
cv2.imshow("Edges", edges)

cv2.namedWindow("Hough Lines", cv2.WINDOW_NORMAL)
cv2.imshow("Hough Lines", img_out)

cv2.waitKey(0)
cv2.destroyAllWindows()
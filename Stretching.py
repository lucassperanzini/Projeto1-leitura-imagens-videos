import cv2
import numpy as np
# define o caminho e a imagem onde o OpenCv vai encontr´a-la
PATH = "ImagensTestes/figura08.png"
# Le a imagem


def stretching_pixelwise_gray(img_gray: np.ndarray,r1: int, r2: int, s1: int, s2: int,L: int = 255) -> np.ndarray:

    if img_gray.ndim != 2:
        raise ValueError("img_gray deve ser grayscale (2D).")
    if not (0 < r1 < r2 < L):
        raise ValueError("Precisa de 0 < r1 < r2 < L.")
    if not (0 <= s1 <= L and 0 <= s2 <= L):
        raise ValueError("s1 e s2 devem estar entre 0 e L.")


    out = np.zeros_like(img_gray, dtype=np.uint8)

  
    a1 = s1 / r1
    b1 = 0.0

    a2 = (s2 - s1) / (r2 - r1)
    b2 = s1 - a2 * r1

    a3 = (L - s2) / (L - r2)
    b3 = s2 - a3 * r2

  
    h, w = img_gray.shape
    for x in range(h):
        for y in range(w):
            r = int(img_gray[x, y])

            if r <= r1:
                g = a1 * r + b1
            elif r <= r2:
                g = a2 * r + b2
            else:
                g = a3 * r + b3

       
            g = max(0, min(L, g))
            out[x, y] = int(round(g))

    return out


if __name__ == "__main__":
    img = cv2.imread(PATH, cv2.IMREAD_GRAYSCALE)

    r1, r2 = 100, 120
    s1, s2 = 5, 240 

    out = stretching_pixelwise_gray(img, r1, r2, s1, s2)

    cv2.imshow("Original", img)
    cv2.imshow("Stretching por Partes", out)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
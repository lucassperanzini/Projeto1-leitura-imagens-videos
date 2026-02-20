import cv2

print(cv2.__version__)

IMG_PATH = r"D:\Documents\Nova pasta\PASTAS\FIAP\fiap\4 ano\Applied Compurter Vision\Projeto1\Images-gray\lena.jpg "


def main():
    img = cv2.imread(IMG_PATH, cv2.IMREAD_COLOR)
    altura, largura, canais = img.shape


    print("Altura:", altura)
    print("Largura:", largura)
    print("Canais:", canais)


    cv2.namedWindow("window_name",2)
    cv2.imshow("window_name", img)


    cv2.waitKey(0)
    cv2.destroyAllWindows()





if __name__ == "__main__":
    main()
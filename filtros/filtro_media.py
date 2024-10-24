import cv2
import numpy as np
import matplotlib.pyplot as plt

from tkinter import messagebox

caminho_imagem = 'images/Lenag.pgm'

mascara = np.array([[1, 1, 1],
                    [1, 1, 1],
                    [1, 1, 1]], dtype=np.float32)
mascara = mascara / 9

def filtro_media(imagem, mascara):
    altura, largura = imagem.shape
    kaltura, klargura = mascara.shape

    imagem_filtrada = np.zeros_like(imagem)

    offset_y = kaltura // 2
    offset_x = klargura // 2

    for y in range(altura):
        for x in range(largura):
            soma = 0.0

            for ky in range(kaltura):
                for kx in range(klargura):
                    ny = y + ky - offset_y
                    nx = x + kx - offset_x

                    if 0 <= ny < altura and 0 <= nx < largura:
                        soma += imagem[ny, nx] * mascara[ky, kx]

            imagem_filtrada[y, x] = soma

    return imagem, imagem_filtrada

def on_aplicar_filtro_media():
    try:
        imagem = cv2.imread(caminho_imagem, cv2.IMREAD_GRAYSCALE)
        imagem_original, imagem_filtrada = filtro_media(imagem, mascara)

        plt.subplot(1, 2, 1)
        plt.imshow(imagem_original, cmap='gray')
        plt.title('Imagem Original')
        plt.axis('off')

        plt.subplot(1, 2, 2)
        plt.imshow(imagem_filtrada, cmap='gray')
        plt.title('Filtro de Média (3x3)')
        plt.axis('off')

        plt.show()
    except ValueError as e:
        messagebox.showerror("Erro", str(e))

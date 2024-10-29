import cv2
import numpy as np
from tkinter import Label, messagebox
from PIL import Image, ImageTk

kernel_roberts_x = np.array([[1, 0],
                             [0, -1]], dtype=np.float32)
kernel_roberts_y = np.array([[0, 1],
                             [-1, 0]], dtype=np.float32)

def filtro_roberts(imagem, kernel_x, kernel_y):
    altura, largura = imagem.shape

    imagem_filtrada = np.zeros_like(imagem, dtype=np.float32)

    for y in range(altura - 1):
        for x in range(largura - 1):
            gx = imagem[y, x] * kernel_x[0, 0] + imagem[y, x + 1] * kernel_x[0, 1] + \
                 imagem[y + 1, x] * kernel_x[1, 0] + imagem[y + 1, x + 1] * kernel_x[1, 1]
            gy = imagem[y, x] * kernel_y[0, 0] + imagem[y, x + 1] * kernel_y[0, 1] + \
                 imagem[y + 1, x] * kernel_y[1, 0] + imagem[y + 1, x + 1] * kernel_y[1, 1]

            imagem_filtrada[y, x] = min(max(np.sqrt(gx**2 + gy**2), 0), 255)

    return imagem, imagem_filtrada.astype(np.uint8)

label_original = None
label_filtrada = None

def on_aplicar_filtro_roberts(caminho_imagem, janela_filtro):
    global label_original, label_filtrada

    try:
        imagem = cv2.imread(caminho_imagem, cv2.IMREAD_GRAYSCALE)
        if imagem is None:
            raise ValueError("Erro ao carregar a imagem.")

        imagem_original, imagem_filtrada = filtro_roberts(imagem, kernel_roberts_x, kernel_roberts_y)

        imagem_original_tk = ImageTk.PhotoImage(Image.fromarray(imagem_original))
        imagem_filtrada_tk = ImageTk.PhotoImage(Image.fromarray(imagem_filtrada))

        if label_original is not None:
            label_original.destroy()
        if label_filtrada is not None:
            label_filtrada.destroy()

        label_original = Label(janela_filtro, image=imagem_original_tk, text="Imagem Original", compound="top")
        label_original.image = imagem_original_tk
        label_original.pack(side="left", padx=10)

        label_filtrada = Label(janela_filtro, image=imagem_filtrada_tk, text="Imagem Filtrada", compound="top")
        label_filtrada.image = imagem_filtrada_tk
        label_filtrada.pack(side="right", padx=10)

    except Exception as e:
        messagebox.showerror("Erro", str(e))

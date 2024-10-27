import cv2
import numpy as np
from tkinter import Label, messagebox
from PIL import Image, ImageTk

mascara = np.ones((3, 3), dtype=np.float32) / 9

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

label_original = None
label_filtrada = None

def on_aplicar_filtro_media(caminho_imagem, janela_filtro):
    global label_original, label_filtrada

    try:
        imagem = cv2.imread(caminho_imagem, cv2.IMREAD_GRAYSCALE)
        if imagem is None:
            raise ValueError("Erro ao carregar a imagem.")
        
        imagem_original, imagem_filtrada = filtro_media(imagem, mascara)

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

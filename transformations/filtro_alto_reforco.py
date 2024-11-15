import numpy as np
from PIL import Image, ImageTk
from tkinter import Label

def suavizar_imagem(imagem, tamanho_kernel=3):
    kernel = np.ones((tamanho_kernel, tamanho_kernel), np.float32) / (tamanho_kernel ** 2)
    imagem_array = np.array(imagem, dtype=np.float32)
    altura, largura = imagem_array.shape

    imagem_suavizada = np.zeros_like(imagem_array, dtype=np.float32)

    for i in range(1, altura - 1):
        for j in range(1, largura - 1):
            recorte = imagem_array[i - 1:i + 2, j - 1:j + 2]
            imagem_suavizada[i, j] = np.sum(kernel * recorte)

    imagem_suavizada = np.clip(imagem_suavizada, 0, 255).astype(np.uint8)
    return imagem_suavizada

def aplicar_alto_reforço(imagem, k=1.5):
    imagem_array = np.array(imagem, dtype=np.float32)

    imagem_suavizada = suavizar_imagem(imagem)

    resíduo = imagem_array - imagem_suavizada

    imagem_reforcada = imagem_array + k * resíduo

    imagem_reforcada = np.clip(imagem_reforcada, 0, 255).astype(np.uint8)

    return imagem_reforcada

def on_aplicar_alto_reforco(caminho_imagem, frame, k=1.5):
    imagem = Image.open(caminho_imagem).convert("L")
    resultado = aplicar_alto_reforço(imagem, k)

    imagem_transformada = Image.fromarray(resultado)

    for widget in frame.winfo_children():
        widget.destroy()

    imagem_original_tk = ImageTk.PhotoImage(imagem)
    label_original = Label(frame, image=imagem_original_tk, text="Imagem Original", compound="top")
    label_original.image = imagem_original_tk
    label_original.pack(side="left", padx=10)

    imagem_transformada_tk = ImageTk.PhotoImage(imagem_transformada)
    label_filtrada = Label(frame, image=imagem_transformada_tk, text=f"Filtro de Alto Reforço (k={k})", compound="top")
    label_filtrada.image = imagem_transformada_tk
    label_filtrada.pack(side="right", padx=10)

    frame.image_original = imagem_original_tk
    frame.image_transformada = imagem_transformada_tk
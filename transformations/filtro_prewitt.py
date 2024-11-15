import numpy as np
from PIL import Image, ImageTk
from tkinter import Label, messagebox
import tkinter as tk

def aplicar_prewitt(imagem):
    kernel_horizontal = np.array([[-1, 0, 1], [-1, 0, 1], [-1, 0, 1]])
    kernel_vertical = np.array([[-1, -1, -1], [0, 0, 0], [1, 1, 1]])

    imagem_array = np.array(imagem, dtype=np.float32)
    altura, largura = imagem_array.shape

    resultado = np.zeros((altura - 2, largura - 2), dtype=np.float32)

    for i in range(altura - 2):
        for j in range(largura - 2):
            recorte = imagem_array[i:i + 3, j:j + 3]
            g1 = np.sum(kernel_horizontal * recorte)
            g2 = np.sum(kernel_vertical * recorte)
            resultado[i, j] = np.sqrt(g1**2 + g2**2)

    resultado = np.clip(resultado, 0, 255).astype(np.uint8)
    return resultado

def on_aplicar_filtro_prewitt(caminho_imagem, frame):
    try:
        imagem = Image.open(caminho_imagem).convert("L")
        imagem_tk = ImageTk.PhotoImage(imagem)

        resultado = aplicar_prewitt(imagem)
        imagem_transformada = Image.fromarray(resultado)
        imagem_transformada_tk = ImageTk.PhotoImage(imagem_transformada)

        for widget in frame.winfo_children():
            widget.destroy()

        label_original = Label(frame, image=imagem_tk, text="Imagem Original", compound="top")
        label_original.image = imagem_tk
        label_original.pack(side="left", padx=10)

        label_filtrada = Label(frame, image=imagem_transformada_tk, text="Filtro Prewitt", compound="top")
        label_filtrada.image = imagem_transformada_tk
        label_filtrada.pack(side="right", padx=10)

    except Exception as e:
        messagebox.showerror("Erro", f"Erro ao aplicar o filtro: {e}")

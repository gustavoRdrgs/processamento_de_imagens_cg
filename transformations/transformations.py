import cv2
import numpy as np
import tkinter as tk
from tkinter import simpledialog, messagebox

def negativo_imagem(imagem):
    return 255 - imagem

def transformacao_gamma(imagem, gamma, c=1.0):
    imagem_normalizada = imagem / 255.0
    imagem_gamma = c * np.power(imagem_normalizada, gamma)
    return np.uint8(imagem_gamma * 255)

def transformacao_logaritmica(imagem, a=1.0):
    return np.uint8(a * np.log1p(imagem))

def transferencia_intensidade(imagem, r, w, sigma):
    return np.uint8(255 / (1 + np.exp(-(imagem - w) / sigma)))

def transferencia_faixa_dinamica(imagem):
    min_val = np.min(imagem)
    max_val = np.max(imagem)
    imagem_dinamica = (imagem - min_val) * (255 / (max_val - min_val))
    return np.uint8(imagem_dinamica)

def transferencia_linear(imagem, a, b):
    return np.clip(a * imagem + b, 0, 255)

def aplicar_transformacao(tipo, imagem):
    try:
        if tipo == "Negativo":
            imagem_resultado = negativo_imagem(imagem)
        elif tipo == "Gamma":
            c = float(simpledialog.askstring("Gamma", "Digite o valor de c:"))
            gamma = float(simpledialog.askstring("Gamma", "Digite o valor de gamma (0-1):"))
            imagem_resultado = transformacao_gamma(imagem, gamma, c)
        elif tipo == "Logarítmica":
            a = float(simpledialog.askstring("Logarítmica", "Digite o valor de a:"))
            imagem_resultado = transformacao_logaritmica(imagem, a)
        elif tipo == "Transferência Intensidade":
            r = int(simpledialog.askstring("Transferência Intensidade", "Digite o valor de r (0-255):"))
            w = int(simpledialog.askstring("Transferência Intensidade", "Digite o valor de w (0-255):"))
            sigma = float(simpledialog.askstring("Transferência Intensidade", "Digite o valor de sigma:"))
            imagem_resultado = transferencia_intensidade(imagem, r, w, sigma)
        elif tipo == "Faixa Dinâmica":
            imagem_resultado = transferencia_faixa_dinamica(imagem)
        elif tipo == "Transferência Linear":
            a = float(simpledialog.askstring("Transferência Linear", "Digite o valor de a:"))
            b = float(simpledialog.askstring("Transferência Linear", "Digite o valor de b:"))
            imagem_resultado = transferencia_linear(imagem, a, b)
        else:
            imagem_resultado = None
        
        return imagem_resultado

    except Exception as e:
        messagebox.showerror("Erro", str(e))

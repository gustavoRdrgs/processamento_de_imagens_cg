import cv2
import numpy as np
import tkinter as tk
from tkinter import simpledialog, messagebox

def negativo_imagem(imagem):
    return 255 - imagem

def transformacao_gamma(imagem, gamma, c=1.0):
    if not (0 <= gamma <= 1):
        raise ValueError("O valor de gamma deve estar no intervalo [0, 1].")
    if c <= 0:
        raise ValueError("O valor de c deve ser maior que 0.")
    
    imagem_transformada = c * (imagem ** gamma)
    imagem_resultado = np.clip(imagem_transformada, 0, 255)
    return imagem_resultado.astype(np.uint8)


def transformacao_logaritmica(imagem, a=1.0):
    
    imagem_float = imagem.astype(np.float32) 
    return np.clip(a * np.log1p(imagem_float), 0, 255).astype(np.uint8)

def transferencia_intensidade(imagem, r, w, sigma):
    
    return np.uint8(255 / (1 + np.exp(-(imagem - w) / sigma)))

def transferencia_faixa_dinamica(imagem, w):
  
    min_val = np.min(imagem)
    max_val = np.max(imagem)
    imagem_dinamica = ((imagem - min_val) * (255 / (max_val - min_val))) * w #w_target
    return np.uint8(imagem_dinamica)

def transferencia_linear(imagem, a, b):
    
    return np.clip(a * imagem + b, 0, 255).astype(np.uint8)

def aplicar_transformacao(tipo, imagem):
   
    try:
        if tipo == "Negativo":
            imagem_resultado = negativo_imagem(imagem)
        elif tipo == "Gamma":
            c = float(simpledialog.askstring("Gamma", "Digite o valor de C (ex.: 1 ou 10):"))
            gamma = float(simpledialog.askstring("Gamma", "Digite o valor de gamma (0-1):"))
            imagem_resultado = transformacao_gamma(imagem, gamma, c)
        elif tipo == "Logarítmica":
            a = float(simpledialog.askstring("Logarítmica", "Digite o valor de a:"))
            imagem_resultado = transformacao_logaritmica(imagem, a)
        elif tipo == "Transferência Intensidade Geral":
            r = int(simpledialog.askstring("Transferência Intensidade Geral", "Digite o valor de r (0-255):"))
            w = int(simpledialog.askstring("Transferência Intensidade Geral", "Digite o valor de w (0-255):"))
            sigma = float(simpledialog.askstring("Transferência Intensidade Geral", "Digite o valor de sigma:"))
            imagem_resultado = transferencia_intensidade(imagem, r, w, sigma)
        elif tipo == "Faixa Dinâmica":
            w = int(simpledialog.askstring("Faixa Dinâmica", "Digite o valor de w (0-255):"))
            imagem_resultado = transferencia_faixa_dinamica(imagem, w)
        elif tipo == "Transferência Linear":
            a = float(simpledialog.askstring("Transferência Linear", "Digite o valor de a:"))
            b = float(simpledialog.askstring("Transferência Linear", "Digite o valor de b:"))
            imagem_resultado = transferencia_linear(imagem, a, b)
        else:
            imagem_resultado = None
        
        return imagem_resultado

    except Exception as e:
        messagebox.showerror("Erro", str(e))

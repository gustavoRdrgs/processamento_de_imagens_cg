import tkinter as tk
import numpy as np
import matplotlib.pyplot as plt
import cv2

class Filtro:
    @staticmethod
    # Função que adiciona zeros ao redor da matriz imagem
    def adiciona_zeros(matriz_imagem):
        altura, largura = matriz_imagem.shape
        nova_imagem = np.zeros((altura + 2, largura + 2), dtype=matriz_imagem.dtype)
        nova_imagem[1:-1, 1:-1] = matriz_imagem
        return nova_imagem

class Mediana:
    def __init__(self, matriz_imagem):
        self.matriz_imagem = matriz_imagem
        self.filtro = Filtro()
        self.matriz_imagem = self.filtro.adiciona_zeros(matriz_imagem)

    def aplica_filtro(self):
        altura, largura = self.matriz_imagem.shape
        retorno = np.zeros((altura - 2, largura - 2), dtype=self.matriz_imagem.dtype)

        for i in range(1, altura - 1):
            for j in range(1, largura - 1):
                vetor = [
                    self.matriz_imagem[i - 1][j - 1], self.matriz_imagem[i - 1][j], self.matriz_imagem[i - 1][j + 1],
                    self.matriz_imagem[i][j - 1], self.matriz_imagem[i][j], self.matriz_imagem[i][j + 1],
                    self.matriz_imagem[i + 1][j - 1], self.matriz_imagem[i + 1][j], self.matriz_imagem[i + 1][j + 1]
                ]
                vetor.sort()
                retorno[i - 1][j - 1] = vetor[4]

        return retorno

def on_aplicar_filtro_mediana():
    try:
        imagem = cv2.imread('images/Lenasalp.pgm', cv2.IMREAD_GRAYSCALE)  # Altere o caminho da imagem aqui
        mediana = Mediana(imagem)
        imagem_filtrada = mediana.aplica_filtro()

        plt.subplot(1, 2, 1)
        plt.imshow(imagem, cmap='gray')
        plt.title('Imagem Original')
        plt.axis('off')

        plt.subplot(1, 2, 2)
        plt.imshow(imagem_filtrada, cmap='gray')
        plt.title('Filtro de Mediana (3x3)')
        plt.axis('off')

        plt.show()
    except Exception as e:
        tk.messagebox.showerror("Erro", str(e))

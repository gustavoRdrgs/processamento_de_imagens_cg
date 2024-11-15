import cv2
import numpy as np
import tkinter as tk
from tkinter import simpledialog, messagebox
from tkinter import filedialog
from matplotlib import pyplot as plt

# Funções de Transformação
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

# Função para aplicar a transformação na imagem
def aplicar_transformacao(tipo):
    global imagem
    if imagem is None:
        messagebox.showerror("Erro", "Nenhuma imagem carregada.")
        return

    try:
        if tipo == "Negativo":
            imagem_resultado = negativo_imagem(imagem)
            plt.imshow(imagem_resultado, cmap='gray')
            plt.title("Negativo")
            plt.axis('off')
            plt.show()

        elif tipo == "Gamma":
            c = float(simpledialog.askstring("Gamma", "Digite o valor de c:"))
            gamma = float(simpledialog.askstring("Gamma", "Digite o valor de gamma (0-1):"))
            imagem_resultado = transformacao_gamma(imagem, gamma, c)
            plt.imshow(imagem_resultado, cmap='gray')
            plt.title("Transformação Gamma")
            plt.axis('off')
            plt.show()

        elif tipo == "Logarítmica":
            a = float(simpledialog.askstring("Logarítmica", "Digite o valor de a:"))
            imagem_resultado = transformacao_logaritmica(imagem, a)
            plt.imshow(imagem_resultado, cmap='gray')
            plt.title("Transformação Logarítmica")
            plt.axis('off')
            plt.show()

        elif tipo == "Transferência Intensidade":
            r = int(simpledialog.askstring("Transferência Intensidade", "Digite o valor de r (0-255):"))
            w = int(simpledialog.askstring("Transferência Intensidade", "Digite o valor de w (0-255):"))
            sigma = float(simpledialog.askstring("Transferência Intensidade", "Digite o valor de sigma:"))
            imagem_resultado = transferencia_intensidade(imagem, r, w, sigma)
            plt.imshow(imagem_resultado, cmap='gray')
            plt.title("Transferência de Intensidade")
            plt.axis('off')
            plt.show()

        elif tipo == "Faixa Dinâmica":
            imagem_resultado = transferencia_faixa_dinamica(imagem)
            plt.imshow(imagem_resultado, cmap='gray')
            plt.title("Transformação Faixa Dinâmica")
            plt.axis('off')
            plt.show()

        elif tipo == "Transferência Linear":
            a = float(simpledialog.askstring("Transferência Linear", "Digite o valor de a:"))
            b = float(simpledialog.askstring("Transferência Linear", "Digite o valor de b:"))
            imagem_resultado = transferencia_linear(imagem, a, b)
            plt.imshow(imagem_resultado, cmap='gray')
            plt.title("Transformação Linear")
            plt.axis('off')
            plt.show()

    except Exception as e:
        messagebox.showerror("Erro", str(e))

# Função para carregar a imagem selecionada
def carregar_imagem():
    global imagem
    caminho_imagem = f'images/{imagem_selecionada.get()}'
    imagem_carregada = cv2.imread(caminho_imagem, cv2.IMREAD_GRAYSCALE)

    if imagem_carregada is None:
        messagebox.showerror("Erro", f"A imagem {imagem_selecionada.get()} não pôde ser carregada.")
    else:
        imagem = imagem_carregada
        messagebox.showinfo("Imagem Carregada", f"A imagem {imagem_selecionada.get()} foi carregada com sucesso!")

# Configuração da interface Tkinter
janela_transformacoes = None  # Variável global para controlar a janela de transformações

def abrir_tela_transformacoes_intensidade(janela_principal):
    global janela_transformacoes

    # Verifique se a janela já está aberta e feche-a antes de abrir uma nova
    if janela_transformacoes is not None and janela_transformacoes.winfo_exists():
        janela_transformacoes.destroy()

    janela_transformacoes = tk.Toplevel(janela_principal)
    janela_transformacoes.title("Transformações de Intensidade")
    janela_transformacoes.geometry("300x400")

    # Funções para cada transformação
    def aplicar_negativo():
        aplicar_transformacao("Negativo")

    def aplicar_gamma():
        aplicar_transformacao("Gamma")

    def aplicar_logaritmica():
        aplicar_transformacao("Logarítmica")

    def aplicar_transferencia_intensidade():
        aplicar_transformacao("Transferência Intensidade")

    def aplicar_faixa_dinamica():
        aplicar_transformacao("Faixa Dinâmica")

    def aplicar_transferencia_linear():
        aplicar_transformacao("Transferência Linear")

    # Botões para cada transformação
    botao_negativo = tk.Button(janela_transformacoes, text="Negativo", command=aplicar_negativo)
    botao_negativo.pack(pady=10)

    botao_gamma = tk.Button(janela_transformacoes, text="Transformação Gamma", command=aplicar_gamma)
    botao_gamma.pack(pady=10)

    botao_logaritmica = tk.Button(janela_transformacoes, text="Transformação Logarítmica", command=aplicar_logaritmica)
    botao_logaritmica.pack(pady=10)

    botao_transferencia = tk.Button(janela_transformacoes, text="Transferência de Intensidade", command=aplicar_transferencia_intensidade)
    botao_transferencia.pack(pady=10)

    botao_faixa_dinamica = tk.Button(janela_transformacoes, text="Faixa Dinâmica", command=aplicar_faixa_dinamica)
    botao_faixa_dinamica.pack(pady=10)

    botao_transferencia_linear = tk.Button(janela_transformacoes, text="Transferência Linear", command=aplicar_transferencia_linear)
    botao_transferencia_linear.pack(pady=10)

# Configuração principal da interface
janela_principal = tk.Tk()
janela_principal.title("Transformações de Imagem")

# Variável para selecionar a imagem
imagem_selecionada = tk.StringVar(janela_principal)
imagem_selecionada.set("Lena.pgm")  # Imagem padrão ao iniciar

# Opções de imagens
opcoes_imagens = ["Lenag.pgm", "Airplane.pgm", "Lenasalp.pgm", "Lena.pgm"]

# Criar dropdown para seleção da imagem
menu_imagens = tk.OptionMenu(janela_principal, imagem_selecionada, *opcoes_imagens)
menu_imagens.pack(pady=10)

# Botão para carregar a imagem selecionada
botao_carregar_imagem = tk.Button(janela_principal, text="Carregar Imagem", command=carregar_imagem)
botao_carregar_imagem.pack(pady=10)

# Botão para abrir a tela de transformações de intensidade
botao_transformacoes_intensidade = tk.Button(janela_principal, text="Transformações de Intensidade", command=lambda: abrir_tela_transformacoes_intensidade(janela_principal))
botao_transformacoes_intensidade.pack(pady=10)

janela_principal.mainloop()


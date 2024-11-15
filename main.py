import tkinter as tk
from transformations.filtro_media import on_aplicar_filtro_media
from transformations.filtro_mediana import on_aplicar_filtro_mediana
from transformations.filtro_passa_alta import on_aplicar_filtro_passa_alta
from transformations.filtro_roberts import on_aplicar_filtro_roberts
from transformations.filtro_roberts_cruzado import on_aplicar_filtro_roberts_cruzado
from transformations.filtro_prewitt import on_aplicar_filtro_prewitt
from transformations.filtro_alto_reforco import on_aplicar_alto_reforco
from transformations.filtro_sobel import on_aplicar_filtro_sobel
from transformations.morfologia import on_aplicar_morfologia
import numpy as np

def formatar_matriz(matriz):
    return "\n".join(["\t".join([f"{elem:.2f}" for elem in linha]) for linha in matriz])

def abrir_tela_filtro(filtro_funcao=None, is_morfologico=False):
    janela_filtro = tk.Toplevel(janela)
    janela_filtro.title("Aplicar Filtro")
    janela_filtro.geometry("800x600")

    caminho_imagens = 'images'
    imagem_selecionada = tk.StringVar(janela_filtro)

    if is_morfologico:
        imagem_selecionada.set("fingerprint.pbm")
        opcoes_imagens = ["fingerprint.pbm", "map.pbm", "holes.pbm"]
    else:
        imagem_selecionada.set("Lena.pgm")
        opcoes_imagens = ["Lenag.pgm", "Airplane.pgm", "Lenasalp.pgm", "Lena.pgm"]

    menu_imagens = tk.OptionMenu(janela_filtro, imagem_selecionada, *opcoes_imagens)
    menu_imagens.pack(pady=5)

    if is_morfologico:
        operacao_morfologica = tk.StringVar(janela_filtro)
        operacao_morfologica.set("Erosão")

        opcoes_operacoes = [
            "Erosão", "Dilatação", "Abertura", "Fechamento",
            "Gradiente", "Contorno Externo", "Contorno Interno",
            "Top Hat", "Bottom Hat"
        ]
        menu_operacoes = tk.OptionMenu(janela_filtro, operacao_morfologica, *opcoes_operacoes)
        menu_operacoes.pack(pady=5)

    frame_imagens = tk.Frame(janela_filtro)
    frame_imagens.pack(pady=10, expand=True)

    filtro_var = tk.StringVar(janela_filtro)
    filtro_var.set("Filtro da Média")

    if not is_morfologico:
        label_matriz = tk.Label(janela_filtro, text="Matriz Aplicada: ", justify="left")
        label_matriz.pack(pady=10)

    if not is_morfologico:
        opcoes_filtros = [
            "Filtro da Média",
            "Filtro da Mediana",
            "Filtro Passa Alta",
            "Filtro Roberts",
            "Filtro Roberts Cruzado",
            "Filtro Prewitt",
            "Filtro de Alto Reforço",
            "Filtro Sobel"
        ]
        menu_filtros = tk.OptionMenu(janela_filtro, filtro_var, *opcoes_filtros)
        menu_filtros.pack(pady=5)

    label_k = tk.Label(janela_filtro, text="Fator K:")
    entry_k = tk.Entry(janela_filtro)
    label_k.pack_forget()
    entry_k.pack_forget()

    def aplicar_filtro():
        caminho_imagem = f"{caminho_imagens}/{imagem_selecionada.get()}"
        matriz_aplicada = ""

        if is_morfologico:
            operacao = operacao_morfologica.get()
            on_aplicar_morfologia(caminho_imagem, frame_imagens, operacao)
        else:
            filtro = filtro_var.get()
            if filtro == "Filtro da Média":
                matriz_aplicada = on_aplicar_filtro_media(caminho_imagem, frame_imagens)
            elif filtro == "Filtro da Mediana":
                matriz_aplicada = ""
                on_aplicar_filtro_mediana(caminho_imagem, frame_imagens)
            elif filtro == "Filtro Passa Alta":
                matriz_aplicada = np.array([[-1, -1, -1], [-1, 8, -1], [-1, -1, -1]])
                on_aplicar_filtro_passa_alta(caminho_imagem, frame_imagens)
            elif filtro == "Filtro Roberts":
                matriz_aplicada = "\n[1 0]  [1 -1]\n[-1 0]  [0 0]"
                on_aplicar_filtro_roberts(caminho_imagem, frame_imagens)
            elif filtro == "Filtro Roberts Cruzado":
                matriz_aplicada = "\n[1 0]  [0 -1]\n[0 1]  [-1 0]"
                on_aplicar_filtro_roberts_cruzado(caminho_imagem, frame_imagens)
            elif filtro == "Filtro Prewitt":
                matriz_aplicada = "\n[-1 0 1]   [-1 -1 -1]\n[-1 0 1]   [0 0 0]\n[-1 0 1]   [1 1 1]"
                on_aplicar_filtro_prewitt(caminho_imagem, frame_imagens)
            elif filtro == "Filtro Sobel":
                matriz_aplicada = "\n[-1 0 1]   [-1 -2 -1]\n[-2 0 1]   [0 0 0]\n[-1 0 1]   [1 2 1]"
                on_aplicar_filtro_sobel(caminho_imagem, frame_imagens)
            elif filtro == "Filtro de Alto Reforço":
                try:
                    k = float(entry_k.get())
                except ValueError:
                    k = 1.5
                on_aplicar_alto_reforco(caminho_imagem, frame_imagens, k)

        if isinstance(matriz_aplicada, np.ndarray):
            matriz_formatada = formatar_matriz(matriz_aplicada)
        else:
            matriz_formatada = matriz_aplicada

        if not is_morfologico:
            label_matriz.config(text=f"Máscara Aplicada:\n{matriz_formatada}")

    def mostrar_caixa_k(*args):
        if filtro_var.get() == "Filtro de Alto Reforço":
            label_k.pack(pady=5)
            entry_k.pack(pady=5)
        else:
            label_k.pack_forget()
            entry_k.pack_forget()

    filtro_var.trace("w", mostrar_caixa_k)

    botao_aplicar = tk.Button(janela_filtro, text="Aplicar Filtro", command=aplicar_filtro)
    botao_aplicar.pack(pady=10)

janela = tk.Tk()
janela.title("Seleção de Filtro")
janela.geometry("300x250")

botao_filtros_imagem = tk.Button(janela, text="Filtros de Imagem", command=abrir_tela_filtro)
botao_filtros_imagem.pack(pady=10)

botao_morfologia = tk.Button(janela, text="Operadores Morfológicos", command=lambda: abrir_tela_filtro(is_morfologico=True))
botao_morfologia.pack(pady=10)

janela.mainloop()

import tkinter as tk
from transformations.filtro_media import on_aplicar_filtro_media
from transformations.filtro_mediana import on_aplicar_filtro_mediana
from transformations.filtro_passa_alta import on_aplicar_filtro_passa_alta
from transformations.roberts import on_aplicar_filtro_roberts
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
    filtro_var.set("Filtro de Média")

    if not is_morfologico:
        label_matriz = tk.Label(janela_filtro, text="Matriz Aplicada: ", justify="left")
        label_matriz.pack(pady=10)

    if not is_morfologico:
        opcoes_filtros = ["Filtro de Média", "Filtro de Mediana", "Filtro Passa Alta", "Filtro Roberts"]
        menu_filtros = tk.OptionMenu(janela_filtro, filtro_var, *opcoes_filtros)
        menu_filtros.pack(pady=5)

    def aplicar_filtro():
        caminho_imagem = f"{caminho_imagens}/{imagem_selecionada.get()}"
        if is_morfologico:
            operacao = operacao_morfologica.get()
            on_aplicar_morfologia(caminho_imagem, frame_imagens, operacao)
        else:
            filtro = filtro_var.get()
            if filtro == "Filtro de Média":
                matriz_aplicada = np.ones((3, 3), dtype=np.float32) / 9
                on_aplicar_filtro_media(caminho_imagem, frame_imagens)
            elif filtro == "Filtro de Mediana":
                matriz_aplicada = ""
                on_aplicar_filtro_mediana(caminho_imagem, frame_imagens)
            elif filtro == "Filtro Passa Alta":
                matriz_aplicada = np.array([[-1, -1, -1], [-1, 8, -1], [-1, -1, -1]])
                on_aplicar_filtro_passa_alta(caminho_imagem, frame_imagens)
            elif filtro == "Filtro Roberts":
                matriz_aplicada = np.array([[1, 0], [0, -1]])
                on_aplicar_filtro_roberts(caminho_imagem, frame_imagens)

        # Exibe a matriz aplicada
        if isinstance(matriz_aplicada, np.ndarray):
            matriz_formatada = formatar_matriz(matriz_aplicada)
        else:
            matriz_formatada = matriz_aplicada

        if not is_morfologico:
            label_matriz.config(text=f"Matriz Aplicada:\n{matriz_formatada}")

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

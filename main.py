import tkinter as tk
from filtros.filtro_media import on_aplicar_filtro_media
from filtros.filtro_mediana import on_aplicar_filtro_mediana
from filtros.filtro_passa_alta import on_aplicar_filtro_passa_alta
from filtros.roberts import on_aplicar_filtro_roberts
from filtros.morfologia import on_aplicar_morfologia 

def abrir_tela_filtro(filtro_funcao, is_morfologico=False):
    janela_filtro = tk.Toplevel(janela)
    janela_filtro.title("Aplicar Filtro")
    janela_filtro.geometry("600x400")

    caminho_imagens = 'images'
    imagem_selecionada = tk.StringVar(janela_filtro)
    imagem_selecionada.set("Lena.pgm")

    if is_morfologico:
        opcoes_imagens = ["Lenag.pgm", "Airplane.pgm", "Lenasalp.pgm", "Lena.pgm", "fingerprint.pbm", "map.pbm", "holes.pbm"]
    else:
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

    def aplicar_filtro():
        caminho_imagem = f"{caminho_imagens}/{imagem_selecionada.get()}"
        if is_morfologico:
            operacao = operacao_morfologica.get()
            on_aplicar_morfologia(caminho_imagem, janela_filtro, operacao)
        else:
            filtro_funcao(caminho_imagem, janela_filtro)

    botao_aplicar = tk.Button(janela_filtro, text="Aplicar Filtro", command=aplicar_filtro)
    botao_aplicar.pack(pady=10)

janela = tk.Tk()
janela.title("Seleção de Filtro")
janela.geometry("300x250")

botao_media = tk.Button(janela, text="Filtro de Média", command=lambda: abrir_tela_filtro(on_aplicar_filtro_media))
botao_media.pack(pady=10)

botao_mediana = tk.Button(janela, text="Filtro de Mediana", command=lambda: abrir_tela_filtro(on_aplicar_filtro_mediana))
botao_mediana.pack(pady=10)

botao_passa_alta = tk.Button(janela, text="Filtro Passa Alta", command=lambda: abrir_tela_filtro(on_aplicar_filtro_passa_alta))
botao_passa_alta.pack(pady=10)

botao_roberts = tk.Button(janela, text="Filtro Roberts", command=lambda: abrir_tela_filtro(on_aplicar_filtro_roberts))
botao_roberts.pack(pady=10)

botao_morfologia = tk.Button(janela, text="Operadores Morfológicos", command=lambda: abrir_tela_filtro(on_aplicar_morfologia, is_morfologico=True))
botao_morfologia.pack(pady=10)

janela.mainloop()

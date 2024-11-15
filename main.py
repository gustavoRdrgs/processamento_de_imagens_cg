import tkinter as tk
from screens.screen_filters import abrir_tela_filtro
from screens.screen_math_operations import abrir_tela_operacoes_imagem

janela = tk.Tk()
janela.title("Seleção de Filtro")
janela.geometry("300x250")

botao_filtros_imagem = tk.Button(janela, text="Filtros de Imagem", command=lambda: abrir_tela_filtro(janela))
botao_filtros_imagem.pack(pady=10)

botao_operacoes_imagem = tk.Button(janela, text="Operações com Imagem", command=lambda: abrir_tela_operacoes_imagem(janela))
botao_operacoes_imagem.pack(pady=10)

botao_morfologia = tk.Button(janela, text="Operadores Morfológicos", command=lambda: abrir_tela_filtro(janela, is_morfologico=True))
botao_morfologia.pack(pady=10)

janela.mainloop()

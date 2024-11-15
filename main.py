import tkinter as tk
from screens.screen_filters import abrir_tela_filtro
from screens.screen_math_operations import abrir_tela_operacoes_imagem
from screens.screen_intensity_transformations import abrir_tela_transformacoes_intensidade

janela = tk.Tk()
janela.title("Seleção de Filtro")
janela.geometry("300x250")

# Botão para abrir a tela de filtros de imagem
botao_filtros_imagem = tk.Button(janela, text="Filtros de Imagem", command=lambda: abrir_tela_filtro(janela))
botao_filtros_imagem.pack(pady=10)

# Botão para abrir a tela de operações com imagem
botao_operacoes_imagem = tk.Button(janela, text="Operações com Imagem", command=lambda: abrir_tela_operacoes_imagem(janela))
botao_operacoes_imagem.pack(pady=10)

# Botão para abrir a tela de operadores morfológicos
botao_morfologia = tk.Button(janela, text="Operadores Morfológicos", command=lambda: abrir_tela_filtro(janela, is_morfologico=True))
botao_morfologia.pack(pady=10)

# Botão para abrir a tela de transformações de intensidade
botao_transformacoes_intensidade = tk.Button(janela, text="Transformações de Intensidade", command=lambda: abrir_tela_transformacoes_intensidade(janela))
botao_transformacoes_intensidade.pack(pady=10)

janela.mainloop()

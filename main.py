import tkinter as tk
import numpy as np
import matplotlib.pyplot as plt
from filtros.filtro_media import on_aplicar_filtro_media
from filtros.filtro_mediana import on_aplicar_filtro_mediana

janela = tk.Tk()
janela.title("Aplicar Filtros")
janela.geometry("300x200")

# Botão para aplicar o filtro de média
botao_media = tk.Button(janela, text="Aplicar Filtro de Média", command=on_aplicar_filtro_media)
botao_media.pack(pady=10)

# Botão para aplicar o filtro de mediana
botao_mediana = tk.Button(janela, text="Aplicar Filtro de Mediana", command=on_aplicar_filtro_mediana)
botao_mediana.pack(pady=10)

janela.mainloop()

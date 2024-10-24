import tkinter as tk
import numpy as np
import matplotlib.pyplot as plt

from filtros.filtro_media import on_aplicar_filtro_media

janela = tk.Tk()
janela.title("Aplicar Filtro de Média")
janela.geometry("300x150")

botao = tk.Button(janela, text="Aplicar Filtro de Média", command=on_aplicar_filtro_media)
botao.pack(pady=20)

janela.mainloop()

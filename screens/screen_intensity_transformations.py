import tkinter as tk
from tkinter import simpledialog, messagebox
from transformations.transformations import aplicar_transformacao

def abrir_tela_transformacoes_intensidade(janela):
    janela_transformacoes = tk.Toplevel(janela)
    janela_transformacoes.title("Transformações de Intensidade")
    janela_transformacoes.geometry("800x600")

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

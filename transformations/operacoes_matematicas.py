import cv2
import numpy as np
from utils.carregar_imagem import carregar_imagem
from utils.salvar_imagem_pgm import salvar_imagem_pgm
import warnings

def soma_imagens(imagem1, imagem2):
    img1 = carregar_imagem(imagem1)
    img2 = carregar_imagem(imagem2)
    
    resultado = np.zeros_like(img1)

    for i in range(img1.shape[0]):
        for j in range(img1.shape[1]):
            resultado[i, j] = max(0, min(255, img1[i, j] + img2[i, j]))
    
    pathing_image = salvar_imagem_pgm(resultado, 'resultado_soma.pgm')
    return pathing_image

def subtracao_imagens(imagem1, imagem2):
    img1 = carregar_imagem(imagem1)
    img2 = carregar_imagem(imagem2)

    resultado = np.zeros_like(img1)

    for i in range(img1.shape[0]):
        for j in range(img1.shape[1]):
            resultado[i, j] = max(0, min(255, img1[i, j] - img2[i, j]))
    
    pathing_image = salvar_imagem_pgm(resultado, 'resultado_subtracao.pgm')
    return pathing_image

def multiplicacao_imagens(imagem1, imagem2):
    img1 = carregar_imagem(imagem1)
    img2 = carregar_imagem(imagem2)

    resultado = np.zeros_like(img1)

    for i in range(img1.shape[0]):
        for j in range(img1.shape[1]):
            resultado[i, j] = max(0, min(255, img1[i, j] * img2[i, j]))
    
    pathing_image = salvar_imagem_pgm(resultado, 'resultado_multiplicacao.pgm')
    return pathing_image

def divisao_imagens(imagem1, imagem2):
    img1 = carregar_imagem(imagem1)
    img2 = carregar_imagem(imagem2)

    resultado = np.zeros_like(img1)

    for i in range(img1.shape[0]):
        for j in range(img1.shape[1]):
            if img2[i, j] != 0:
                resultado[i, j] = max(0, min(255, img1[i, j] / img2[i, j]))
            else:
                resultado[i, j] = 0

    pathing_image = salvar_imagem_pgm(resultado, 'resultado_divisao.pgm')
    return pathing_image

def or_imagens(imagem1, imagem2):
    img1 = carregar_imagem(imagem1)
    img2 = carregar_imagem(imagem2)

    resultado = np.zeros_like(img1)

    for i in range(img1.shape[0]):
        for j in range(img1.shape[1]):
            resultado[i, j] = max(0, min(255, img1[i, j] | img2[i, j]))

    pathing_image = salvar_imagem_pgm(resultado, 'resultado_or.pgm')
    return pathing_image

def and_imagens(imagem1, imagem2):
    img1 = carregar_imagem(imagem1)
    img2 = carregar_imagem(imagem2)

    resultado = np.zeros_like(img1)

    for i in range(img1.shape[0]):
        for j in range(img1.shape[1]):
            resultado[i, j] = max(0, min(255, img1[i, j] & img2[i, j]))

    pathing_image = salvar_imagem_pgm(resultado, 'resultado_and.pgm')
    return pathing_image

def xor_imagens(imagem1, imagem2):
    img1 = carregar_imagem(imagem1)
    img2 = carregar_imagem(imagem2)

    resultado = np.zeros_like(img1)

    for i in range(img1.shape[0]):
        for j in range(img1.shape[1]):
            resultado[i, j] = max(0, min(255, img1[i, j] ^ img2[i, j]))

    pathing_image = salvar_imagem_pgm(resultado, 'resultado_xor.pgm')
    return pathing_image

warnings.simplefilter("ignore", category=RuntimeWarning)
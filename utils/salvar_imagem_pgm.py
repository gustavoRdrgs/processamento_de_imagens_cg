import os
import cv2

def salvar_imagem_pgm(imagem_resultado, nome_arquivo, destino_pasta="images/images_result_operations"):
    if not os.path.exists(destino_pasta):
        os.makedirs(destino_pasta)
    
    caminho_arquivo = os.path.join(destino_pasta, nome_arquivo)

    cv2.imwrite(caminho_arquivo, imagem_resultado)
    
    return caminho_arquivo
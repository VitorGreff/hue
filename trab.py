import cv2
import numpy as np
import matplotlib.pyplot as plt

def plot_results(before, after):
    plt.figure(figsize = ((10, 5)))
    plt.subplot(1, 2, 1)
    plt.imshow(cv2.cvtColor(before, cv2.COLOR_BGR2RGB))
    plt.title("antes", fontsize = 10)
    plt.subplot(1, 2, 2)
    plt.imshow(after)
    plt.title("depois", fontsize = 10)
    plt.show()  

# Função para realizar a alteração na faixa de matizes
# a -> imagem, m -> intervalo, x -> variação
def alterar_faixa_matizes(a, m, x):
    # Converter a imagem para o espaço de cores HSV
    imagem_hsv = cv2.cvtColor(a, cv2.COLOR_BGR2HSV)
    # print(f'm : {m}\nx : {x}')
    
    aux_max = np.mod((m + x)/2, 180)
    aux_min = np.mod((m - x)/2, 180)
    
    matiz_max = max(aux_max, aux_min)
    matiz_min = min(aux_max, aux_min) 

    print(matiz_min, " ", matiz_max)

    imagem_hsv[:, :, 0] = np.where(
        # Checar condição
        (imagem_hsv[:, :, 0] >= matiz_min) & (imagem_hsv[:, :, 0] <= matiz_max),
        (imagem_hsv[:, :, 0] + 90) % 180,
        imagem_hsv[:, :, 0] 
    )

    imagem_rgb = cv2.cvtColor(imagem_hsv, cv2.COLOR_HSV2RGB)
    plot_results(a, imagem_rgb)

def main():
    imagem_entrada = cv2.imread("circulo_cromatico.jpeg") # BGR
    alterar_faixa_matizes(imagem_entrada, 60, 30)

    # imagem_entrada = cv2.imread("circulo.jpg") # BGR
    # alterar_faixa_matizes(imagem_entrada, 75, 30)

    # imagem_entrada = cv2.imread("aves.jpg") # BGR
    # alterar_faixa_matizes(imagem_entrada, 20, 38)

    # imagem_entrada = cv2.imread("teste.jpg") # BGR
    # alterar_faixa_matizes(imagem_entrada, 60, 30)

    # imagem_entrada = cv2.imread("gato.jpg") # BGR
    # alterar_faixa_matizes(imagem_entrada, 225, 40)


if __name__ == "__main__":
    main()



import cv2
import numpy as np
import matplotlib.pyplot as plt

# Função para realizar a alteração na faixa de matizes
# a -> imagem, m -> intervalo, x -> variação
def alterar_faixa_matizes(a, m, x):
    # Converter a imagem para o espaço de cores HSV
    imagem_hsv = cv2.cvtColor(a, cv2.COLOR_BGR2HSV)
    # Checar limites
    if m + x > 359:
        matiz_max = m + x - 360
    else:
        matiz_max = m + x
    
    if m - x < 0:
        matiz_min = m - x + 360
    else:
        matiz_min = m - x

    print(matiz_min, " ",matiz_max)

    imagem_hsv[:, :, 0] = np.where(
        # Checar condição
        (imagem_hsv[:, :, 0] >= matiz_max) & (imagem_hsv[:, :, 0] <= matiz_min),
        (imagem_hsv[:, :, 0] + 180),
        imagem_hsv[:, :, 0]
    )

    # Converter a imagem de volta para o espaço de cores RGB
    imagem_rgb = cv2.cvtColor(imagem_hsv, cv2.COLOR_HSV2RGB)

    return imagem_rgb

imagem_entrada = cv2.imread("circulo.jpg")
imagem_saida = alterar_faixa_matizes(imagem_entrada, 20, 350)

plt.figure(figsize = ((12, 6)))
plt.subplot(1, 2, 2)
plt.imshow(imagem_entrada)
plt.title("depois", fontsize = 10)
plt.subplot(1, 2, 1)
plt.imshow(imagem_saida)
plt.title("antes", fontsize = 10)
plt.show()  
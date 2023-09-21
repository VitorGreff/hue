import cv2
import numpy as np
import matplotlib.pyplot as plt

def plot_results(before, after):
    plt.figure(figsize=((10, 5)))
    plt.subplot(1, 2, 1)
    # a imagem original estava no padrão BGR
    plt.imshow(cv2.cvtColor(before, cv2.COLOR_BGR2RGB))
    plt.title("antes", fontsize=10)
    plt.subplot(1, 2, 2)
    plt.imshow(after)
    plt.title("depois", fontsize=10)
    plt.show()

# a -> imagem, m -> intervalo, x -> variação
def alterar_faixa_matizes(a, m, x):
    # converte a imagem para o padrão HSV de 16 bits
    imagem_hsv = cv2.cvtColor(a, cv2.COLOR_BGR2HSV).astype(np.uint16)
    # extrai os limites (a lib usa 180 graus para a representação da matiz)
    matiz_max = np.mod((m + x) / 2, 180)
    matiz_min = np.mod((m - x) / 2, 180)

    print(f"[Min] {matiz_min*2} <--> {matiz_max*2} [Max]")

    if matiz_min < matiz_max:
        # Não precisa de ajustes circulares, pois matiz_min é menor que matiz_max
        imagem_hsv[:, :, 0] = np.where(
            (imagem_hsv[:, :, 0] >= matiz_min) & (imagem_hsv[:, :, 0] <= matiz_max),
            (imagem_hsv[:, :, 0] + 90) % 180,
            imagem_hsv[:, :, 0]
        )
    elif matiz_min > matiz_max:
        # Ajuste circular para o caso em que matiz_min é maior que matiz_max
        imagem_hsv[:, :, 0] = np.where(
            ((imagem_hsv[:, :, 0] >= matiz_min) & (imagem_hsv[:, :, 0] <= 179)) |
            ((imagem_hsv[:, :, 0] >= 0) & (imagem_hsv[:, :, 0] <= matiz_max)),
            (imagem_hsv[:, :, 0] + 90) % 180,
            imagem_hsv[:, :, 0]
        )

    # converte o resultado da imagem para 8 bits e pro padrão RGB
    imagem_rgb = cv2.cvtColor(imagem_hsv.astype(np.uint8), cv2.COLOR_HSV2RGB)
    plot_results(a, imagem_rgb)

def main():
    imagem_entrada = cv2.imread("circulo_cromatico.jpeg") 
    alterar_faixa_matizes(imagem_entrada, 100, 20)

    imagem_entrada = cv2.imread("circulo.jpg") 
    alterar_faixa_matizes(imagem_entrada, 20, 38)

    imagem_entrada = cv2.imread("circulo2.png")  
    alterar_faixa_matizes(imagem_entrada, 30, 70)

    imagem_entrada = cv2.imread("circulo3.png")  
    alterar_faixa_matizes(imagem_entrada, 30, 70)

    # imagem_entrada = cv2.imread("fmuseum.jpg")  
    # alterar_faixa_matizes(imagem_entrada, 20, 38)

    # imagem_entrada = cv2.imread(".jpg")  
    # alterar_faixa_matizes(imagem_entrada, 60, 30)

    # imagem_entrada = cv2.imread("square.jpeg")  
    # alterar_faixa_matizes(imagem_entrada, 20, 38)

if __name__ == "__main__":
    main()

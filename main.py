import cv2
import numpy as np
import matplotlib.pyplot as plt
import util

# a -> imagem, m -> intervalo, x -> variação
def alter_hue(a, m, x):
    # converte a imagem para o padrão HSV de 16 bits
    imagem_hsv = cv2.cvtColor(a, cv2.COLOR_BGR2HSV).astype(np.uint16)
    # extrai os limites (a lib usa 180 graus para a representação da matiz)
    matiz_max = np.mod((m + x) / 2, 180)
    matiz_min = np.mod((m - x) / 2, 180)

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
    util.plot_results(a, imagem_rgb)

if __name__ == "__main__":
    op = 0
    lista = util.open_folder()
    while op != 3:
        print("\n[1] Listar imagens")
        print("[2] Inveter matiz")
        print("[3] Encerrar programa")
        op = int(input("\nSelecione uma opção: "))
        if op == 1:
            for imagem in lista:
                print(imagem)
        elif op == 2:
            name = str(input("Digite o nome da imagem: ")) + ".png"
            m = int(input("Digite um valor para m: "))
            x = int(input("Digite um valor para x: "))
            if name in lista:
                imagem = cv2.imread(util.convert_path(name))
                alter_hue(imagem, m, x)
            else:
                print("Imagem inválida!")
                continue
        elif op == 3:
            print("Encerrando.")
            continue
        else: 
            print("Opção inválida!")

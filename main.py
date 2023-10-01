import cv2
import numpy as np
import util

def altera_matiz(a, m, x):
    imagem_hsv = cv2.cvtColor(a, cv2.COLOR_BGR2HSV).astype(np.uint16)
    matiz_max = int(np.mod((m + x) / 2, 180))
    matiz_min = int(np.mod((m - x) / 2, 180))

    if matiz_min < matiz_max:
        imagem_hsv[:, :, 0] = np.where(
            (imagem_hsv[:, :, 0] >= matiz_min) & (imagem_hsv[:, :, 0] <= matiz_max),
            (imagem_hsv[:, :, 0] + 90) % 180,
            imagem_hsv[:, :, 0]
        )
    elif matiz_min > matiz_max:
        imagem_hsv[:, :, 0] = np.where(
            ((imagem_hsv[:, :, 0] >= matiz_min) & (imagem_hsv[:, :, 0] <= 179)) |
            ((imagem_hsv[:, :, 0] >= 0) & (imagem_hsv[:, :, 0] <= matiz_max)),
            (imagem_hsv[:, :, 0] + 90) % 180,
            imagem_hsv[:, :, 0]
        )
    imagem_rgb = cv2.cvtColor(imagem_hsv.astype(np.uint8), cv2.COLOR_HSV2RGB)
    util.plot_results(a, imagem_rgb)

if __name__ == "__main__":
    op = 0
    lista = util.open_folder()
    while op != 3:
        print("\n[1] Listar imagens")
        print("[2] Inverter matiz")
        print("[3] Encerrar programa")
        op = int(input("\nSelecione uma opção: "))
        if op == 1:
            for imagem in lista:
                print(imagem)
        elif op == 2:
            name = str(input("Digite o nome da imagem: "))
            if name in lista:
                m = int(input("Digite um valor para m: "))
                x = int(input("Digite um valor para x: "))
                imagem = cv2.imread(util.convert_path(name))
                altera_matiz(imagem, m, x)
            else:
                print("Imagem inválida!")
                continue
        elif op == 3:
            print("Encerrando")
            continue
        else: 
            print("Opção inválida!")
import os
import matplotlib.pyplot as plt
import cv2

diretorio_atual = os.path.dirname(__file__)
caminho_da_pasta = os.path.join(diretorio_atual, 'files')

def open_folder():
    conteudos_da_pasta = os.listdir(caminho_da_pasta)
    return conteudos_da_pasta
 
def convert_path(name):
    return os.path.join(caminho_da_pasta, name)

def plot_results(before, after):
    plt.figure(figsize=((14, 7)))
    plt.subplot(1, 2, 1)
    plt.imshow(cv2.cvtColor(before, cv2.COLOR_BGR2RGB))
    plt.title("antes", fontsize=20)
    plt.axis('off')  

    plt.subplot(1, 2, 2)
    plt.imshow(after)
    plt.title("depois", fontsize=20)
    plt.axis('off') 
    plt.show()
    if os.name == "nt":
        os.system("cls")
    else:
        os.system("clear")
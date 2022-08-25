import numpy as np
from PIL import Image
import pandas as pd
import os

def stampaImmagine(filename):
    im_1 = Image.open(filename)
    ar = np.array(im_1)
    print(ar)

#accedo ad ogni immagine nella cartella qualitative_datasets e le stampo in forma matriciale
def ottieniImmagini(filename):
    #apro la cartella del dataset
    entries = os.listdir(filename)
    entries.pop(0)
    #apro ogni sottocartella
    for cartella in entries:
        lista_cartella = os.listdir(filename + '/'+ cartella)
        lista_cartella.pop(0)
        #lista_cartella è la lista di sottocartelle all'interno di "cartella"
        if(lista_cartella[0]=='input'):
            continue
        else:
            lista_immagini = os.listdir(filename + '/' + cartella + '/' + lista_cartella[1])
            for immagine in lista_immagini:
                stampaImmagine(filename + '/' + cartella + '/' + lista_cartella[1] + '/' + immagine)


ottieniImmagini('C:/Users/Gizam/OneDrive/Desktop/DeepVideoDeblurring_Dataset/qualitative_datasets')


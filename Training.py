import numpy as np
from PIL import Image
import pandas as pd
import os

#dim immagini 720x1280x3
x = []
y = []

def appendImmagine(filename, x_train):
    im_1 = Image.open(filename)
    ar = np.array(im_1)
    x_train = np.append(x_train,ar)
    return x_train
    

#accedo ad ogni immagine nella cartella qualitative_datasets e le stampo in forma matriciale
def ottieniImmagini(filename, x_train):
    #apro la cartella del dataset
    entries = os.listdir(filename)
    entries.pop(0)
    #apro ogni sottocartella
    print("LOADING DATASET:")
    for cartella in entries:
        print(cartella)
        lista_cartella = os.listdir(filename + '/'+ cartella)
        lista_cartella.pop(0)
        #lista_cartella è la lista di sottocartelle all'interno di "cartella"
        if(lista_cartella[0]=='input'):
            continue
        else:
            lista_immagini = os.listdir(filename + '/' + cartella + '/' + lista_cartella[1])
            for immagine in lista_immagini:
                if(immagine==".DS_Store"): 
                    continue
                x_train = appendImmagine(filename + '/' + cartella + '/' + lista_cartella[1] + '/' + immagine, x_train)
    return x_train

def OttieniImmaginiRidotto(filename,x_train, y):
    #apro la cartella del dataset
    entries = os.listdir(filename)
    entries.pop(0)
    #apro ogni sottocartella
    print("LOADING DATASET:")
    for cartella in entries:
        if(cartella=="input"):
            lista_immagini = os.listdir(filename + '/' + cartella)
            for immagine in lista_immagini:
                if(immagine==".DS_Store"): 
                    continue
                x_train = appendImmagine(filename + '/' + cartella + '/' + lista_cartella[1] + '/' + immagine, x_train)
        else:
            lista_immagini = os.listdir(filename + '/' + cartella)
            for immagine in lista_immagini:
                if(immagine==".DS_Store"): 
                    continue
                y = appendImmagine(filename + '/' + cartella + '/' + lista_cartella[1] + '/' + immagine, y)
    return x_train, y

#x_train = ottieniImmagini('C:/Users/Gizam/OneDrive/Desktop/DeepVideoDeblurring_Dataset/qualitative_datasets', x_train)
x,y = ottieniImmaginiRidotto()
x_train2 = np.array(x_train)

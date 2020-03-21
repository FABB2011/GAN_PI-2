import librosa
import pandas as pd
from sklearn.cluster import KMeans
import numpy as np
import sys
import json
import os
import random
import classes
import images
np.set_printoptions(threshold=np.inf)


def fourier(data, nb_images, div):
    tab = []
    for i in range(nb_images):
        audio = abs(np.fft.rfft(data[div * i:div * (i + 1)]))
        tab.append(audio)
    return tab


def ema(data, nb_images, period):
    tab_inv = []
    for i in range(len(data[0])):
        tab_eq = []
        for j in range(nb_images):
            tab_eq.append(data[j][i])
        tab_inv.append(tab_eq)

    for i in range(len(tab_inv)):
        tab_inv[i] = pd.DataFrame(tab_inv[i])
        tab_inv[i] = tab_inv[i].ewm(span=period).mean()
        tab_inv[i] = tab_inv[i][0]

    data_fin = []
    for i in range(nb_images):
        tab_t = []
        for j in range(len(tab_inv)):
            tab_t.append(tab_inv[j][i])
        data_fin.append(tab_t)
    return data_fin


def scale_rand(data, nb_images):

    for i in range(nb_images):
        data[i] = data[i][50:178]
        data[i] = 2 * ((data[i] - min(data[i])) / (max(data[i]) - min(data[i]))) - 1
        random.Random(5).shuffle(data[i])
    return data

def create_classes(data, clusters):

    for i in range(len(data)):
        data[i] = data[i].tolist()
        classe = eval('classes.classes' + str(clusters[i]))
        truncation = eval('classes.truncation' + str(clusters[i]))
        data[i].append(classe)
        data[i].append(truncation)
    return data

def delete_data(data):
    for i in range(len(data)):
        data1[i].append(False)

    for i in range(len(data) - 1):
        if  data[i][len(data[i]) - 2] != data[i + 1][len(data[i + 1]) - 2]:

            data[i][len(data[i]) - 1] = True


    return data


data1, sampling_rate1 = librosa.load('/home/fabrice/PycharmProjects/GANMovie/audioFiles/subzero45.wav')
duration1 = len(data1)/sampling_rate1
frame_rate1 = 24
nb_images1 = int(duration1*frame_rate1)
div1 = sampling_rate1//frame_rate1
div1 = int(div1)

data1 = fourier(data1, nb_images1, div1)

data1 = ema(data1, nb_images1, 25)

clusters = KMeans(n_clusters=3, random_state=0).fit(data1)

print(clusters.labels_)

data1 = scale_rand(data1, nb_images1)

data2 = create_classes(data1, clusters.labels_)

data3 = delete_data(data2)

'''
for i in range(len(data3)):
    print(data3[i][len(data3[i]) - 2:len(data3[i])])
'''
images.main(data3)






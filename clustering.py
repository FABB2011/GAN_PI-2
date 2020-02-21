import librosa
import pandas as pd
from sklearn.cluster import KMeans
import numpy as np
import sys
import json
import os
import random
import classes

np.set_printoptions(threshold=sys.maxsize)
dir_path = os.path.dirname(os.path.realpath(__file__))


def new_json(my_list, file_number, cluster):

    values = {"truncation": eval('classes.truncation' + str(cluster)),
            "latent": my_list,
            "classes": eval('classes.classes' + str(cluster))}
    with open(dir_path+'/jsonStore/' + str(file_number) + '.json','w') as outfile:
        json.dump(values, outfile)


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


def create_files(data, nb_images):

    for i in range(nb_images):
        with open('/home/fabrice/PycharmProjects/GANV2/dataFiles/' + str(i) + '.txt', 'w') as f:
            for item in data[i]: f.write("%s\n" % item)
        data[i] = data[i].tolist()
        new_json(data[i], i, clusters.labels_[i])


data1, sampling_rate1 = librosa.load('/home/fabrice/PycharmProjects/GANV2/audioFiles/subzero.wav')
duration1 = len(data1)/sampling_rate1
frame_rate1 = 24
nb_images1 = int(duration1*frame_rate1)
div1 = sampling_rate1//frame_rate1
div1 = int(div1)

data1 = fourier(data1, nb_images1, div1)

data1 = ema(data1, nb_images1, 50)

clusters = KMeans(n_clusters=17, random_state=0).fit(data1)
print(clusters.labels_)

data1 = scale_rand(data1, nb_images1)

create_files(data1, nb_images1)




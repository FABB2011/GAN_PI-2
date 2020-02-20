import librosa
import matplotlib.pyplot as plt
import pandas as pd
from sklearn.cluster import KMeans
import numpy as np
import sys
import json
import classes
import os
import random
from scipy.io import wavfile

np.set_printoptions(threshold=sys.maxsize)
dir_path = os.path.dirname(os.path.realpath(__file__))

def new_json(my_list, file_number, cluster):

    data = {"truncation": eval('classes.truncation' + str(cluster)),
            "latent": my_list,
            "classes": eval('classes.classes' + str(cluster))}
    with open(dir_path+'/jsonStore/' + str(file_number) + '.json','w') as outfile:
        json.dump(data, outfile)


data, sampling_rate = librosa.load('/home/fabrice/PycharmProjects/GANV2/audioFiles/subzero.wav')
duration = len(data)/sampling_rate
frame_rate = 24
nb_images = int(duration*frame_rate)
div = sampling_rate//frame_rate
div = int(div)

tab = []
for i in range(nb_images):
    audio = abs(np.fft.rfft(data[div * i:div * (i + 1)]))
    tab.append(audio)

tabInv = []
for i in range(len(tab[0])):
    tabEq = []
    for j in range(nb_images):
        tabEq.append(tab[j][i])
    tabInv.append(tabEq)

for i in range(len(tabInv)):
    tabInv[i] = pd.DataFrame(tabInv[i])
    tabInv[i] = tabInv[i].ewm(span=20).mean()
    tabInv[i] = tabInv[i][0]

dataF = []
for i in range(nb_images):
    tabT = []
    for j in range(len(tabInv)):
        tabT.append(tabInv[j][i])
    dataF.append(tabT)

clusters = KMeans(n_clusters=20, random_state=0).fit(dataF)
print(clusters.labels_)

for i in range(nb_images):
    data = dataF[i][100:228]
    data = 2 * ((data - min(data)) / (max(data) - min(data))) - 1
    random.Random(5).shuffle(data)

    with open('/home/fabrice/PycharmProjects/GANV2/dataFiles/' + str(i) + '.txt', 'w') as f:
        for item in data: f.write("%s\n" % item)
    #data = data.tolist()
    #new_json(data, i, clusters.labels_[i])


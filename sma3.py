import numpy as np
from scipy.io import wavfile
import json
import math
import os
import pandas as pd
import matplotlib.pyplot as plt
import random

dir_path = os.path.dirname(os.path.realpath(__file__))


def normalize(array):
    for i in range(len(array)):
        mean = np.mean(array)
        std = np.std(array)
        array[i] = (array[i] - mean) / std
    return array


def new_json(my_list, file_name):
    data = {"truncation": 0.99999, 'latent': my_list,
            "classes": [[2, 0.6046175963028713], [26, -0.22644737976315157], [41, -0.07887031825155294],
                        [113, 0.06189174711325805], [160, 0.040110608260472636], [166, 0.04988011508575531],
                        [238, 0.03277059051391763], [239, 0.020667736081565045], [253, 0.04517390375562291],
                        [265, 0.07049985374599582], [271, 0.135419381510952], [287, 0.3110135519864581],
                        [337, 0.030080828347213227], [371, 0.11407948233226375], [422, 0.053773823583785615],
                        [426, 0.07463719117854961], [432, 0.04987286048959339], [473, 0.06416993579972702],
                        [508, 0.05096203813826808], [543, 0.02070870602156376], [549, -0.6970882499543491],
                        [552, 0.10780430245377809], [561, 0.039351262919123], [564, 0.16209645906083442],
                        [594, 0.4552120276136199], [602, 0.05167892802623459], [613, 0.03686333189246887],
                        [631, 0.04853041907061059], [655, 0.006147148597422881], [674, -0.005119146062385997],
                        [679, 0.19744191952051013], [688, 0.04907715074750399], [713, -0.07352056544963029],
                        [717, 0.008374267373214716], [718, -0.017434679648659822], [764, 0.15719877414432215],
                        [794, 0.3587674047437466], [855, 0.034096414580130116], [900, 0.07351533208271513],
                        [913, 0.06651369207607799], [925, 0.02698520048388676], [940, 0.010294507912424294],
                        [978, -0.0026688849324594636], [992, 0.029283186042910442]]
            }

    with open(dir_path+'/jsonStore/' + str(file_name) + '.json','w') as outfile:
        json.dump(data, outfile)


def sma(data, period):
    j = next(i for i, x in enumerate(data) if x is not None)
    our_range = range(len(data))[j + period - 1:]
    empty_list = [None] * (j + period - 1)
    sub_result = [np.mean(data[i - period + 1: i + 1]) for i in our_range]
    return np.array(empty_list + sub_result)


rate, audio = wavfile.read('/home/fabrice/PycharmProjects/GANV2/audioFiles/25.wav')
audio = np.mean(audio, axis=1)
#audio = audio[300000:400000]
duration = len(audio)/rate
frame_rate = 30
images = int(duration*frame_rate)
div = rate//frame_rate


tab = []
for i in range(images):
    data = abs(np.fft.rfft(audio[div * i:div * (i+1)]))
    data = data.tolist()
    tab.append(data)


tabInv = []
for i in range(len(tab[0])):
    tabEq = []
    for j in range(images):
        tabEq.append(tab[j][i])
    tabInv.append(tabEq)

for i in range(len(tabInv)):
    tabInv[i] = tabInv[i]
    #tabInv[i] = sma(tabInv[i], 10)
    tabInv[i] = pd.DataFrame(tabInv[i])
    tabInv[i] = tabInv[i].ewm(span=80).mean()
    tabInv[i] = tabInv[i][0]

dataF = []
for i in range(images):
    tabT = []
    for j in range(len(tabInv)):
        tabT.append(tabInv[j][i])
    dataF.append(tabT)

for i in range(images):
    data = dataF[i][100:228]
    data = 2 * ((data - min(data)) / (max(data) - min(data))) - 1
    random.Random(5).shuffle(data)

    with open('/home/fabrice/PycharmProjects/GANV2/dataFiles/' + str(i) + '.txt', 'w') as f:
        for item in data: f.write("%s\n" % item)
    data = data.tolist()
    new_json(data, str(i))






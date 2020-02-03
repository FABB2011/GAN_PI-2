import numpy as np
from scipy.io import wavfile
import json
import math
import os

dir_path = os.path.dirname(os.path.realpath(__file__))

def new_json(my_list, file_name):
    data = {'truncation': float(1), 'latent': my_list,
            'classes': [[188, 0.2696612715283029], [338, 0.9262914142148885], [385, 0.13095440634023092], [483, 0.20723007243371555]]}

    with open(dir_path+'/jsonStore/' + str(file_name) + '.json','w') as outfile:
        json.dump(data, outfile)


rate, audio = wavfile.read('/home/fabrice/PycharmProjects/GANV2/audioFiles/sine.wav')
# audio = np.mean(audio, axis=1)
duration = len(audio)/rate

frame_rate = 60
images = int(duration*frame_rate)

div = rate//frame_rate


tab = []
moy = []

for i in range(images):
    data = abs(np.fft.rfft(audio[div * i:div * (i+1)]))
    data = data.tolist()
    tab.append(data)



for i in range(len(tab[0])):
    somme = 0;
    for j in range(images):
        somme = somme + tab[j][i]
    somme = somme//images
    moy.append(somme)



for i in range(len(tab)):
    tab[i] = np.log10(tab[i])
    tab[i] = 2 * ((tab[i] - min(tab[i])) / (max(tab[i]) - min(tab[i]))) - 1

moy = np.log10(moy)
moy = 2 * ((moy - min(moy)) / (max(moy) - min(moy))) - 1


print(len(tab))


for i in range(images):
    for j in range(len(tab[0])):
        if tab[i][j] > moy[j]:
            tab[i][j] = moy[j] + 0.01
        else:
            tab[i][j] = moy[j] - 0.01

    tab[i] = tab[i].tolist()

    with open('/home/fabrice/PycharmProjects/GANV2/dataFiles/' + str(i) + '.txt', 'w') as f:
        for item in tab[i]: f.write("%s\n" % item)
    #new_json(tab, str(i))



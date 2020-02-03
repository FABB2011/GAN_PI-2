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


#rate, audio = wavfile.read('/home/fabrice/PycharmProjects/GANV2/audioFiles/House Fire Alarm-SoundBible.com-1609046789.wav')
rate, audio = wavfile.read(dir_path+'/audioFiles/sine.wav')
duration = len(audio)/rate
# audio = np.mean(audio, axis=1)
frame_rate = 60
images = int(duration*frame_rate)
div = rate//frame_rate

data = abs(np.fft.rfft(audio[div * 0:div * (0+1)]))
w, h = len(data), 669
tab = [[0 for x in range(w)] for y in range(h)]
moy = [0]*w

for i in range(0, images):
    data = abs(np.fft.rfft(audio[div * i:div * (i+1)]))
    data = data.tolist()
    for compteur in range(w):
        tab[compteur][i] = data[compteur]

for k in range(w):
    for l in range(0, images):
        moy[k] = moy[k] + tab[k][l]
    moy[k] = moy[k]/669

data = np.log10(data)
data = 2 * ((data - min(data)) / (max(data) - min(data))) - 1
dat = [0]*w
for i in range(len(data)):
    dat[i] = data[i]

for i in range(images):
    for compteur in range(w):
        tab[compteur][i] = data[compteur]
        if dat[compteur] > moy[compteur]:
            dat[compteur] = dat[compteur] + 0.01
        else:
            dat[compteur] = dat[compteur] - 0.01

    with open(dir_path+'/dataFiles/' + str(i) + '.txt', 'w') as f:
        for item in dat: f.write("%s\n" % item)
    new_json(dat, str(i))

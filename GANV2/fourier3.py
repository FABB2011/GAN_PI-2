import numpy as np
from scipy.io import wavfile
import json
import math


def new_json(my_list, file_name):
    data = {'truncation': float(1), 'latent': my_list,
            'classes': [[188, 0.2696612715283029], [338, 0.9262914142148885], [385, 0.13095440634023092], [483, 0.20723007243371555]]}

    with open('/home/fabrice/PycharmProjects/GANV2/jsonStore/' + str(file_name) + '.json','w') as outfile:
        json.dump(data, outfile)


#rate, audio = wavfile.read('/home/fabrice/PycharmProjects/GANV2/audioFiles/House Fire Alarm-SoundBible.com-1609046789.wav')
rate, audio = wavfile.read('/audioFiles/House Fire Alarm-SoundBible.com-1609046789.wav')
duration = len(audio)/rate
audio = np.mean(audio, axis=1)
frame_rate = 60
images = int(duration*frame_rate)
div = rate//frame_rate

for i in range(0, images):
    data = abs(np.fft.rfft(audio[div * i:div * (i+1)]))
    data = data[0:128]
    data = np.log10(data)
    data = 2 * ((data - min(data)) / (max(data) - min(data))) - 1
    data = data.tolist()
    with open('/home/fabrice/PycharmProjects/GANV2/dataFiles/' + str(i) + '.txt', 'w') as f:
        for item in data: f.write("%s\n" % item)
    new_json(data, str(i))




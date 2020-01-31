import numpy as np
import matplotlib.pyplot as plt
from scipy.io import wavfile
import json


def new_json(my_list, file_name):
    data = {'truncation': float(1), 'latent': my_list,
            'classes': [[188, 0.2696612715283029], [338, 0.9262914142148885], [385, 0.13095440634023092], [483, 0.20723007243371555]]}

    with open('/home/fabrice/PycharmProjects/DTE/gan-movie-maker-master/jsonStore/' + str(file_name) + '.json','w') as outfile:
        json.dump(data, outfile)


def moy_tab(n, tab):
    averaged_array = []
    for i in range(0, len(tab), n):
        slice_from_index = i
        slice_to_index = slice_from_index + n
        averaged_array.append(np.mean(tab[slice_from_index:slice_to_index]))
    return averaged_array[0:128]


rate, audio = wavfile.read('/home/fabrice/PycharmProjects/DTE/gan-movie-maker-master/audioFiles/House Fire Alarm-SoundBible.com-1609046789.wav')
audio = np.mean(audio, axis=1)

#19381
for i in range(0, 660):
    div = 735
    data = abs(np.fft.rfft(audio[div * i:div * (i+1)]))
    #data = data[0:128]
    data = 2 * ((data - min(data)) / (max(data) - min(data))) - 0.5
    data = data[0:128]
    #data = 2 * ((data - min(data)) / (max(data) - min(data))) - 1
    data = data.tolist()
    with open('/home/fabrice/PycharmProjects/DTE/gan-movie-maker-master/dataFiles/' + str(i) + '.txt', 'w') as f:
        for item in data: f.write("%s\n" % item)
    new_json(data, str(i))
    a = plt.subplot()
    a.set_xscale('log')
    a.set_xlabel('frequency [Hz]')
    a.set_ylabel('|amplitude|')
    #plt.plot(data)
#plt.show()



'''
audio1 = []
for i in range(0,19381):
    audio1.append(audio[i:i+128])
    i = i + (len(audio)//19381)
'''


'''
for i in range(1000,1006):
    div = rate // mod
    data = abs(np.fft.rfft(audio[div * i:div * (i+1)]))
    data = data.tolist()
    with open('/home/fabrice/PycharmProjects/GANHAR/gan-movie-maker-master/dataFiles/' + str(i) + '.txt', 'w') as f:
        for item in data:
            f.write("%s\n" % item)
    new_json(data, str(i))
    a = plt.subplot()
    a.set_xscale('log')
    a.set_xlabel('frequency [Hz]')
    a.set_ylabel('|amplitude|')
    plt.plot(data)
plt.show()

for i in range(3000,3006):
    div = rate // mod
    data = abs(np.fft.rfft(audio[div * i:div * (i+1)]))
    data = data.tolist()
    with open('/home/fabrice/PycharmProjects/GANHAR/gan-movie-maker-master/dataFiles/' + str(i) + '.txt', 'w') as f:
        for item in data:
            f.write("%s\n" % item)
    new_json(data, str(i))
    a = plt.subplot()
    a.set_xscale('log')
    a.set_xlabel('frequency [Hz]')
    a.set_ylabel('|amplitude|')
    plt.plot(data)
plt.show()

'''



'''
rate, data = wavfile.read('/home/fabrice/PycharmProjects/GANHAR/gan-movie-maker-master/audioFiles/Poney Part 1.wav')
data = np.mean(data, axis=1)
#print(len(data))
data = abs(np.fft.rfft(data))
max = max(data)
print(max)'''


'''
rate, da = wavfile.read('/home/fabrice/PycharmProjects/GANHAR/gan-movie-maker-master/audioFiles/Poney Part 1.wav')
da = np.mean(da, axis=1)
div = rate//30
da = abs(np.fft.rfft(da[div*501:div*502]))
a = plt.subplot()
a.set_xscale('log')
a.set_xlabel('frequency [Hz]')
a.set_ylabel('|amplitude|')
plt.plot(da)
plt.show()

rate, da = wavfile.read('/home/fabrice/PycharmProjects/GANHAR/gan-movie-maker-master/audioFiles/Poney Part 1.wav')
da = np.mean(da, axis=1)
div = rate//30
da = abs(np.fft.rfft(da[div*7000:div*7001]))
b = plt.subplot()
b.set_xscale('log')
b.set_xlabel('frequency [Hz]')
b.set_ylabel('|amplitude|')
plt.plot(da)


rate, da = wavfile.read('/home/fabrice/PycharmProjects/GANHAR/gan-movie-maker-master/audioFiles/Poney Part 1.wav')
da = np.mean(da, axis=1)
div = rate//30
da = abs(np.fft.rfft(da[div*7001:div*7002]))
c = plt.subplot()
c.set_xscale('log')
c.set_xlabel('frequency [Hz]')
c.set_ylabel('|amplitude|')
plt.plot(da)

rate, da = wavfile.read('/home/fabrice/PycharmProjects/GANHAR/gan-movie-maker-master/audioFiles/Poney Part 1.wav')
da = np.mean(da, axis=1)
div = rate//30
da = abs(np.fft.rfft(da[div*7002:div*7003]))
c = plt.subplot()
c.set_xscale('log')
c.set_xlabel('frequency [Hz]')
c.set_ylabel('|amplitude|')
plt.plot(da)
plt.show()

'''


'''
lf = abs(np.fft.rfft(da))
b = plt.subplot()
b.set_xscale('log')
b.set_xlabel('frequency [Hz]')
b.set_ylabel('|amplitude|')
plt.plot(lf)
plt.show()

lf = abs(np.fft.rfft(da[0:len(da)]))
b = plt.subplot()
b.set_xscale('log')
b.set_xlabel('frequency [Hz]')
b.set_ylabel('|amplitude|')
plt.plot(lf)
plt.show()
'''

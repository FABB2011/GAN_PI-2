import librosa
import matplotlib.pyplot as plt
import pandas as pd

data, sampling_rate = librosa.load('/home/fabrice/PycharmProjects/GANV2/audioFiles/25.wav')

duration = len(data)/sampling_rate
frame_rate = 30
nb_images = int(duration*frame_rate)
div = sampling_rate//frame_rate
print(div)

data1 = data[45*735:46*735]

plt.plot(data1)
plt.show()

data1 = pd.DataFrame(data1)
data1 = data1.ewm(span=80).mean()

plt.plot(data1)
plt.show()

data2 = data[46*735:47*735]

plt.plot(data2)
plt.show()

data2 = pd.DataFrame(data2)
data2 = data2.ewm(span=80).mean()

plt.plot(data2)
plt.show()
import librosa
import pandas as pd
from sklearn.cluster import KMeans
import numpy as np
import random
import classes
import create_images
np.set_printoptions(threshold=np.inf)


# apply the Fourier transform on each part of the audio depending on the chosen frame rate
def fourier(data, nb_images, div):
    tab = []
    for i in range(nb_images):
        audio = abs(np.fft.rfft(data[div * i:div * (i + 1)]))
        tab.append(audio)
    return tab


# compute the exponential moving average on each part of the data
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


# scale the data between -1 and +1
def scale_rand(data, nb_images, shuffle):
    for i in range(nb_images):
        data[i] = data[i][50:178]
        for j in range(len(data[i])):
            if data[i][j] > 1:
                data[i][j] = 1.0
        data[i] = 2 * ((data[i] - min(data[i])) / (max(data[i]) - min(data[i]))) - 1
        # the data are shuffled
        random.Random(shuffle).shuffle(data[i])
    return data


# give to each frame an image type (a class) depending on their cluster
def create_classes(data, clusters):
    for i in range(len(data)):
        data[i] = data[i].tolist()
        classe = eval('classes.classes' + str(clusters[i]))
        truncation = eval('classes.truncation' + str(clusters[i]))
        data[i].append(classe)
        data[i].append(truncation)
    return data


# mark a frame as true if the following frame class is different
def mark_data(data):
    for i in range(len(data)):
        data[i].append(False)
    for i in range(len(data) - 1):
        if data[i][len(data[i]) - 2] != data[i + 1][len(data[i + 1]) - 2]:
            data[i][len(data[i]) - 1] = True
    return data


def main(audio_path, frame_rate, skip, image_number, ema_period, shuffle):

    # load the song
    print("Audio reading...\n")
    data1, sampling_rate1 = librosa.load(audio_path)

    # compute the duration of the song
    duration1 = len(data1) / sampling_rate1

    # compute the total number of image that will be created depending on the duration and the frame rate
    nb_images1 = int(duration1 * frame_rate)

    # div1 is the number of the length of a tab representing one frame
    div1 = sampling_rate1 // frame_rate
    div1 = int(div1)

    # Fourier transformation
    print("Fourier transform calculation...\n")
    data1 = fourier(data1, nb_images1, div1)

    # exponential moving average
    print("Exponential moving average calculation...\n")
    data1 = ema(data1, nb_images1, ema_period)

    # clustering
    print("Cluster computation...\n")
    clusters = KMeans(n_clusters=image_number, random_state=0).fit(data1)
    #print(clusters.labels_)

    # scaling of the data
    print("Data scaling and shuffling...\n")
    data1 = scale_rand(data1, nb_images1, shuffle)

    # assignation of classes
    print("Class allocation...\n")
    data2 = create_classes(data1, clusters.labels_)

    # mark the data that will change of class
    print("Transition identification...\n")
    data3 = mark_data(data2)

    # we call the function that create an image from each part of the data
    print("Images creation...\n")
    create_images.main(data3, skip, nb_images1)





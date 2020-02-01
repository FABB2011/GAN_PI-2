import sys
import numpy as np
import biggan
import image_utils
import os
import pandas as pd
import cv2
import glob


def main(arguments=None):

    print('Loading bigGAN...')
    gan = biggan.BigGAN()

    #for root, _, files in os.walk('/home/fabrice/PycharmProjects/GANV2/jsonStore'):
    for root, _, files in os.walk('/jsonStore'):
        len(files)

    compteur = len(files)

    for i in range(compteur):
        #data = pd.read_json('/home/fabrice/PycharmProjects/GANV2/jsonStore/' + str(i) + '.json', lines=True)
        data = pd.read_json('/jsonStore/' + str(i) + '.json', lines=True)

        z_seq = data['latent']
        z_seq = z_seq.tolist()
        z_seq = np.array(z_seq)

        label_seq = np.zeros(1000)
        j = 0
        for c in range(len(data['classes'][0])):
            label_seq[data['classes'][0][j][0]] = data['classes'][0][j][1]
            j = j + 1

        label_seq.shape = (1, 1000)

        #saver = image_utils.ImageSaver(output_dir="/home/fabrice/PycharmProjects/GANV2/images", prefix=i)
        saver = image_utils.ImageSaver(output_dir="/images", prefix=i)
        gan.sample(z_seq, label_seq, save_callback=saver.save)

    print('Done.')

    #workdir = "/home/fabrice/PycharmProjects/GANV2/images"
    workdir = "/images"
    outputVideo = "video.mp4"
    if not os.path.exists(workdir):
        os.makedirs(workdir)

    img_array = []

    size = (None)

    for filename in glob.glob(workdir + '/*.png'):
        img = cv2.imread(filename)
        height, width, layers = img.shape
        size = (width, height)
        img_array.append(img)

    out = cv2.VideoWriter(outputVideo, cv2.VideoWriter_fourcc(*'DIVX'), 60, size)

    for i in range(len(img_array)):
        out.write(img_array[i])
    out.release()


if __name__ == '__main__':
    sys.exit(main())



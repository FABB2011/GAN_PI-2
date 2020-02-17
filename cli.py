import sys
import numpy as np
import biggan
import image_utils
import os
import pandas as pd
import cv2
import glob

dir_path = os.path.dirname(os.path.realpath(__file__))

def main(arguments=None):

    print('Loading bigGAN...')
    gan = biggan.BigGAN()

    for root, _, files in os.walk(dir_path+'/jsonStore'):
        len(files)

    compteur = len(files)

    for i in range(compteur):
        data = pd.read_json(dir_path+'/jsonStore/' + str(i) + '.json', lines=True)
        #data = pd.read_json('/home/fabrice/PycharmProjects/GANV2/jsonStore/99.json', lines=True)

        truncationV = data['truncation']

        z_seq = data['latent']
        z_seq = z_seq.tolist()
        z_seq = np.array(z_seq)

        label_seq = np.zeros(1000)
        j = 0
        for c in range(len(data['classes'][0])):
            label_seq[data['classes'][0][j][0]] = data['classes'][0][j][1]
            j = j + 1

        label_seq.shape = (1, 1000)

        saver = image_utils.ImageSaver(output_dir=dir_path+"/images", prefix=i)
        gan.sample(z_seq, label_seq, truncation=truncationV, save_callback=saver.save)


if __name__ == '__main__':
    sys.exit(main())



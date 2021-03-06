import sys
import numpy as np
import biggan
import image_utils
import os
import pandas as pd
import glob


def main(arguments=None):

    gan = biggan.BigGAN()

    for root, _, files in os.walk('/home/fabrice/PycharmProjects/GANMovie/jsonStore'):
        len(files)

    for i in range(len(files)):
        data = pd.read_json('/home/fabrice/PycharmProjects/GANMovie/jsonStore/' + str(i) + '.json', lines=True)

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

        #print(label_seq)

        saver = image_utils.ImageSaver(output_dir="/home/fabrice/PycharmProjects/GANMovie/images", prefix=i)
        gan.sample(z_seq, label_seq, truncation=truncationV, save_callback=saver.save)


if __name__ == '__main__':
    sys.exit(main())



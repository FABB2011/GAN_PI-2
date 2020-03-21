import sys
import numpy as np
import biggan
import image_utils


def main(tab):

    gan = biggan.BigGAN()

    for i in range(len(tab)):

        if tab[i][len(tab[i]) - 1:len(tab[i])] == [False] or tab[i][len(tab[i]) - 1:len(tab[i])] == [True]:

            tab[i] = tab[i][:len(tab[i]) - 1]

            # print(tab[i])

            latent_space = tab[i][0:128]
            latent_space = np.array(latent_space)
            latent_space.shape = (1, 128)

            classes = tab[i][128:len(tab[0]) - 1]
            label_seq = np.zeros(1000)
            for j in range(len(classes[0])):
                label_seq[classes[0][j][0]] = classes[0][j][1]
            label_seq.shape = (1, 1000)

            truncation = tab[i][len(tab[i]) - 1]

            # saver = image_utils.ImageSaver(output_dir="/home/fabrice/PycharmProjects/GANMovie/images", prefix=i)
            saver = image_utils.ImageSaver(output_dir="images", prefix=i)
            gan.sample(latent_space, label_seq, truncation=truncation, save_callback=saver.save)

        else:
            print('NO')



if __name__ == '__main__':
    sys.exit(main())
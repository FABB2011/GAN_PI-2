import sys
import numpy as np
import biggan
import image_utils
import json
import transition


# create a json file representing the data of one frame
def new_json(data, num):
    classes = data[128:len(data) - 1]
    classes = classes[0]
    values = {"truncation": data[len(data) - 1],
            "latent": data[0:128],
            "classes": classes}
    with open('/home/fabrice/PycharmProjects/GANMovie/jsonStore/' + str(num) + '.json','w') as outfile:
        json.dump(values, outfile)


def main(tab, skip, nb_image):

    # load the gan function
    gan = biggan.BigGAN()

    i = 0
    while i < len(tab):

        if tab[i][len(tab[i]) - 1:len(tab[i])] == [False]:

            data = tab[i][:len(tab[i]) - 1]

            latent_space = data[0:128]
            latent_space = np.array(latent_space)
            latent_space.shape = (1, 128)

            classes = data[128:len(data) - 1]
            label_seq = np.zeros(1000)
            for j in range(len(classes[0])):
                label_seq[classes[0][j][0]] = classes[0][j][1]
            label_seq.shape = (1, 1000)

            truncation = data[len(data) - 1]

            saver = image_utils.ImageSaver(output_dir="/home/fabrice/PycharmProjects/GANMovie/images", prefix=i)
            gan.sample(latent_space, label_seq, truncation=truncation, save_callback=saver.save)
            i = i + 1

        else:
            tab0 = tab[i][:len(tab[i]) - 1]
            tab1 = tab[i + skip][:len(tab[i + skip]) - 1]
            new_json(tab0, 0)
            new_json(tab1, 1)
            transition.main(i, gan, skip)
            i = i + skip

        print(str(i), ' sur ', str(nb_image))


def main2(tab, skip, nb_image):

    # load the gan function
    gan = biggan.BigGAN()

    i = 0
    while i < len(tab):
        tab0 = tab[i][:len(tab[i]) - 1]
        tab1 = tab[i + 1][:len(tab[i + skip]) - 1]

        new_json(tab0, 0)
        new_json(tab1, 1)

        transition.main(i, gan, skip)
        step = skip

        print(str(i), ' sur ', str(nb_image))

        i = i + step










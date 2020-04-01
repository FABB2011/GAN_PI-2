import numpy as np
import biggan
import image_utils
import json
import create_transitions
import random
import os

dir_path = os.path.dirname(os.path.realpath(__file__))

# create a json file representing the data of one frame
def new_json(data, num):
    classes = data[128:len(data) - 1]
    classes = classes[0]
    values = {"truncation": data[len(data) - 1],
            "latent": data[0:128],
            "classes": classes}
    with open(dir_path+'/jsonStore/' + str(num) + '.json','w') as outfile:
        json.dump(values, outfile)


# shuffle the data in order to obtain different images
def chang_image(tab):
    const = random.randint(1, 1000)
    for i in range(len(tab)):
        for j in range(i, len(tab)):
            if tab[i][len(tab[i]) - 1:len(tab[i])] == [False]:
                temp = tab[i][0:128]
                random.Random(const).shuffle(temp)
                for k in range(len(temp)):
                    tab[i][k] = temp[k]
        print('shuffle: ', str(i), ' on ', str(len(tab)))


def main(tab, skip, nb_image):
    # we can shuffle the data if we want with this function
    #chang_image(tab)

    # load the GAN function
    gan = biggan.BigGAN()

    i = 0
    while i < len(tab):

        # if there is no changes in the data classes, we create the image
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

            saver = image_utils.ImageSaver(output_dir=dir_path+"/images", prefix=i)
            gan.sample(latent_space, label_seq, truncation=truncation, save_callback=saver.save)
            i = i + 1

        # if there is changes in the data classes, we create transition images between this image and the image + skip
        else:
            tab0 = tab[i][:len(tab[i]) - 1]
            tab1 = tab[i + skip][:len(tab[i + skip]) - 1]

            new_json(tab0, 0)
            new_json(tab1, 1)

            create_transitions.main(i, gan, skip)
            i = i + skip

        print('images: ', str(i), ' on ', str(nb_image))


def main2(tab, skip, nb_image):

    # load the GAN function
    gan = biggan.BigGAN()

    i = 0
    while i < len(tab):
        tab0 = tab[i][:len(tab[i]) - 1]
        tab1 = tab[i + 1][:len(tab[i + skip]) - 1]

        new_json(tab0, 0)
        new_json(tab1, 1)

        create_transitions.main(i, gan, skip)
        step = skip

        print('images: ', str(i), ' on ', str(nb_image))

        i = i + step










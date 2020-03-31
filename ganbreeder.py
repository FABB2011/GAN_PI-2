import json
import numpy as np
import os


def parse_info_dict(info):
    keyframe = dict()
    keyframe['truncation'] = np.float(info['truncation'])
    keyframe['latent'] = np.asarray(info['latent'])
    classes = info['classes']
    keyframe['label'] = np.zeros(1000)
    for c in info['classes']:

        keyframe['label'][c[0]] = c[1]
    return keyframe


def get_info(key):
    key = key.replace("'", "")
    os.chdir('/home/fabrice/PycharmProjects/GANMovie/jsonStore')
    with open(key+'.json') as json_data:
        key_json = json.load(json_data)
    return parse_info_dict(key_json)


def get_info_batch(keys):
    l = list()
    x = []
    x = x + keys[0].split()
    for key in x:
        l.append(get_info(key))
    return l
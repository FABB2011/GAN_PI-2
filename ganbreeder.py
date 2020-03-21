import requests
import json
import numpy as np
import biggan
import os

def login(username, password):
    def get_sid():
        url = 'https://artbreeder.com/login'
        r = requests.get(url)
        r.raise_for_status()
        for c in r.cookies:
            if c.name == 'connect.sid': # find the right cookie
                print('Session ID: ' + str(c.value))
                return c.value

    def login_auth(sid, username, password):
        url = 'https://artbreeder.com/login'
        headers = {
                'Content-Type': 'application/json',
                }
        cookies = {
                'connect.sid': sid
                }
        payload = {
                'email': username,
                'password': password
                }
        r = requests.post(url, headers=headers, cookies=cookies, data=json.dumps(payload))
        if not r.ok:
            print('Authentication failed')
            r.raise_for_status()
        print('Authenticated')

    sid = get_sid()
    login_auth(sid, username, password)
    return sid

def parse_info_dict(info):
    keyframe = dict()
    keyframe['truncation'] = np.float(info['truncation'])
    keyframe['latent'] = np.asarray(info['latent'])
    classes = info['classes']
    keyframe['label'] = np.zeros(1000)
    for c in info['classes']:

        keyframe['label'][c[0]] = c[1]
    return keyframe

def get_info(sid, key):
    if sid == '':
        raise Exception('Cannot get info; session ID not defined. Be sure to login() first.')
    cookies = {
            'connect.sid': sid
            }

    key = key.replace("'", "")

    os.chdir('/home/fabrice/PycharmProjects/GANV2/jsonStore')

    with open(key+'.json') as json_data:
        key_json = json.load(json_data)

    return parse_info_dict(key_json)

def get_info_batch(username, password, keys):
    l = list()
    sid = "s%3Abx8-041_GrVmqCx4Gh6kH89Woji55a3M.sNXFvkoZ5cDHhfUTfjt%2Blaxrr6q2HQjLrOKXAa9Y7V4"
    x = []
    x = x + keys[0].split()
    for key in x:
        l.append(get_info(sid, key))
    return l
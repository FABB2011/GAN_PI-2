import fourier
import create_video
import add_audio
import os
import json

dir_path = os.path.dirname(os.path.realpath(__file__))
liste_sounds = os.listdir(dir_path+'/audioFiles/')
parameters = dict()
choice_sound = ""
choice_skip = ""
choice_image_number = ""
choice_ema_period = ""
parameterrs_choice = "2"
doesparamexist = False
try:
    paramjson = open(dir_path+"/parammemory.json","r")
    para = paramjson.read()
    param = json.loads(para)
    choice_sound = param["sound"]
    choice_skip = param["skip"]
    choice_image_number = param["image"]
    choice_ema_period = param["ema"]
    doesparamexist = True
    paramjson.close()
except FileNotFoundError:
    print("no previous paramters entry found")

print("Welcome to the Gan Clip Generator !\n")
print('What do you want to do :\n')
if(doesparamexist):
    print('1 Enter a new set of parameters\n2 Load and modify your previous parameters\n')
    parameterrs_choice = input('\nChoose between 1 and 2 : ')

if(parameterrs_choice == '2'):
    
    if(doesparamexist):
        print('Sound you choose previously : '+choice_sound+'\nEnter noting if you want to keep your settings.\n')

        print('Here is a list of the available sounds :\n')

        for i in range(len(liste_sounds)):
            print(liste_sounds[i])

        temp_choice_sound = input('\nChoose a sound please (.wav) : ')
        while(temp_choice_sound not in liste_sounds and choice_sound != ''):
                print('Sound not found ! ')
        temp_choice_sound = input('\nChoose a sound please (.wav) : ')
        choice_sound = temp_choice_sound

        print('\nYour last transitions images choice :'+choice_skip)
        temp_choice_skip = input('\nChoose also the number of transitions images (to make transitions more fluid) : ')
        if(temp_choice_skip != ''):
            choice_skip = temp_choice_skip
        
        print('\nYour last number of images choice : '+choice_image_number)
        temp_choice_image_number = input('\nChoose also the number of images : ')
        if(temp_choice_image_number != ''):
            choice_image_number = temp_choice_image_number

        print('\nYour last ema period : '+choice_ema_period)
        temp_choice_ema_period = input('\nChoose also the ema period : ')
        if(temp_choice_ema_period != ''):
            choice_ema_period = temp_choice_ema_period

else:
    print('Here is a list of the available sounds :\n')

    for i in range(len(liste_sounds)):
        print(liste_sounds[i])

    choice_sound = input('\nChoose a sound please (.wav) : ')

    while(choice_sound not in liste_sounds):
        print('Sound not found ! ')
        choice_sound = input('\nChoose a sound please (.wav) : ')

    choice_skip = input('\nChoose also the number of transitions images (to make transitions more fluid) : ')
    choice_image_number = input('\nChoose also the number of images : ')
    choice_ema_period = input('\nChoose also the ema_period : ')

parameters["sound"] = choice_sound
parameters["skip"] = choice_skip
parameters["image"] = choice_image_number
parameters["ema"] = choice_ema_period
try:
    paramjson = open(dir_path+"/parammemory.json","w")
    paramjson.write(json.dumps(parameters))
    paramjson.close()
except FileNotFoundError:
    print("problem saving command parameters")

if(choice_ema_period == ''):
    choice_ema_period = '0'
if(choice_skip == ''):
    choice_skip = '0'
if(choice_image_number == ''):
    choice_image_number = '0'

ema_period = int(choice_ema_period)
skip = int(choice_skip)
image_number = int(choice_image_number)

audio_path = '/home/fabrice/PycharmProjects/GAN21/audioFiles/'+str(choice_sound)
print(audio_path)
frame_rate = 20
#skip = 1
#image_number = 3
#ema_period = 5
shuffle = 1200
images_path = os.listdir(dir_path+'/images/')
video_path = './video.avi'
video_nameSS = 'video.avi'
video_name = 'video.mkv'

# create images
fourier.main(audio_path, frame_rate, skip, image_number, ema_period, shuffle)
# make a video with the created images
create_video.main(frame_rate, images_path, video_nameSS)
# add the audio to the video
add_audio.main(audio_path, video_path, video_name)

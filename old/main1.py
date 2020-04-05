import fourier
import create_video
import add_audio
import os

dir_path = os.path.dirname(os.path.realpath(__file__))
liste_sounds = os.listdir(dir_path+'/audioFiles/')

print('chemin -> ',os.getcwd())

try:
	os.mkdir('images')
	print("Directory images created")
except FileExistsError:
	print("Directory images already exists")

try:
	os.mkdir('audioFiles')
	print("Directory images created")
except FileExistsError:
	print("Directory images already exists")

print('Welcome to the Gan Clip Generator !\n')

print('Here is a list of the available sounds :\n')

for i in range(len(liste_sounds)):
    print(liste_sounds[i])

choice_sound = input('\nChoose a sound please (.wav) : ')

while(choice_sound not in liste_sounds):
    print('Sound not found ! ')
    choice_sound = input('\nChoose a sound please (.wav) : ')


choice_skip = input('\nChoose also the number of transitions images (to make transitions more fluid) : ')
skip = int(choice_skip) + 1

choice_image_number = input('\nChoose also the number of images : ')
image_number = int(choice_image_number)


choice_resolution = input('\nChoose also the resolution of the final video : ')
resolution = int(choice_resolution)


audio_path = './audioFiles/'+str(choice_sound)
print(audio_path)
frame_rate = 20
#skip = 1
#image_number = 3
ema_period = 5
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
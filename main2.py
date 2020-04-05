import fourier
import create_video
import add_audio
import os
import random

dir_path = os.path.dirname(os.path.realpath(__file__))
list_sounds = os.listdir(dir_path+'/audioFiles/')

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
print('Menu : \n')
print('1 - Create images')
print('2 - Create video')
print('3 - End program')

option = int(input('Choose the option you want but be sure you have images to make a video : '))

ema_period = 15
shuffle = random.randint(500, 1500)
print(shuffle)

while option != 3:
	if option == 1:

		print('Here is a list of the available sounds :\n')
		for i in range(len(list_sounds)):
			print(list_sounds[i])

		choice_sound = input('\nChoose a sound please : ')

		audio_path = './audioFiles/' + str(choice_sound)

		while choice_sound not in list_sounds:
			print('Sound not found ! ')
			choice_sound = input('\nChoose a sound please : ')

		frame_rate = int(input('\nChoose also the frame rate : '))

		skip = int(input('\nChoose also the number of transitions images (to make transitions more fluid) : '))

		image_number = int(input('\nChoose also the number of images : '))

		fourier.main(audio_path, frame_rate, skip, image_number, ema_period, shuffle)
		option = int(input('Choose the option you want but be sure you have images to make a video : '))

	if option == 2:

		choice_resolution = input(
			'\n(list of classic values : 240,360,480,720,1080,1440,2160)\nChoose also the resolution of the final video : \n')
		resolution = int(choice_resolution)

		images_path = './images/'
		video_path = './' + str(choice_sound) + '_video.avi'
		video_nameSS = str(choice_sound) + '_video.avi'
		video_name = str(choice_sound) + '_video.mkv'
		audio_path = dir_path + './audioFiles/' + str(choice_sound)

		frame_rate = int(input('\nChoose the same framerate that you have chosen for the images : '))

		create_video.main(frame_rate, images_path, video_nameSS)

		add_audio.main(audio_path, video_path, video_name)
		option = int(input('Choose the option you want but be sure you have images to make a video : '))
print('End of the program...')

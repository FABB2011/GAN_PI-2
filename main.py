import fourier
import create_video
import add_audio
import os
import random

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



print('Menu : \n')
print('1 - Create images')
print('2 - Create video')
print('3 - End program')

option = input('Choose the option you want but be sure you have images to make a video : ')

option = int(option)
ema_period = 5
shuffle = random.randint(500, 1500)

while option != 3:
	if option == 1:
		# create images

		print('Here is a list of the available sounds :\n')
		for i in range(len(liste_sounds)):
			print(liste_sounds[i])

		choice_sound = input('\nChoose a sound please (.wav) : ')

		audio_path = './audioFiles/' + str(choice_sound)

		while (choice_sound not in liste_sounds):
			print('Sound not found ! ')
			choice_sound = input('\nChoose a sound please (.wav) : ')

		choice_skip = input('\nChoose also the number of transitions images (to make transitions more fluid) : ')
		skip = int(choice_skip)

		choice_image_number = input('\nChoose also the number of images : ')
		image_number = int(choice_image_number)

		choice_framerate = input('\nChoose also the framerate : ')
		frame_rate = int(choice_framerate)

		fourier.main(audio_path, frame_rate, skip, image_number, ema_period, shuffle)
		option = input('Choose the option you want but be sure you have images to make a video : ')
		option = int(option)

	if option == 2:
		# make a video with the created images

		choice_resolution = input(
			'\n(list of classic values : 240,360,480,720,1080,1440,2160)\nChoose also the resolution of the final video : \n')
		resolution = int(choice_resolution)

		# frame_rate = 20
		# skip = 1
		# image_number = 3
		# images_path = './images/'
		images_path = dir_path + '/images/'
		video_path = dir_path + str(choice_sound) + '_video.avi'
		video_nameSS = str(choice_sound) + '_video.avi'
		video_name = str(choice_sound) + '_video.mkv'
		audio_path = dir_path + '/audioFiles/' + str(choice_sound)

		choice_framerate = input('\nChoose the same framerate that you have chosen for the images : ')
		frame_rate = int(choice_framerate)

		create_video.main(frame_rate, images_path, video_nameSS)
		# add the audio to the video
		add_audio.main(audio_path, video_path, video_name)
		option = input('Choose the option you want but be sure you have images to make a video : ')
		option = int(option)
print('End of the program...')

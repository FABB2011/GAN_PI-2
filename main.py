import fourier
import create_video
import add_audio
import os
import random
import change_video_resolution

dir_path = os.path.dirname(os.path.realpath(__file__))
list_sounds = os.listdir(dir_path+'/audioFiles/')

print('path -> ',os.getcwd())

try:
	os.mkdir('images')
	print("Directory images created")
except FileExistsError:
	print("Directory images exists")

try:
	os.mkdir('audioFiles')
	print("Directory audioFiles created")
except FileExistsError:
	print("Directory audioFiles exists")

print('Welcome to the Gan Clip Generator !\n')
print('Menu : \n')
print('1 - Create images')
print('2 - Create video')
print('3 - End program')

option = int(input('Choose the option you want but make sure you have images to create a video, if you already created images '
			   'and you want to create new one, make sure that the "images" file is empty : '))
ema_period = 15
shuffle = random.randint(100, 1500)

if option == 1:

	print('Here is a list of the available sounds :\n')
	for i in range(len(list_sounds)):
		print(list_sounds[i])

	choice_sound = input('\nChoose a sound please (.wav) : ')

	audio_path = dir_path + '/audioFiles/' + str(choice_sound)

	while (choice_sound not in list_sounds):
		print('Sound not found ! ')
		choice_sound = input('\nChoose a sound please (.wav) : ')

	frame_rate = int(input('\nChoose also the frame rate : '))
	image_number = int(input('\nChoose also the number of images : '))
	skip = int(input('\nChoose also the number of transitions images (to make the video more fluid) : '))

	fourier.main(audio_path, frame_rate, skip, image_number, ema_period, shuffle)

if option == 2:

	print('\nMake sure to use the same parameters (frame rate, sound file) you used to create images')

	resolution = int(input(
		'\n(list of classic values : 240,360,480,720,1080,1440,2160)\nChoose also the resolution of the final video : \n'))

	frame_rate = int(input('\nChoose also the frame rate : '))

	choice_sound = input('\nChoose a sound please (.wav) : ')
	audio_path = dir_path + '/audioFiles/' + str(choice_sound)

	images_path = dir_path + '/images/'
	video_nameSS = 'videoSS.avi'
	video_pathSS = dir_path + '/videoSS.avi'
	video_name = 'video.mkv'
	video_path = dir_path + '/video.mkv'
	video_name_final = 'video_final.mkv'

	create_video.main(frame_rate, images_path, video_nameSS)
	add_audio.main(audio_path, video_pathSS, video_name)
	change_video_resolution.main(video_path, resolution, video_name_final)

if option == 3:
	print('End of the program...')
















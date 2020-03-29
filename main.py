import fourier
import create_video
import add_audio
import random

audio_path = '/home/fabrice/PycharmProjects/GANMovie/audioFiles/subzero45.wav'
frame_rate = 20
skip = 15
image_number = 3
ema_period = 15
shuffle = 800
images_path = '/home/fabrice/PycharmProjects/GANMovie/images/'
video_path = '/home/fabrice/PycharmProjects/GANMovie/video.avi'
video_nameSS = 'video.avi'
video_name = 'video.mkv'

# create images
fourier.main(audio_path, frame_rate, skip, image_number, ema_period, shuffle)
# make a vido with the created images
#create_video.main(frame_rate, images_path, video_nameSS)
# add the audio to the video
#add_audio.main(audio_path, video_path, video_name)


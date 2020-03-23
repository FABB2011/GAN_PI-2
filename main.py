import fourier
import vid3
import assocSonVid


audio_path = '/home/fabrice/PycharmProjects/GANMovie/audioFiles/subzero45.wav'
frame_rate = 2
skip = 5
image_number = 4
ema_period = 15
images_path = '/home/fabrice/PycharmProjects/GANMovie/images/'
video_path = '/home/fabrice/PycharmProjects/GANMovie/output.avi'
video_name = 'nom'

fourier.main(audio_path, frame_rate, skip, image_number, ema_period)
vid3.main(frame_rate, images_path)
assocSonVid.main(audio_path, video_path, video_name)

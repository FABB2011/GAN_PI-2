import fourier
import vid3
import assocSonVid


audio_path = '/home/fabrice/PycharmProjects/GANMovie/audioFiles/Trauma.wav'
frame_rate = 60
skip = 15
image_number = 60
ema_period = 15
shuffle = 800
images_path = '/home/fabrice/PycharmProjects/GANMovie/images/'
video_path = '/home/fabrice/PycharmProjects/GANMovie/out.avi'
video_name = 'nom.mkv'

fourier.main(audio_path, frame_rate, skip, image_number, ema_period, shuffle)
#vid3.main(frame_rate, images_path)
#assocSonVid.main(audio_path, video_path, video_name)


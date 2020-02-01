import subprocess
import ffmpeg

audio = 'sine.wav'
video = 'videoSin.mp4'
sortie = 'av.mkv'

cmd = 'ffmpeg -y -i ' + audio + '  -r 30 -i ' + video + '  -filter:a aresample=async=1 -c:a flac -c:v copy ' + sortie + ''
subprocess.call(cmd, shell=True)
print('Audio et vidéo associé.')
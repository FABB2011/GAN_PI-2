import subprocess
import ffmpeg

audio = '/home/fabrice/PycharmProjects/GANV2/audioFiles/PoneyPart1.wav'
video = '/home/fabrice/PycharmProjects/GANV2/output.avi'
sortie = 'av.mkv'

cmd = 'ffmpeg -y -i ' + audio + '  -r 24 -i ' + video + '  -filter:a aresample=async=1 -c:a flac -c:v copy ' + sortie + ''
subprocess.call(cmd, shell=True)

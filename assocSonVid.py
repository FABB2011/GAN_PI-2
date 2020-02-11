import subprocess
import ffmpeg

audio = '/home/fabrice/PycharmProjects/GANV2/audioFiles/subzero.wav'
video = '/home/fabrice/PycharmProjects/GANV2/output.avi'
sortie = 'av.mkv'

cmd = 'ffmpeg -y -i ' + audio + '  -r 30 -i ' + video + '  -filter:a aresample=async=1 -c:a flac -c:v copy ' + sortie + ''
subprocess.call(cmd, shell=True)

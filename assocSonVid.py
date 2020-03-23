import subprocess


def main(audio_path, video_path, video_name):

    cmd = 'ffmpeg -y -i ' + audio_path + '  -r 24 -i ' + video_path + '  -filter:a aresample=async=1 -c:a flac -c:v copy ' + video_name + ''
    subprocess.call(cmd, shell=True)



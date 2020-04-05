import subprocess

def main(video_path, resolution, nom):
    cmd = 'ffmpeg -i ' + video_path + ' -s ' +  str(resolution) + 'x' + str(resolution) + ' -c:a copy ' + nom
    subprocess.call(cmd, shell=True)
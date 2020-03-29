import cv2
import os


def main(frame_rate, images_path, video_name):
    liste = sorted(os.listdir(images_path))
    liste.sort(key=lambda f: os.path.getmtime(os.path.join(images_path, f)))
    frame = cv2.imread(images_path + liste[0])
    h, l, c = frame.shape
    fourcc = cv2.VideoWriter_fourcc(*'XVID')
    out = cv2.VideoWriter(video_name, fourcc, frame_rate, (l, h))
    for i in range(len(liste)):
        frame = cv2.imread(images_path + liste[i])
        out.write(frame)
    out.release()

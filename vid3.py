import cv2
import os


def main(frame_rate, path_image):

    print('Création de la vidéo')
    liste = sorted(os.listdir(path_image))
    frame = cv2.imread(path_image + liste[0])
    h, l, c = frame.shape
    fourcc = cv2.VideoWriter_fourcc(*'XVID')
    out = cv2.VideoWriter('output.avi', fourcc, frame_rate, (l, h))
    for i in range(len(liste)):
        frame = cv2.imread(path_image + liste[i])
        out.write(frame)
    print('vidéo créée')
    out.release()



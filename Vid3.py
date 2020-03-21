import cv2
import os

path_img = '/home/fabrice/PycharmProjects/GANV2/images/'
fps = 24

print('Création de la vidéo')
liste = sorted(os.listdir(path_img))
liste.sort(key=lambda f: os.path.getctime(os.path.join(path_img, f)))
frame = cv2.imread(path_img + liste[0])
h, l, c = frame.shape
fourcc = cv2.VideoWriter_fourcc(*'XVID')
out = cv2.VideoWriter('output.avi', fourcc, fps, (l, h))
for i in range(len(liste)):
    frame = cv2.imread(path_img + liste[i])
    out.write(frame)
print('vidéo créée')
out.release()
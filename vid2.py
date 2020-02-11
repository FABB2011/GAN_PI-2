import cv2
import os

path_img = '/media/fabrice/FREEDOS/ResultGAN/peinture/images/'
liste = sorted(os.listdir(path_img))
frame = cv2.imread(path_img + liste[0])
h, l, c = frame.shape
fourcc = cv2.VideoWriter_fourcc(*'XVID')
out = cv2.VideoWriter('output.avi', fourcc, 30, (l, h))
for i in range(len(liste)):
    frame = cv2.imread(path_img + liste[i])
    out.write(frame)
out.release()
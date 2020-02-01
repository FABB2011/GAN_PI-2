import os
import cv2
import glob

workdir = "/home/fabrice/PycharmProjects/GANV2/images"

outputVideo = "video.mp4"
if not os.path.exists(workdir):
    os.makedirs(workdir)

img_array = []

size = (None)

for filename in glob.glob(workdir + '/*.png'):
    img = cv2.imread(filename)
    height, width, layers = img.shape
    size = (width, height)
    img_array.append(img)

out = cv2.VideoWriter(outputVideo, cv2.VideoWriter_fourcc(*'DIVX'), 60, size)

for i in range(len(img_array)):
    out.write(img_array[i])
out.release()

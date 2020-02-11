import sys
sys.path.append('./gantools/gantools')
import cli as gaanBreederCli
import os
import shutil
import ffmpeg
import glob
import cv2
import numpy as np
import biggan


movieFrameRate = 3
workdir = "output/01_test_global"
outputVideo = "output/video.mp4"
if not os.path.exists(workdir):
	os.makedirs(workdir)

print('Loading bigGAN...')
gan = biggan.BigGAN()

def main():
	print("Starting program")

	for root, _, files in os.walk('C:/Users/Nicolas/PycharmProjects/Projet_gan_debut/Julian/gan-movie-maker/jsonStore'):
		len(files)

	total_files = len(files)
	print('total : ', total_files)


	keysList=[]

	for k in range(total_files):
		keysList.append("testTri"+str(k))
	print('keysList : ',keysList)

	durations = np.ones(total_files)
	durations[total_files-1] = 0


	print('DUDU : ', durations)


	# Calculating frame number from transition duration
	frameNumberPerDuration=[]
	for duration in durations:
		frameNumberPerDuration.append(int(movieFrameRate*duration))

	folderNames = []
	arguments = ["-uhenri.lieutaud@gmail.com", "-pAB6hzKSXYBf7", "--no-loop", "-o"+workdir]
	i = 0


	# Appel de la fonction sur chaque objet
	for key in keysList:

		# Creating arguments
		#print(frameNumberPerDuration[i])
		if i == len(keysList)-1:
			arguments.append("-k '" + key + "' '" + keysList[0] + "'")
			# arguments.append("-l" + keysList[0])
			arguments.append("-n"+str(frameNumberPerDuration[i]))
			# arguments.append("-o"+folderNames[i])
		else:
			arguments.append("-k" + key + " " + keysList[i+1])
			# arguments.append("-l" + keysList[i+1])
			arguments.append("-n"+str(frameNumberPerDuration[i]))
			# arguments = ["-o outpout", "-uhenri.lieutaud@gmail.com", "-pAB6hzKSXYBf7", "-k" + key , "-l" + keysList[i+1]]
		# arguments.append("-o"+folderNames[i])
		arguments.append("-P"+ str(i).zfill(4))
		i += 1
		print(arguments)
		# Vérification des arguments
		args = gaanBreederCli.handle_args(arguments)
		print(args)

		# Appel de la fonction principale
		# print("la");
		# print(arguments);
		# print("la");
		gaanBreederCli.main(arguments)

	print('PASSAGE FINAL')

	os.chdir('C:/Users/Nicolas/PycharmProjects/Projet_gan_debut/Julian/gan-movie-maker/gantools/gantools/output/01_test_global')

	img_array = []
	for filename in glob.glob(workdir + '/*.png'):
		img = cv2.imread(filename)
		height, width, layers = img.shape
		size = (width, height)
		img_array.append(img)



if __name__ == '__main__':
	main()

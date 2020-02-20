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
workdir = "transitions"
outputVideo = "output/video.mp4"
if not os.path.exists(workdir):
	os.makedirs(workdir)

print('Loading bigGAN...')
gan = biggan.BigGAN()

def main():
	print("Starting program")

	for root, _, files in os.walk('/home/fabrice/PycharmProjects/GANV2/jsonStore'):
		len(files)

	total_files = len(files)
	print('total : ', total_files)


	keysList=[]

	for k in range(total_files):
		keysList.append(str(k))
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

if __name__ == '__main__':
	main()
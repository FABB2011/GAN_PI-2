import cli
import os
import numpy as np


def main(num, gan, suppr):

	for root, _, files in os.walk('/home/fabrice/PycharmProjects/GANMovie/jsonStore'):
		len(files)

	total_files = len(files)

	keysList=[]
	for k in range(total_files):
		keysList.append(str(k))

	durations = np.ones(total_files)
	durations[total_files-1] = 0

	frameNumberPerDuration=[]
	for duration in durations:
		frameNumberPerDuration.append(int(suppr*duration))

	arguments = ["--no-loop"]
	i = 0

	for key in keysList:

		if i == len(keysList)-1:
			arguments.append("-k '" + key + "' '" + keysList[0] + "'")
			arguments.append("-n"+str(frameNumberPerDuration[i]))

		else:
			arguments.append("-k" + key + " " + keysList[i+1])
			arguments.append("-n"+str(frameNumberPerDuration[i]))
		arguments.append("-P"+ str(i).zfill(4))
		i += 1
		cli.main(arguments, num, gan)


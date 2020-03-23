import sys
sys.path.append('./gantools/gantools')
import cli as gaanBreederCli
import os
import numpy as np
import biggan

movieFrameRate = 10
workdir = "transitions"
if not os.path.exists(workdir):
	os.makedirs(workdir)

#gan = biggan.BigGAN()

def main():

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
		frameNumberPerDuration.append(int(movieFrameRate*duration))

	arguments = ["-uhenri.lieutaud@gmail.com", "-pAB6hzKSXYBf7", "--no-loop", "-o"+workdir]
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
		gaanBreederCli.main(arguments, 1, gan)

if __name__ == '__main__':
	main()
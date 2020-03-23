import sys
sys.path.append('./gantools/gantools')
import cli as gaanBreederCli
import os
import numpy as np
import biggan
import pandas as pd

movieFrameRate = 10
workdir = "transitions"
if not os.path.exists(workdir):
	os.makedirs(workdir)

gan = biggan.BigGAN()

def main():

	for root, _, files in os.walk('/home/fabrice/PycharmProjects/GANVMovie/jsonStore'):
		len(files)

	#print(len(files))

	for j in range(2):

		data1 = pd.read_json('/home/fabrice/PycharmProjects/GANVMovie/jsonStore/' + str(j) + '.json', lines=True)
		data2 = pd.read_json('/home/fabrice/PycharmProjects/GANVMovie/jsonStore/' + str(j + 1) + '.json', lines=True)

		if data1['truncation'].values != data2['truncation'].values:

			keysList = []
			for k in range(j, j + 2):
				keysList.append(str(k))

			durations = np.ones(2)
			durations[1] = 0

			frameNumberPerDuration = []
			for duration in durations:
				frameNumberPerDuration.append(int(movieFrameRate * duration))

			arguments = ["-uhenri.lieutaud@gmail.com", "-pAB6hzKSXYBf7", "--no-loop", "-o" + workdir]
			i = 0

			for key in keysList:

				if i == len(keysList) - 1:
					arguments.append("-k '" + key + "' '" + keysList[0] + "'")
					arguments.append("-n" + str(frameNumberPerDuration[i]))

				else:
					arguments.append("-k" + key + " " + keysList[i + 1])
					arguments.append("-n" + str(frameNumberPerDuration[i]))
				arguments.append("-P" + str(i).zfill(4))
				i += 1

				gaanBreederCli.main(arguments, j)
				

if __name__ == '__main__':
	main()
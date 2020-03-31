import sys

sys.path.append('./gantools/gantools')
import cli as gaanBreederCli
import os
import numpy as np
import biggan
import pandas as pd

movieFrameRate = 10


# gan = biggan.BigGAN()

def main(tab):

    tab0 = tab[0][:len(tab[0]) - 1]
    tab1 = tab[1][:len(tab[1]) - 1]

    print(tab0)


















if __name__ == '__main__':
    main()

import cv2
import pandas as pd
import numpy as np
import glob
import os




def loadImageAsGray(imagePath):
    im = cv2.imread(imagePath)
    im = cv2.cvtColor(im, cv2.COLOR_BGR2GRAY)
    return im


def getDataset(path):
    fotos = {}

    for fname in glob.glob(path):
        persona = fname.split('/')[-2]
        print(f"Loading file {fname}")
        if persona in fotos:
            fotos[persona].append(loadImageAsGray(fname))
        else:
            fotos[persona] = [loadImageAsGray(fname)]
    return fotos

fotos = getDataset('../input/korean/carnet/women/*.jpg')



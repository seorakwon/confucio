from __future__ import print_function
from keras.datasets import mnist
from keras.models import Sequential
from keras.layers import Dense, Dropout, Flatten
from keras.layers import Conv2D, MaxPooling2D
from keras import backend as K
import pandas as pd
import numpy as np
import pickle
import cv2
import matplotlib.pyplot as plt
import glob
from keras.callbacks import ModelCheckpoint
from keras.models import load_model
from keras.models import model_from_json
import json
from keras import backend as K

import cv2
import numpy as np
from keras.models import load_model
import tensorflow as tf
from keras import backend as K
import keras
print(keras.__version__)
import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'

model = load_model('oncecuatro.hdf5')

tf_session= K.get_session()
tf_graph = tf.get_default_graph()


def process_image(path):
    im = cv2.imread(path)
    im = cv2.cvtColor(im, cv2.COLOR_BGR2GRAY)
    im_size = cv2.resize(im, (200,200))
    im_np = np.array([im_size])
    im_final = np.expand_dims(im_np, axis =-1)
    return im_final

        
def get_prediction(path):
    global tf_graph,tf_session
    
    with tf_session.as_default():
            with tf_graph.as_default():
   
                prediction = model.predict(process_image(path))[0]
                dirs = ['Chinese', 'Japanese', 'Korean', 'Other']
                for i, p in enumerate(prediction):
                    if p > 0.5:
                        return {
                            "classes":dirs,
                            "prediction": {
                                "label":dirs[i],
                                "prob": str(p)
                            }
                        }
                #print("Probs -> Other:{0:.5f} Chinese:{1:.5f} Japanese{2: .5f} Korean{3: .5f}".format(pred[0],pred[1], pred[2], pred[3]))
    
    



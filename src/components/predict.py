import cv2
import numpy as np
from src.entity import PredictConfig
import os
import tensorflow as tf

class Predictor:
    def __init__(self, config: PredictConfig):
        self.config=config

    def estimate(self):
        self.images=[]
        for fielname in os.listdir(self.config.prediction_dir):
            filepath=os.path.join(self.config.prediction_dir, fielname)
            img=cv2.imread(filepath, 1)
            img=cv2.resize(img, (self.config.image_size[0], self.config.image_size[1]))
            self.images.append(img)

        self.images=np.array(self.images, dtype=np.float32)
        self.images=tf.keras.applications.vgg16.preprocess_input(self.images)
        self.model=tf.keras.models.load_model(self.config.trained_model_path)

        self.y_one_hot=self.model.predict(self.images)

        for i in range(len(self.y_one_hot)):
            p=self.y_one_hot[i].argmax()
            if p==0:
                print('call me')
            elif p==1:
                print('fingers crossed')
            elif p==2:
                print('okay')
            elif p==3:
                print('paper')
            elif p==4:
                print('peace')
            elif p==5:
                print('rock')
            elif p==6:
                print('rock_on')
            elif p==7:
                print('scissor')
            elif p==8:
                print('thumns')
            elif p==9:
                print('up')
#to components
import pickle
import cv2
import numpy as np
import os
from src.entity import PreprocessConfig
from pathlib import Path
import tensorflow as tf

class Preprocess:
    def __init__(self, config:PreprocessConfig) -> None:
        self.config=config
        self.images=[]
        self.labels=[]

    '''
    call me:0
    fingers crossed:1
    okay:2
    paper:3
    peace: 4
    rock: 5
    rock_on: 6
    scissor: 7
    thumns: 8
    up:9
    '''
    
    def process(self):
        i=0
        for folder in os.listdir(self.config.data_path):
            folder_path=os.path.join(self.config.data_path, folder)

            for filename in os.listdir(folder_path):
                lst=[]
                for j in range(self.config.classes):
                    lst.append(0)

                lst[i]=1
                self.labels.append(lst)

                img=cv2.imread(str(os.path.join(folder_path, filename)), 1)
                img=cv2.resize(img, (self.config.image_size[0], self.config.image_size[1]))
                self.images.append(img)
            
            i+=1
        
        self.images=np.array(self.images, dtype=np.float32)
        self.labels=np.array(self.labels, dtype=np.uint8)

        self.images=tf.keras.applications.vgg16.preprocess_input(self.images)

        with open(Path(self.config.image_tensor_path), 'wb') as file:
            pickle.dump(self.images, file)
        
        with open(Path(self.config.labels_path), 'wb') as file:
            pickle.dump(self.labels, file)

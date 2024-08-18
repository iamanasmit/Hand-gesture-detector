from src.entity import PrepareBaseModelConfig
from pathlib import Path
import tensorflow as tf

class PrepareBaseModel:
    def __init__(self, config: PrepareBaseModelConfig):
        self.config=config

    @staticmethod
    def save_model(path:Path, model: tf.keras.Model):
        model.save(path)

    def create_model(self):
        vgg16=tf.keras.applications.vgg16.VGG16(weights='imagenet', include_top=False, input_shape=tuple(self.config.params_image_size))
        vgg16.trainable=False
        input_layer=tf.keras.layers.Input(shape=self.config.params_image_size)
        x=vgg16(input_layer)
        x=tf.keras.layers.Flatten()(x)
        no=256*self.config.params_classes
        # x=tf.keras.layers.Dense(units=self.config.params_classes, activation= 'relu')(x)
        while (no>self.config.params_classes):
            x=tf.keras.layers.Dense(units=no, activation='relu')(x)
            x=tf.keras.layers.Dropout(0.2)(x)
            no=int(no/4)
        x=tf.keras.layers.Dense(units=self.config.params_classes, activation='softmax')(x)
        self.model=tf.keras.Model(inputs=input_layer, outputs=x)
        self.model.summary()
        self.save_model(self.config.updated_base_model_path, self.model)
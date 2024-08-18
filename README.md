# Hand Gesture Recognition with TensorFlow and VGG16

This project implements a hand gesture recognition system using deep learning. The model is built with TensorFlow and utilizes the pre-trained VGG16 model as a base, fine-tuned for the specific task of recognizing various hand gestures.


## Overview

Hand Gesture Recognition is an important area in computer vision with applications in human-computer interaction, sign language interpretation, and more. This project leverages the power of convolutional neural networks (CNNs) to classify hand gestures into different categories.

The project uses a pre-trained VGG16 model to take advantage of transfer learning.

## Dataset

The model is trained on the kaggle dataset (https://www.kaggle.com/datasets/roobansappani/hand-gesture-recognition) containing images of different hand gestures, categorized into the following classes:

1. Call Me
2. Fingers Crossed
3. Okay
4. Paper
5. Peace
6. Rock
7. Rock On
8. Scissor
9. Thumbs Up

Each image in the dataset is resized to 224x224 pixels, which is the input size expected by the VGG16 model.

## Model Architecture

The model architecture is based on the pre-trained VGG16 model from the ImageNet dataset. The top layers of the VGG16 model were removed, and custom fully connected layers were added for the classification of hand gestures.

- **Base Model**: VGG16 pre-trained on ImageNet
- **Custom Layers**:
  - Flatten
  - Dense Layer with ReLU activation
  - Dropout Layer for regularization
  - Output Layer with Softmax activation for classification

The model is compiled with the Adam optimizer and categorical crossentropy loss.

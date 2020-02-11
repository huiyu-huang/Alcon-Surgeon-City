
from __future__ import absolute_import, division, print_function, unicode_literals
import tensorflow as tf


from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Conv2D, Flatten, Dropout, MaxPooling2D
from tensorflow.keras.preprocessing.image import ImageDataGenerator

import os
import numpy as np
import matplotlib.pyplot as plt

import pathlib


train_data_dir = "data/train"
train_data_dir = pathlib.Path(train_data_dir)

test_data_dir = "data/test"
test_data_dir = pathlib.Path(test_data_dir)


train_image_count = len(list(train_data_dir.glob('*/*.jpg')))
test_image_count = len(list(test_data_dir.glob('*/*.jpg')))


CLASS_NAMES = np.array([item.name for item in train_data_dir.glob('*') if item.name != "LICENSE.txt"])


BATCH_SIZE = 32
IMG_HEIGHT = 224
IMG_WIDTH = 224
epochs = 15


train_image_generator = tf.keras.preprocessing.image.ImageDataGenerator(rescale=1./255)

test_image_generator = tf.keras.preprocessing.image.ImageDataGenerator(rescale=1./255)


train_data_gen = train_image_generator.flow_from_directory(directory=str(train_data_dir),
                                                     batch_size=BATCH_SIZE,
                                                     shuffle=True,
                                                     target_size=(IMG_HEIGHT, IMG_WIDTH),
                                                     classes = list(CLASS_NAMES))

test_data_gen = train_image_generator.flow_from_directory(directory=str(test_data_dir),
                                                     batch_size=BATCH_SIZE,
                                                     shuffle=True,
                                                     target_size=(IMG_HEIGHT, IMG_WIDTH),
                                                     classes = list(CLASS_NAMES))





model = Sequential([
    Conv2D(16, 3, padding='same', activation='relu', input_shape=(IMG_HEIGHT, IMG_WIDTH ,3)),
    MaxPooling2D(),
    Conv2D(32, 3, padding='same', activation='relu'),
    MaxPooling2D(),
    Conv2D(64, 3, padding='same', activation='relu'),
    MaxPooling2D(),
    Flatten(),
    Dense(512, activation='relu'),
    Dense(6, activation='softmax')
])

model.compile(optimizer='adam',
              loss='binary_crossentropy',
              metrics=['accuracy'])

model.summary()


history = model.fit_generator(
    train_data_gen,
    steps_per_epoch=train_image_count // BATCH_SIZE,
    epochs=epochs,
    validation_data=test_data_gen,
    validation_steps=test_image_count // BATCH_SIZE
)

model.save('my_model.h5')

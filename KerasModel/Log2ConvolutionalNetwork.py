import os

from PIL import Image
from keras import optimizers
from keras.models import Sequential
from keras.layers import Conv2D, MaxPool2D, Dense, Flatten
from ImageGeneration import Generator as ImageGenerator
import numpy as np

from KerasModel import printModel
from help_functions import print_picture, loadImageMatrix

def init():
    model = Sequential([

        Conv2D(filters=12, kernel_size=3, activation='relu', padding='same', input_shape=(256, 256, 3)),
        MaxPool2D(padding='same'),  # 64

        Conv2D(filters=16, kernel_size=3, activation='relu', padding='same'),
        MaxPool2D(padding='same'),  # 32

        Conv2D(filters=16, kernel_size=3, activation='relu', padding='same'),
        MaxPool2D(padding='same'),  # 16

        Conv2D(filters=16, kernel_size=3, activation='relu', padding='same'),
        MaxPool2D(padding='same'),  # 8

        Conv2D(filters=16, kernel_size=3, activation='relu', padding='same'),
        MaxPool2D(padding='same'),  # 4

        Conv2D(filters=16, kernel_size=3, activation='relu', padding='same'),
        MaxPool2D(padding='same'),  # 2

        Conv2D(filters=16, kernel_size=3, activation='relu', padding='same'),
        MaxPool2D(padding='same'),  # 1

        Flatten(),
        Dense(1, activation='sigmoid')

    ])

    # optimizer = optimizers.SGD(lr=0.01, decay=1e-6, momentum=0.9, nesterov=True)
    optimizer = optimizers.adam(lr=1e-4, decay=1e-6)
    model.compile(loss='mean_squared_error', optimizer=optimizer, metrics=['accuracy'])

    return model


if __name__ == '__main__':
    model = init()

    i = 1
    while True:
        images, labels = ImageGenerator.generator([
            "../ImageGeneration/Images/WithLicence",
            "../ImageGeneration/Images/WithoutLicence",
            "../ImageGeneration/Images/Backgrounds"],
            tbgenerated=200)

        model.fit(np.array(images), labels, batch_size=18, epochs=5, verbose=1, validation_split=0.25)
        model.summary()

        if i % 10 == 0:
            printModel(model)

        i += 1

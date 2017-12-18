import metrics as m
from keras import optimizers
from keras import regularizers as reg
from keras.models import Sequential
from keras.layers import Conv2D, Dense, Flatten


def init():
    model = Sequential([
        Conv2D(input_shape=(512, 512, 3),
               filters=12, kernel_size=7, activation='relu', padding='same', strides=2, kernel_regularizer=reg.l2(0.)),  # 256

        Conv2D(filters=16, kernel_size=5, activation='relu', padding='same', strides=2, kernel_regularizer=reg.l2(0.)),  # 128

        Conv2D(filters=16, kernel_size=3, activation='relu', padding='same', strides=2, kernel_regularizer=reg.l2(0.)),  # 64

        Conv2D(filters=16, kernel_size=3, activation='relu', padding='same', strides=2, kernel_regularizer=reg.l2(0.)),  # 32

        Conv2D(filters=16, kernel_size=3, activation='relu', padding='same', strides=2, kernel_regularizer=reg.l2(0.)),  # 16

        Conv2D(filters=16, kernel_size=3, activation='relu', padding='same', strides=2, kernel_regularizer=reg.l2(0.)),  # 8

        Conv2D(filters=16, kernel_size=3, activation='relu', padding='same', strides=2, kernel_regularizer=reg.l2(0.)),  # 4

        Conv2D(filters=16, kernel_size=3, activation='relu', padding='same', strides=2, kernel_regularizer=reg.l2(0.)),  # 2

        Conv2D(filters=16, kernel_size=3, activation='relu', padding='same', strides=2, kernel_regularizer=reg.l2(0.)),  # 1

        Flatten(),
        Dense(2, activation='softmax')
    ])

    optimizer = optimizers.adam(lr=1e-5, decay=1e-6)
    model.compile(loss='mean_squared_error', optimizer=optimizer, metrics=['accuracy', m.f1measure, m.f_half_measure, m.precision, m.recall])

    return model

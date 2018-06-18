# reference :  https://keras.io/getting-started/sequential-model-guide/#examples
import keras
from keras.models import Sequential
from keras.layers import Dense

import numpy as np

def createModel():
    model = Sequential()

    model.add(Dense(32, activation='relu', input_dim = 100))
    model.add(Dense(1, activation = 'sigmoid'))

    model.compile(optimizer='rmsprop', loss = 'binary_crossentropy', metrics = ['accuracy'])

    return model

# create dummy data
data = np.random.random((1000, 100))
labels = np.random.randint(2, size=(1000, 1))

model = createModel()
model.fit(data, labels, epochs = 20, batch_size = 32)
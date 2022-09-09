# -*- coding: utf-8 -*-
"""
Created on Mon Apr 20 15:27:37 2020

@author: Alan
"""
import numpy as np
from keras.models import Sequential
from keras.layers.core import Dense

#////////XOR////////XOR//////////XOR////////XOR/////XOR/////XOR/////XOR/////
# cargamos las 4 combinaciones de las compuertas XOR
training_data = np.array([[0,0],[0,1],[1,0],[1,1]], "float32")#Xor
 
# y estos son los resultados que se obtienen, en el mismo orden
target_data = np.array([[0],[1],[1],[0]], "float32")#Xor

model = Sequential()
model.add(Dense(16, input_dim=2, activation='relu'))
model.add(Dense(1, activation='sigmoid'))
 
model.compile(loss='mean_squared_error',
              optimizer='adam',
              metrics=['binary_accuracy'])
 
model.fit(training_data, target_data, epochs=200)
 
# evaluamos el modelo
scores = model.evaluate(training_data, target_data)
 
print("\n%s: %.2f%%" % (model.metrics_names[1], scores[1]*100))
print (model.predict(training_data).round())



#////////or////////or//////////or////////or/////or/////or/////OR/////
# cargamos las 4 combinaciones de las compuertas XOR
training_dataO = np.array([[0,0],[0,1],[1,0],[1,1]], "float32")#Or
 
# y estos son los resultados que se obtienen, en el mismo orden
target_dataO = np.array([[0],[1],[1],[1]], "float32")#Or

model = Sequential()
model.add(Dense(16, input_dim=2, activation='relu'))
model.add(Dense(1, activation='sigmoid'))
 
model.compile(loss='mean_squared_error',
              optimizer='adam',
              metrics=['binary_accuracy'])
 
model.fit(training_dataO, target_dataO, epochs=200)
 
# evaluamos el modelo
scores = model.evaluate(training_dataO, target_dataO)
 
print("\n%s: %.2f%%" % (model.metrics_names[1], scores[1]*100))
print (model.predict(training_dataO).round())



#////////AND////////AND//////////AND////////AND/////AND/////AND/////AND/////
# cargamos las 4 combinaciones de las compuertas XOR
training_dataA = np.array([[0,0],[0,1],[1,0],[1,1]], "float32")#And
 
# y estos son los resultados que se obtienen, en el mismo orden
target_dataA = np.array([[0],[0],[0],[1]], "float32")#And

model = Sequential()
model.add(Dense(16, input_dim=2, activation='relu'))
model.add(Dense(1, activation='sigmoid'))
 
model.compile(loss='mean_squared_error',
              optimizer='adam',
              metrics=['binary_accuracy'])
 
model.fit(training_dataA, target_dataA, epochs=200)
 
# evaluamos el modelo
scores = model.evaluate(training_dataA, target_dataA)
 
print("\n%s: %.2f%%" % (model.metrics_names[1], scores[1]*100))
print (model.predict(training_dataA).round())
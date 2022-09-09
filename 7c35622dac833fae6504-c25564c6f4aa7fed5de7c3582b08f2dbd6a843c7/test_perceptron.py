import random

class Perceptron:
    def __init__(self,input_number,step_size=0.1):
        self._ins = input_number
        self._w = [random.random() for _ in range(input_number)]
        self._eta = step_size
        
    def predict(self,inputs):
        weighted_average = sum(w*elm for w,elm in zip(self._w,inputs))
        if weighted_average > 0:
            return 1
        return 0

    def train(self,inputs,ex_output):
        output = self.predict(inputs)
        error = ex_output - output
        if error != 0:
            self._w = [w+self._eta*error*x for w,x in zip(self._w,inputs)]
        return error

#!/usr/bin/env python
#from perceptron import Perceptron

## Datos de hombres y mujeres
input_data = [[170,56,24,1],# Mujer de 1.70m y 56kg
              [172,69,26,0],# Hombre de 1.72m y 63kg
              [160,50,23,1],# Mujer de 1.60m y 50kg
              [170,63,25,0],# Hombre de 1.70m y 63kg
              [174,66,24,1],# Mujer de 1.70m y 56kg
              [158,55,24,0],# Hombre de 1.83m y 80kg
              [180,75,24,1],# Mujer de 1.70m y 56kg
              [185,79,27,0],# Hombre de 1.82m y 70kg
              [150,55,22,1],# Mujer de 1.70m y 56kg
              [183,80,27,0],# Hombre de 1.83m y 80kg
              [160,60,23,1],# Mujer de 1.70m y 56kg
              [158,55,24,0],# Hombre de 1.83m y 80kg
              [165,70,23,1],# Mujer de 1.70m y 56kg
              [177,75,26,0],# Hombre de 1.82m y 70kg
              [152,49,22,1],# Mujer de 1.58m y 55kg
              [175,80,25,0],# Hombre de 1.83m y 80kg
              [166,70,24,1],# Mujer de 1.70m y 56kg
              [163,55,25,0],# Hombre de 1.83m y 80kg
              [153,67,23,1],# Mujer de 1.70m y 56kg
              [173,68,26,0],# Hombre de 1.83m y 80kg
              [168,65,23,1],# Mujer de 1.58m y 55kg
              [188,80,27,0],# Hombre de 1.83m y 80kg
              [170,70,24,1],# Mujer de 1.70m y 56kg
              [160,55,25,0],# Hombre de 1.83m y 80kg
              [165,61,23,1],# Mujer de 1.70m y 56kg
              [174,70,26,0],# Hombre de 1.82m y 70kg
              [149,55,22,1],# Mujer de 1.58m y 55kg
              [190,85,28,0],# Hombre de 1.83m y 80kg
              [162,65,23,1],# Mujer de 1.58m y 55kg
              [178,80,27,0],# Hombre de 1.83m y 80kg
              [160,70,23,1],# Mujer de 1.70m y 56kg
              [168,70,26,0],# Hombre de 1.83m y 80kg
              [183,90,24,1],# Mujer de 1.70m y 56kg
              [182,70,27,0],# Hombre de 1.82m y 70kg
              [158,55,23,1],# Mujer de 1.58m y 55kg
              [183,80,28,0],# Hombre de 1.83m y 80kg
              [180,70,24,1],# Mujer de 1.70m y 56kg
              [158,65,26,0],# Hombre de 1.83m y 80kg
              [160,70,23,1],# Mujer de 1.70m y 56kg
              [162,70,26,0],# Hombre de 1.82m y 70kg
              [158,55,23,1],# Mujer de 1.58m y 55kg
              [173,80,27,0],# Hombre de 1.83m y 80kg
              [158,45,23,1],# Mujer de 1.58m y 55kg
              [190,86,28,0],# Hombre de 1.83m y 80kg
              [151,60,22,1],# Mujer de 1.70m y 56kg
              [164,70,26,0],# Hombre de 1.82m y 70kg
              [155,60,23,1],# Mujer de 1.70m y 56kg
              [166,70,26,0],# Hombre de 1.82m y 70kg
              [157,55,22,1],# Mujer de 1.58m y 55kg
              [169,60,26,0],# Hombre de 1.83m y 80kg
              [163,70,23,1],# Mujer de 1.70m y 56kg
              [158,55,25,0],# Hombre de 1.83m y 80kg
              [165,70,23,1],# Mujer de 1.70m y 56kg
              [172,70,27,0],# Hombre de 1.82m y 70kg
              [179,70,24,1],# Mujer de 1.58m y 55kg
              [199,90,30,0],# Hombre de 1.83m y 80kg
              [145,50,22,1],# Mujer de 1.70m y 56kg
              [155,55,25,0],# Hombre de 1.83m y 80kg
              [143,50,22,1],# Mujer de 1.70m y 56kg
              [154,60,25,0],# Hombre de 1.82m y 70kg
              [162,60,23,1],# Mujer de 1.70m y 56kg
              [193,87,29,0],# Hombre de 1.83m y 80kg
              [167,62,23,1],# Mujer de 1.70m y 56kg
              [158,55,25,0],# Hombre de 1.83m y 80kg
              [173,80,24,1],# Mujer de 1.70m y 56kg
              [162,70,26,0],# Hombre de 1.82m y 70kg
              [178,75,24,1],# Mujer de 1.58m y 55kg
              [183,80,28,0],# Hombre de 1.83m y 80kg
              [162,70,22,1],# Mujer de 1.70m y 56kg
              [179,75,28,0],# Hombre de 1.83m y 80kg
              [153,60,22,1],# Mujer de 1.70m y 56kg
              [195,90,30,0],# Hombre de 1.82m y 70kg
              [148,55,22,1],# Mujer de 1.58m y 55kg
              [160,70,26,0],# Hombre de 1.83m y 80kg
              [177,70,24,1],# Mujer de 1.70m y 56kg
              [188,85,28,0],# Hombre de 1.83m y 80kg
              [181,80,24,1],# Mujer de 1.70m y 56kg
              [192,86,29,0],# Hombre de 1.82m y 70kg
              [168,70,24,1],# Mujer de 1.70m y 56kg
              [175,80,27,0],# Hombre de 1.83m y 80kg
              [160,70,23,1],# Mujer de 1.70m y 56kg
              [163,55,26,0],# Hombre de 1.83m y 80kg
              [173,80,24,1],# Mujer de 1.70m y 56kg
              [152,63,25,0],# Hombre de 1.82m y 70kg
              [150,55,22,1],# Mujer de 1.70m y 56kg
              [183,80,29,0],# Hombre de 1.83m y 80kg
              [153,60,22,1],# Mujer de 1.70m y 56kg
              [164,55,26,0],# Hombre de 1.83m y 80kg
              [171,80,24,1],# Mujer de 1.70m y 56kg
              [182,70,28,0],# Hombre de 1.82m y 70kg
              [178,75,24,1],# Mujer de 1.58m y 55kg
              [160,74,26,0],# Hombre de 1.83m y 80kg
              [156,55,22,1],# Mujer de 1.58m y 55kg
              [193,80,29,0],# Hombre de 1.83m y 80kg
              [162,70,22,1],# Mujer de 1.70m y 56kg
              [172,70,27,0],# Hombre de 1.82m y 70kg
              [153,60,22,1],# Mujer de 1.70m y 56kg
              [185,70,28,0],# Hombre de 1.82m y 70kg
              [151,55,22,1],# Mujer de 1.58m y 55kg
              [183,80,28,0],# Hombre de 1.83m y 80kg
              [165,54,23,1]]# Mujer de 1.65m y 54kg
                

## Creamos el perceptron
pr = Perceptron(4,0.1) # Perceptron con 3 entradas
weights = [] # Lista con los pesos
errors = []  # Lista con los errores

## Fase de entrenamiento
for _ in range(100):
    # Vamos a entrenarlo varias veces sobre los mismos datos
    # para que los 'pesos' converjan
    for person in input_data:
        output = person[-1]
        inp = [1] + person[0:-1] # Agregamos un uno por default
        weights.append(pr._w)
        err = pr.train(inp,output)
        errors.append(err)

h = float(input("Introduce tu estatura en centimetros.- "))
w = float(input("Introduce tu peso en kilogramos.- "))
np = float(input("Introduce tu número de pie.- "))

if pr.predict([1,h,w,np]) == 1: print ("Mujer")
else: print ("Hombre")

#print """
#Nota: El resultado puede estar incorrecto. 
#Esto puede ser debido a sesgo en la muestra, o porque es imposible separar
#a hombres y mujeres perfectamente basados unicamente en talla y peso."""

## Fase de graficacion
import imp

can_plot = True
try:
    imp.find_module('matplotlib')
except:
    can_plot = False

if not can_plot:
    print ("No es posible graficar los resultados porque no tienes matplotlib")
    sys.exit(0)
    pass

import matplotlib.pyplot as plt

plt.plot(errors)
plt.show()
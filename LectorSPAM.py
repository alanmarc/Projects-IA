import collections


salida = []
 
print("-------Ingresa el nombre de tu archivo-------")
archivo = input()
    
with open( archivo +'.txt', 'r') as f:
    lineas = [linea.split() for linea in f]

for linea in lineas:

    cuenta1 = collections.Counter(linea)
    
    
   
    print ("Las palabras mas usadas son ")
    print(cuenta1.most_common(3)) #muestra los primeros tres mas repetidos
    

    
    
    
    
    
    
# -*- coding: utf-8 -*-
"""
Created on Sat Feb  1 21:44:46 2020

@author: user
"""
#Se importa la libreria networkx como nx
import networkx as nx
#Se importa la libreria pyplot de matplotlib como plt
import matplotlib.pyplot as plt
#Se crea un grafo vacio
G=nx.Graph()
#Se crean los nodos:
#Nodo Venezuela
G.add_node("Abuelo")

#Se crean los nodos de los estados

G.add_nodes_from(["Padre1","Padre2","Padre3","Padre4"])

#Se crean los nodos de las ciudades.

G.add_nodes_from(["Hijo11","Hijo12","Hijo21","Hijo22","Hijo31","Hijo32","Hijo41","Hijo42"])

#Se crean los enlaces de los estados al país

G.add_edge("Padre1","Abuelo")

G.add_edge("Padre2","Abuelo")

G.add_edge("Padre3","Abuelo")

G.add_edge("Padre4","Abuelo")

G.add_edge("Hijo11","Padre1")

G.add_edge("Hijo12","Padre1")

G.add_edge("Hijo21","Padre2")

G.add_edge("Hijo21","Padre2")

G.add_edge("Hijo31","Padre3")

G.add_edge("Hijo32","Padre3")

G.add_edge("Hijo41","Padre4")

G.add_edge("Hijo42","Padre4")


#Se dibuja el grafo

nx.draw(G)

#Se muestra en pantalla

plt.show()

#Se vuelve a dibujar el grafo y se salva en un archivo png.

nx.draw(G)

plt.savefig("networkx1.png")

#Se muestra información de los nodos (cantidad, nodos)

print ("Nodos: ", G.number_of_nodes(), G.nodes())

#SE muestra información de los enlaces (cantidad, enlaces)

print ("Enlaces: ", G.number_of_edges(),G.edges())
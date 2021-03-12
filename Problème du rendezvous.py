#!/usr/bin/env python
# coding: utf-8

# # Environement et bibliothèque
# 
# 

# In[24]:


import numpy as np
import matplotlib.pyplot as plt
import random
import networkx as nx
from matplotlib import cm
from celluloid import Camera


# # Définition des fonctions
# 
# ### random_adjacency_matrix(n) : 
#  Est la fonction qui génère une matrice aléatoire d'adjacence symétrique de taille n*n
#  
# ### show_graph_with_labels(adjacency_matrix) :
#  Affichage du graphe à l'aide de la bibliothèque networkx
#  
# ### mouvement(x,y) :
#   Est la fonction qui définie le mouvement des noeuds qui dépend de la position de ses voisins ainsi que la matrice de communication  

# In[25]:



def random_adjacency_matrix(n):   
    matrix = [[random.randint(0, 1) for i in range(n)] for j in range(n)]

    # pas de boucle sur le même noeuds
    for i in range(n):
        matrix[i][i] = 0

    # If i is connected to j, j is connected to i
    for i in range(n):
        for j in range(n):
            matrix[j][i] = matrix[i][j]

    return matrix

def show_graph_with_labels(adjacency_matrix):
    rows, cols = np.where(adjacency_matrix == 1)
    edges = zip(rows.tolist(), cols.tolist())
    gr = nx.Graph()
    gr.add_edges_from(edges)
    nx.draw(gr, node_size=500, with_labels=True)
    plt.show()

def mouvement(x,y):    
    for i in range(n):
        for j in range(n):
            x[i] += (x[j]-x[i])*C[i][j]
            y[i] += (y[j]-y[i])*C[i][j]

    return x,y


# ### Paramètres

# In[26]:


n = 50 #nb des noeuds
k = 20  #nb des itérations


# In[27]:


#matrice d'adjacence
M = random_adjacency_matrix(n)

#matrice de communication
C = np.copy(np.array(M))
facteur=np.sum(M,axis=1)
C = C.astype('float')
for i in range(n):
    if facteur[i]==0:
        facteur[i] = 1
    C[i]=C[i]/facteur[i]

a = np.array(M)

#positionner les robots aléatoirement 
rnd = np.random
rnd.seed(0)

x = rnd.rand(n)*200
y = rnd.rand(n)*100


# In[28]:


show_graph_with_labels(a)

colors = cm.rainbow(np.linspace(0, 1, n))

camera = Camera(plt.figure())

plt.scatter(x[0:], y[0:],c=colors, s=100)

for _ in range(k):
    x,y = mouvement(x,y)
    plt.scatter(x[0:], y[0:], c=colors, s=100)
    
    plt.pause(0.1)
    camera.snap()

anim = camera.animate(interval = 200, blit=True)
anim.save('rdv2.mp4')


# # Conclusion
# 
# Après 15 itérations on remarque que les 10 points sont presque confondues et après 45 itérations les 10 points sont confondues.
# 

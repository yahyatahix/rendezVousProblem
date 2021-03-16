#!/usr/bin/env python
# coding: utf-8

# In[42]:


import numpy as np
import matplotlib.pyplot as plt
import random
import networkx as nx
from matplotlib import cm
from celluloid import Camera


# In[43]:


n = 10 #nb des noeuds
k = 20  #nb des itérations
r_sec = 2  #rayon de détection


# In[44]:



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

def position_initial(n):
    rnd = np.random
    rnd.seed(0)

    x = rnd.rand(n)*200
    y = rnd.rand(n)*100

    for i in range(n):
        for j in range(n):
            if abs(x[j]-x[i]) <= 2*r_sec:
                if x[i]-x[j] <= 0:
                    x[i] += -2*r_sec
                if x[i]-x[j] > 0:
                    x[i] += 2*r_sec

            if abs(y[j]-y[i]) <= 2*r_sec:
                if y[i]-y[j] <= 0:
                    y[i] += -2*r_sec
                if y[i]-y[j] > 0:
                    y[i] += 2*r_sec

    return x,y


# In[45]:


#matrice d'adjacence
M = random_adjacency_matrix(n)

#affichage
a = np.array(M)
print("matrice d'adjacence :\n",a.reshape(n,n))

#matrice de communication
C = np.copy(np.array(M))
facteur=np.sum(M,axis=1)
C = C.astype('float')
for i in range(n):
    if facteur[i]==0:
        facteur[i] = 1
    C[i]=C[i]/facteur[i]

print("\n\n matrice de communication :\n", C.reshape(n,n))


# In[46]:


show_graph_with_labels(a)


# In[47]:


#positionner les robots aléatoirement 
#rnd = np.random
#rnd.seed(0)

#x = rnd.rand(n)*200
#y = rnd.rand(n)*100

x,y = position_initial(n)


# In[48]:


colors = cm.rainbow(np.linspace(0, 1, n))

camera = Camera(plt.figure())


for _ in range(k):
    x,y = mouvement(x,y)
    plt.scatter(x[0:], y[0:], c=colors, s=100)
    
    for i in range(n):
        plt.annotate(i, (x[i], y[i]))
    
    plt.pause(1.1)
    camera.snap()

anim = camera.animate(blit=True)
anim.save('rdv2.mp4')


# In[ ]:





# rendezVousProblem

Soit un graphe de voisinage composé de n nœuds, et sa matrice d’adjacence A. 
Initialement, les agents sont placés aléatoirement sur un espace de 2 dimensions.  
Pour se déplacer, chaque agent utilise la matrice de communication qui découle de la matrice d’adajacence.  
Les agents doivent se rencontrer dans la même zone si après.

La formule de déplacement des agents à la (k+1) ème itération:
 
\[ x_{i}^{k+1}=\sum_{j=0}^{n-1} (x_{j}^{k} - x_{i}^{k})\times C_{ij}  \]\\

\[ y_{i}^{k+1}=\sum_{j=0}^{n-1} (y_{j}^{k} - y_{i}^{k})\times C_{ij}  \]\\


La première version consiste à regrouper les agents avec une matrice de communication aléatoire sans prendre en considération le rayon de sécurité.\\

La deuxième version consiste à prendre en considération le rayon de sécurité :\\
C'est à dire respecter cette condition :
\[ |x_{j}^{k} - x_{i}^{k} | \times a_{ij} \geq 2 \times r_{sécurité}  \]

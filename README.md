# rendezVousProblem

Soit un graphe de voisinage composé de n nœuds, et sa matrice d'adjacence A.
 Initialement, les agents sont placés aléatoirement sur un espace de 2 dimensions. 
 Pour se déplacer, chaque agent utilise la matrice de communication qui découle de la matrice d'adajacence. 
 Les agents doivent se rencontrer dans la même zone si après.\\
 
La formule de déplacement des agents à la (k+1) ème itération:
 
 $$
\begin{aligned}
&v_{i}[k+1]=v_{i}[k]+\sum_{j=1}^{N} c_{i j}\left(v_{j}[k]-v_{i}[k]\right)\\
\end{aligned}
$$

$$
\begin{aligned}
&X=\left(x_{i}\right)_{1 \leqslant i<N}\text { ensemble des abscisses des agents  }\\
&Y=\left(y_{i}\right)_{1 \leqslant i<N}\text { ensemble des ordonnées des agents  }\\ 
\end{aligned}
$$

$$
V=\left(v_{i}\right)_{1 \leqslant i\leqslant N} = 
\begin{bmatrix}
x_{i} \\
y_{i} 
\end{bmatrix}
\\
$$

$$
\mathbf{A} =
\begin{bmatrix}
a_{11} & a_{12} & \cdots & a_{1N} \\
a_{21} & a_{22} & \cdots & a_{2N} \\
\vdots & \vdots & \ddots & \vdots \\
a_{N1} & a_{N2} & \cdots & a_{NN}
\end{bmatrix} =
\begin{pmatrix}
a_{11} & a_{12} & \cdots & a_{1N} \\
a_{21} & a_{22} & \cdots & a_{2N} \\
\vdots & \vdots & \ddots & \vdots \\
a_{m1} & a_{m2} & \cdots & a_{NN}
\end{pmatrix}\text { Matrice d'adjacence }\\
$$

Avec :


$$
a_{i j}=\left\{\begin{array}{ll}
1  & \text { ; si j voisin de i } \\
0  & \text { ; sinon } \\
0  &  \text { ; si i=j} \\
\end{array}\right.
$$
$$
{\sum_{j=1}^{N} a_{i j}} \neq 0 \text {   càd aucun agent n'est isolé }
$$

$$
C=\left(c_{i j}\right)_{1 \leqslant i \leqslant N,1 \leqslant j \leqslant N}=\left(\frac{a_{i j}}{\sum_{j=1}^{N} a_{i j}}\right)_{1 \leqslant i \leqslant N,1 \leqslant j \leqslant N}\text { Matrice de communication }\\
$$

La première version consiste à regrouper les agents avec une matrice de communication aléatoire sans prendre en considération le rayon de sécurité.\\

La deuxième version consiste à prendre en considération le rayon de détection en actualisant à chaque itération la matrice d'adjacence ainsi que la matrice de communication. \\

La troisième version consiste à prendre en considération le rayon de sécurité ainsi de le rayon de détection  :\\

C'est à dire respecter cette condition :
$$ |x_{j}^{k} - x_{i}^{k} | \times a_{ij} \geq 2 \times r_{sécurité}  $$
#### Environement

package celluloid, ffmpeg

#!/usr/bin/env python
# coding: utf-8

# In[12]:


import numpy as np
import pandas as pd
from copy import deepcopy
dataset = pd.read_csv('data.csv')

def euclidean(a,b, ax=1):
    return np.linalg.norm(a-b, axis=ax)
k = 3
print("Dataset is :" )
print(dataset)

X1=dataset["X1"].values
X2=dataset["X2"].values
X=np.array(list(zip(X1,X2)))
C_X=[6.2,6.6,6.5]
C_Y=[3.2,3.7,3.0]
C_x = [6.2, 6.6 ,6.5]
C_y = [3.2, 3.7, 3.0]

Centroid = np.array(list(zip(C_x, C_y)), dtype=np.float32)
print("Initial Centroids")
print(Centroid.shape)
Centroid_old = np.zeros(Centroid.shape)
print("Old centroids are:")
print(Centroid_old)
clusters = np.zeros(len(X))
print("Clusters are :")
print(clusters)
error = euclidean(Centroid, Centroid_old, None)
print(error)
iterr = 0
while error != 0:
        iterr = iterr + 1
        for i in range(len(dataset)):
                     distances = euclidean(X[i], Centroid)
                     cluster = np.argmin(distances)
                     clusters[i] = cluster
        Centroid_old = deepcopy(Centroid)
        for p in range(k):
            points = [X[j] for j in range(len(dataset)) if clusters[j] == p]
            Centroid[p] = np.mean(points, axis=0)
        print(" Centre of the clusters after ", iterr," Iteration \n", Centroid)
        error = euclidean(Centroid, Centroid_old, None)
        print("Error  ... ",error)  
    


# In[ ]:





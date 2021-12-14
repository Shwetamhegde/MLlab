#!/usr/bin/env python
# coding: utf-8

# In[20]:


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import statistics as st

col_names=['x','y']
food = pd.read_csv("Food-Truck-LineReg.csv",names=col_names)
X=food['x'].values
Y=food['y'].values

n=np.size(X)

m_x = np.mean(X)
m_y = np.mean(Y)
print("mean of x =",m_x)
print("mean of y=",m_y)

Sy=st.stdev(Y)
Sx=st.stdev(X)
print("standard deviation of y =",Sy)
print("standard deviation of x=",Sx)

import scipy.stats
r=scipy.stats.pearsonr(X,Y)[0]
print("r=",r)

m=r*(Sy/Sx)
print("slope(m)=",m)

# plotting the actual points as scatter plot
plt.scatter(X, Y, color = "m",marker = "o", s = 30)

#finding intercept
c=m_y-(m*m_x)
print("intercept(c)=",c)

y_pred=(m*X)+c

plt.scatter(X, Y, color = "m",marker = "o", s = 30)
# plotting the regression line
plt.plot(X, y_pred, color = "b")

# putting labels    
plt.xlabel('x')
plt.ylabel('y')

# function to show plot
plt.show()

cost=Y-y_pred
print("cost=",cost)

#SSE
sse=sum((Y-y_pred)**2)
print("SSE=",sse)

#SSR
ssr=sum((y_pred-m_y)**2)
print("SSR=",ssr)

#SST
sst=sum((Y-m_y)**2)
print("SST=",sst)

#R square
R2=1-(sse/sst)
print("R square=",R2)


# In[ ]:





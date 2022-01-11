#!/usr/bin/env python
# coding: utf-8

# In[6]:


import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
import warnings
warnings.filterwarnings( "ignore" )

col_names=['x1','x2','result']
df = pd.read_csv( "Student-University.csv" ,names=col_names)
print(df)


# In[3]:


from sklearn.model_selection import train_test_splitX = df.iloc[:,:-1].values
print(X)


# In[4]:


Y = df.iloc[:,-1:].values
print(Y)


# In[10]:


X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size = 1/3, random_state = 0 )
print("Printing trainng data")
print(X_train,Y_train)
print("Printing testing data")
print(X_test,Y_test)


# In[11]:


x1=X_train[:,0]
x2=X_train[:,1]


# In[29]:


b0=0.0
b1=0.0
b2=0.0
y=b0 + b1*x1 + b2*x2
print(y)


# In[22]:


#calculating predictiony_final=b0 + b1*x1 + b2*x2
final_prediction=1 / (1 + np.exp(-y_final))
print(np.round(final_prediction))
print(Y_train)
prediction=1 / (1 + np.exp(-y))
print(np.round(prediction))
print(Y_train)


# In[30]:


alpha = 0.01   #alpha is the Learning rate
epochs = 5000
x=1
for epoch in range(epochs):
    y_pred = 1 / (1 + np.exp(-y))
    # Update b0,b1,b2
    b0 = + alpha * (y - prediction) * prediction * (1 - prediction) * x
    b1 = + alpha * (y - prediction) * prediction * (1 - prediction) * x1
    b2 = + alpha * (y - prediction) * prediction * (1 - prediction) * x2


# In[31]:


y_final=b0 + b1*x1 + b2*x2
final_prediction=1 / (1 + np.exp(-y_final))
print(np.round(final_prediction))
print(Y_train)


# In[ ]:





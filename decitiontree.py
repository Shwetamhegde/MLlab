#!/usr/bin/env python
# coding: utf-8

# In[19]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
data=pd.read_csv("zoodataset.csv")
data


# In[7]:


x1=data['hair'].values
x2=data['feathers'].values
x3=data['eggs'].values
x4=data['milk'].values
x5=data['airborne'].values
x6=data['aquatic'].values
x7=data['predator'].values
x8=data['toothed'].values
x9=data['backbone'].values
x10=data['breathes'].values
x11=data['venomous'].values
x12=data['fins'].values
x13=data['legs'].values
x14=data['tail'].values
x15=data['domestic'].values
x16=data['catsize'].values
y =data['class_type'].values


# In[8]:


X = np.array(list(zip(x1,x2,x3,x4,x5,x6,x7,x8,x9,x10,x11,x12,x13,x14,x15,x16)))
X


# In[9]:


Y=y
Y


# In[10]:


from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X,Y,test_size=0.25)


# In[11]:


from sklearn.metrics import classification_report,confusion_matrix,accuracy_score
from sklearn import tree


# In[12]:


decision = tree.DecisionTreeClassifier(criterion='gini')
decision.fit(X_train,y_train)


# In[13]:


y_predict=decision.predict(X_test)
y_score = accuracy_score(y_test,y_predict)
print('Accuracy: ', y_score)
y_test


# In[20]:


print(classification_report(y_test,y_predict))


# In[18]:


print(confusion_matrix(y_test,y_predict))


# In[ ]:





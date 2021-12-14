#!/usr/bin/env python
# coding: utf-8

# In[57]:


from collections import Counter
def mmm(a):
    sum=0
    n=len(a)
    for i in a:
        sum=sum+i
    mean1=sum/n
    print(mean1)
    a.sort()
    if n%2==0:
        med1=a[n//2]
        med2=a[n//2]+1
        median=(med1+med2)/2
    else:
        median=a[n//2]
    print(median)  
    
    data = Counter(a)
    get_mode = dict(data)
    mode = [k for k, v import statistics
a=[3,2,4,6,8,4,3,8,9,5,7,4,6,8,67]
n=len(a)
for i in a:
    sum=sum+i
mean1=sum/n
var=varience1(a)   
stdv=math.sqrt(var)    
for x in a:
    s=(x-mean)/stdvn get_mode.items() if v == max(list(data.values()))]
  
    if len(mode) == n:
        get_mode = "No mode found"
    else:
        get_mode = "Mode is / are: " + ', '.join(map(str, mode))
      
    print(get_mode)
    


# In[50]:


def varience1(a):
    n=len(a)
    mean=sum(a)/n
    deviations=[(x-mean)**2 for x in a]
    var=sum(deviations)/n
    return var


# In[32]:


a=[10,6,3,4,5,8,9,10,9]  
varience1(a)   
mmm(a)


# In[1]:


a=[10,23,4,5,6]
minimum=min(a)
maximum=max(a)
for x in a:
    n=(x-minimum)/(maximum-minimum)
    print("{}:{}".format(x,n))
    


# In[58]:


import math
a=[7,3,2,1.3,4,9,7,8,1]
mean=sum(a)/len(a)
var=sum((i-mean)**2 for i in a)/len(a)
sd=va**0.5
print("Value:Standardization value")
for x in a:
    s=(x-mean)/sd
    print("{}:{}".format(x,s))


# In[ ]:





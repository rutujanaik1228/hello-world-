#!/usr/bin/env python
# coding: utf-8

# In[22]:


l=[]
n=int(input("enter no. of elements :"))
for i in range(0,n):
    a=int(input("enter list element"))
    l.append(a)
print("the list is:",l)
sum=0
for i in range(0,n):
        a=l[i]
        sum+=a
print(sum)
avg=sum/n
print("the average is:",avg)


# In[19]:


5


# In[ ]:





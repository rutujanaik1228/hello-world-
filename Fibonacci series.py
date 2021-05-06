#!/usr/bin/env python
# coding: utf-8

# In[6]:


n=int(input("enter number of terms:"))
n1,n2=0,1
cnt=0
if n<=0:
    print("enter a positive integer")
elif n==1:
    print("fibonacci series upto",n,"terms:")
    print(n1)
else:
    print("fibonacci series upto",n,"terms:")
    while cnt<n:
        print(n1)
        n3=n1+n2
        n1=n2
        n2=n3
        cnt+=1


# In[ ]:





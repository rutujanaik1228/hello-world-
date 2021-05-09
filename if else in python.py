#!/usr/bin/env python
# coding: utf-8

# In[2]:


n=int(input("enter a number:"))
if n%2!=0:
    print("weird")
else:
    if n in range(2,6):
        print("not weird")
    if n in range(6,20):
        print("weird")
    if n>20 :
        print("not weird")
        


# In[ ]:





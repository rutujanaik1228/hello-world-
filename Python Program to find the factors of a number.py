#!/usr/bin/env python
# coding: utf-8

# In[4]:


def print_factors(x):
   print("The factors of",x,"are:")
   for i in range(1, x + 1):
       if x % i == 0:
           print(i)

num = int(input("enter a number:"))

print_factors(num)


# In[ ]:





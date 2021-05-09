#!/usr/bin/env python
# coding: utf-8

# In[12]:


def int_to_str():
    num=int(input("enter an integer:"))
    a=type(num)
    b=str(num)
    c=type(b)
    print("the enetred integer was:",num,"with type",a)
    print("on conversion:",b,"with type",c)
    
int_to_str()  
def str_to_int():
    num=str(input("enter an integer:"))
    a=type(num)
    b=int(num)
    c=type(b)
    print("the enetred string was:",num,"with type",a)
    print("on conversion:",b,"with type",c)
    
str_to_int()  


# In[ ]:





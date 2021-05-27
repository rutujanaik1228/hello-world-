#!/usr/bin/env python
# coding: utf-8

# In[ ]:


m=float(input("Enter mass in kgs: "))  
c=float(input("Enter velocity in m/s: "))

if m==0 or c==0:
  print('Momentum of object is zero.')
else:
  e=m*(c**2)
  print('Momentum of object is', e)


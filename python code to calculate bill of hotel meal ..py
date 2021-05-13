#!/usr/bin/env python
# coding: utf-8

# In[3]:


def solve(meal_cost, tip_percent, tax_percent):
    tip = (meal_cost * tip_percent) / 100
    tax = (meal_cost * tax_percent) / 100
    totalCost = int(round(meal_cost + tip + tax))
    print(totalCost)
meal_cost = float(input("enter meal cost "))

tip_percent = int(input("enter tip percent "))

tax_percent = int(input("enter tax percent"))

solve(meal_cost, tip_percent, tax_percent)


# In[ ]:





# In[ ]:





# -*- coding: utf-8 -*-
"""Write a Python program to sum of two given integers. However, if the sum is between 15 to 20 it will return 20

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1Dqp0dlJT0uJaVLkRLYRe9lgQKK7XayJZ
"""

a=int(input("enter a number"))
b=int(input("enter a number"))
s=a+b
if s in range(15,21):
  print("20")
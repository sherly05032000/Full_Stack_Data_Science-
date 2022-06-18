#!/usr/bin/env python
# coding: utf-8

# 1. Write a Python program to convert kilometers to miles?

# In[2]:


def kmToMiles():
    kiloMeters = float(input("Enter no of kilometers : "))
    print("{} km is Equal to {} miles".format(kiloMeters,kiloMeters*0.621))

kmToMiles()


# 2. Write a Python program to convert Celsius to Fahrenheit?

# In[3]:


def celToFarh():
    celsius = int(input("Enter temperature in celsius : "))
    Farenheit = (celsius*(9/5))+32
    print("{}° Celsius is Equal to {}° Farenheit".format(celsius,Farenheit))
    
celToFarh()


# 3. Write a Python program to display calendar

# In[5]:


import calendar

def showCalender():
    year = int(input("Enter calender year: "))
    print(calendar.calendar(year))
    
showCalender()


# 4. Write a Python program to solve quadratic equation?

# In[6]:


import cmath
import math

def quadarticEquationRoots(a,b,c):
    
    discriminant = b*b-4*a*c
    
    if discriminant == 0:
        r1 = -b/2*a
        r2 = -b/2*a
        print("Roots are Real",r1,r2)
    elif discriminant > 0:
        r1 = (-b-math.sqrt(discriminant))/(2 * a)
        r2 = (-b+math.sqrt(discriminant))/(2 * a)
        print("Roots are Real and different",r1,r2)
    else:
        r1 = (-b-cmath.sqrt(discriminant))/(2 * a)
        r2 = (-b+cmath.sqrt(discriminant))/(2 * a)
        print("Roots are Imaginary",r1,r2)


a = int(input('Enter a value: '))
b = int(input('Enter b value: '))
c = int(input('Enter c value: '))

quadarticEquationRoots(a,b,c)


# 5. Write a Python program to swap two variables without temp variable?

# In[7]:


num_1 = int(input('Enter first number: '))
num_2 = int(input('Enter second number: '))


def swapNumbers(num_1,num_2):
        print('Before Swapping',num_1,num_2)
        num_1 = num_1+num_2
        num_2 = num_1-num_2
        num_1 = num_1-num_2
        print('before Swapping',num_1,num_2)

swapNumbers(num_1,num_2)


# In[ ]:





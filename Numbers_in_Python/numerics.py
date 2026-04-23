# What are numeric values in python?


#1.int: 5,-22,10000
#2.float: 3.123
#omplete:advanced Math Engineeering Physics Science{ex- 2+3j}

#Numeric Function

#1. Types
print("-"*15+"1.types"+"-"*15)
x="24"
print(type(x))
print(x*3)    #"24" is a string python repeats the next istead of doing math

x=int(x) #type casting
print(type(x))
print(x*3)
print(float(x))

x="3.14"
print(float(x))# float: convert compatible value into float value

x=3 #real part
y=4 #imaginary part
print(complex(x,y)) #complex: creates a complex number using real and imaginary parts



print("-"*15+"2.Maths Operator"+"-"*15)
print(2+3)
print(5-3)
print(4*2)
print(7/2)
print(7//2)
print(9%2)
print(2**3)

x=2
x=x+3
print(x)
x+=3
print(x)
x-=3
print(x)
x*=3
print(x)

print("-"*15+"3.Rounding"+"-"*15)
import math
#Rounding
print(abs(2-10))

#floor():
#
price=36.54979
print(round(price)) #round: handy in data analysis to cleane up numbers for reports or save spaces

print(round(price,2))
print(round(price,1))
print(math.floor(price))
print(math.ceil(price))
print(math.trunc(price))
print(int(price))


print("-"*15+"4.Advance Math"+"-"*15)
#baad me

print("-"*15+"5.Random"+"-"*15)

import random 
#random() : returns a rendom float between 00 and 10
#randint():gets a rendom whole number from start to end (both included)
print(random.random())  
print(random.randint(1,6))
#use case: use it generate test data dummy for like age id or prices
#          random Sampling - picking a smaller random part of a huge dataset


print("-"*15+"5.Validation"+"-"*15)
x=67.0
print(x.is_integer())
x=67.023
print(x.is_integer())


x=70
print(isinstance(x,int))  #isinstance(): checks if a value belong to a certain data type
print(isinstance(x,float))
#!/usr/bin/env python
# coding: utf-8

# In[2]:


A=input("Enter string of 10 chars")
A


# In[3]:


B=input("Enter string of 5 chars")
B


# In[4]:


A.upper()


# In[5]:


x=int(input("ENter first number"))
x


# In[6]:


y=int(input("ENter second number"))
y


# In[21]:


x=int(input("Enter first number "))
y=int(input("Enter second number "))
z=int(input("Now select your option for calculation \nEnter 1 for add \nEnter 2 for Subtract \nEnter 3 for multiplication \nEnter 4 for Division \nEnter 5 for power \n"))
if z==1:
   print(x+y)
elif z==2:
    if x>y:
       print(x-y)
    else:
        print(y-x)
elif z==3:
    print(x*y)
elif z==4:
    if x>y:
        print(x/y)
    else:
        print(y/x)
elif z==5:
    a=int(input("Enter 1 for x^y \nEnter 2 for y^x "))
    if a==1:
        print(x**y) ## using ** for power as ^ for binary operation what I could understand.
    elif a==2:
        print(y**x)
    else:
        print("Enter Valid Option")
else:
    print("Enter Valid Option")
    


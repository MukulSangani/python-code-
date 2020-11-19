#!/usr/bin/env python
# coding: utf-8

# In[2]:


# Data Structures with Python
a=4
print(type(a))
b=30.6
print(type(b))
c=10+2j
print(type(c))


# In[3]:


print(int(-2.8))
print(float(5))


# In[4]:


import math


# In[8]:


print(math.sqrt(4))
print(math.floor(-10.7))
print(math.pow(2,3))
print(round(math.pi,2))
print(math.pi)
print(math.factorial(6))


# In[16]:


import random as rn
#rn.seed(10)
print(rn.random())
print(rn.randrange(50,100))
print(rn.uniform(50.5,100))
x=[1,2,3,4,5]
print(rn.choice(x))


# In[18]:


my_string="Hello Word!"
print(my_string)

print()
"""this is a comment"""

my_string="""Pyhton is a programming language.
Pyhton is interesting.
this is it."""
print(my_string)
my_string="Python is  a programming language.\nthis is it."
print(my_string)


# In[21]:


#slicing
my_string="Python is a programming language.Python is interesting."
print(my_string[0])
print(my_string[-3])
#[inclusive:exclusive]
print(my_string[3:10])
print(my_string[:25])
print(my_string[25:])
print(my_string[:])
#print(my_string[100])
print(len(my_string))


# In[24]:


#my_string[3]="B"  #Strings ae immutable
del my_string
#print(my_string)


# # Lists

# In[25]:


#Pyhton Lists
mylist1=[1,2,3,4,2]
mylist2=[1,4,"pyhton",4.5]
print(mylist1)
print(mylist2)
print(type(mylist2))


# In[28]:


# use a slicing operator
a=[10,20,30,40,50,60,70]
print(a[2])
print(a[0:3])
print(a[5:])
print(a[:])
print(len(a))


# In[29]:


a[3]=55.0
print(a)   # list are mutable


# In[30]:


x=list(range(0,11))
print(x)


# In[34]:


b=["spam",2.0,5,[10,"raj"]]  # nested list
print(b[3][1])
print(b[3][1][1])


# In[35]:


# appending multiple elemets
my_list=[1,3,6,9]
my_new_list=[4,5,6,7,8]
my_list.append("mukul")      # to add single element
my_list.extend(my_new_list)  # to add multiple elements
print(my_list)


# In[36]:


my_list.remove(4)
print(my_list)

print(my_list)
del my_list[1:3]
my_list


# # Tuples

# In[37]:


a=(5,"python",10+2j,5)
print(a)
print(type(a))
print(a[0])


# In[49]:


n_tuple=("mouse",[8,4,5],(1,2,3),8)
print(n_tuple)
print(n_tuple[1][2])
n_tuple[1][1]=0

#del n_tuple
print(n_tuple)


# # Sets

# In[52]:


my_set={1,2,3,5,7,6,4,3,2,10,38,72,16}
print(my_set)

my_set={1,1.0,"Hello","Manish",(1,2,4)}
print(my_set)
#my_set[0]


# In[53]:


## Adding elements
my_set={1,3}
print(my_set)
my_set.add(8)
print(my_set)
my_set.update([6,8,1,4,2])
print(my_set)
# deleting elements
my_set.remove(6)
print(my_set)


# In[55]:


# Union and Intersection
A=[1,2,3,5,6]
B=[4,7,5,8,9]

setA=set(A)
setB=set(B)

print(setA|setB)
print(setA.union(setB))

print(setA & setB)
print(setA.intersection(setB))

print(setA-setB)
print(setA.difference(setB))


# # Dictionaries

# In[59]:


# creatinng a dictionary
my_d1={1:"A",2:"B"}
print(my_d1)

my_d2={'name':["John","Mike","Sam"],"ID":[2,4,3]}
print(my_d2["name"][1])

print(my_d2["name"])

my_d=dict([("fruit","apple"),(2,"mango"),("fruit","mango")])
print(my_d)


# In[61]:


my_d={"Name":"Michiel","age":27}
print(my_d)
my_d["age"]=21
print(my_d)

my_d["address"]="Chicago"
print(my_d)


# In[63]:


my_d.values()

my_d.keys()


# In[64]:


my_d.values()


# In[67]:


a=[1,2,3,4,5,60]
b=(6,7,8,9,10)

c=dict(zip(a,b))  # zip function are use make pairs from both datasets
print(c)

d=list(zip(a,b))
print(d)

e=tuple(zip(a,b))
print(e)


# In[ ]:





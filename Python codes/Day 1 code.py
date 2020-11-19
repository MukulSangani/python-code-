#!/usr/bin/env python
# coding: utf-8

# In[1]:


a=10
b=20
a=5; d=10
b,c=3.2,"Hello"
x=y=z="World"

print(c)
print()
print("value  of b",b)
print("value of a =\n",a)
print(b,c)
print(b,c,sep=",")
c
print(a)


# In[2]:


# Division operation in Python
print(1/3)
print(1//3)# floored division
print(7%3)
print(round(1/3,2))


# In[3]:


a=5
b=3.2
print(type(b))
print(a+b)
a="5"
b="3.2"
print(a+b)
print(type(b))


# In[5]:


# user input
name=input("Enter your name: ")
print("Hello",name)


# In[6]:


x=3
y=5

if x<y:
    print("This is the first block")
    print("x is less than y")
elif x>y:
    print("x is greater than y")
else:
    print("x and y are equal")
print("Done")


# if x==y:
#     print("x and y are equal")
# else:
#     if x>y:
#         print("x is less than y ")
#     else:
#         print("x is greater than y")
#         
# print("Done")
#     

# In[10]:


if x==y: 
    print("x and y are equal") 
else: 
    if x>y: 
        print("x is less than y ") 
    else:
        print("x is greater than y")
                
print("Done")


# In[13]:


x=5;y=8
if (x>7 and y>7)or x!=y:
    print("x is a single-digit positive number.")



# In[16]:


#user defined function
def square(a):
    print("value of a is",a)
    return a*a


#square(10)
value=float(input("Enter the value :"))
square(value)


# In[17]:


# defining a fuction and then call 
def hi():
    print("Hello User!")
hi()


# In[18]:


count=0
while(count<5):
    print(count)
    # count+=1
    count=count+1
else:
    print("count value is reached",count)


# In[25]:


count=0
while(count<6):
    print(count)
    if count==4:
        break
    count+=1


# In[29]:


friends=["A","B","C",3.6]
for f in friends[:3]:
    print("Happy New Year,",f)


# In[33]:


a=100
while(a>=70):
    print(a)
    a-=1


# In[41]:


x=0
while(x<=120):
    if x>25:
        print(x)
    x+=1


# In[ ]:





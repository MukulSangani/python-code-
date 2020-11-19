a=10
b=20
a=5;d=10
b,c=3.2,"Hello"
x=y=z="WOrld"

print(c)
print()
print("Value of a=\n",a)
print("Value of b=",b)
print(b,c)
print(b,c,sep=",")
c
print(a)

#Division operstion in python
print(1/3)
print(1//3) #flored division
print(7%3)
print(round(1/3,2))

a=5
b=3.2
print(type(b))
print(a+b)
a="5"
b="3.2"
print(a+b)
print(type(b))

#User input
name=input("Enter ur name:")
print("Hello",name)

#if else(syntax)
x=3
y=5
if x<y:
    print("This is the first block")
    print("x is greater than y")
elif x>y:
    print("x is greater than y")
else:
    print("x and y are equal")
print("Done")

#nested if else(syntax)########
if x==y:
    print("x and y are equal")
else:
    if x < y:
        print("x is smaller than y")
    else:
        print("x is greater than y")
print("done")

#no output######
x=5;y=8

if x>7 and y>7:
               print("x is single digit positive num")
               print("done")

#user defined fuction######
def square(a):
    print("value is = ",a)
    return a*a
#square(10)      
value=float(input("enter a number:"))
square(value)

def hi():
    print("Hello User!")
hi()

#whie loop#####
count=0
while(count<5):
    print(count)
    #count +=1
    count=count+1
else:
    print("count value reached",count)

count=100
while(count>=70):
    print(count)
    count=count-1
else:
    print("count value readched",count)

#For loop#####
friends = ["A","B","C",3.6]
for f in friends:
    print("Happy Diwali",f)


######Data Structure in PYTHON#######

#1] Numbers
print(int(-2.8))
print(float(5))

#library
import math
print(math.sqrt(4))
print(math.floor(10.7))
print(math.pow(2,3))
print(round(math.pi,2))
print(math.pi)
print(math.factorial(6))

import random as rn  
#rn.seed(10)
print(rn.random())
print(rn.randrange(50,100))
print(rn.uniform(50.5,100))
x=[1,2,3,4,5]
print(rn.choice(x))

#2] String
my_string="hello world"
print(my_string)

my_string="Python is a programming language.\nthis is it."
print(my_string)

#slicing
my_string="Python is a programming language.Python is intresting."
print(my_string[0])
print(my_string[-3])
#[inclusive:exclusive]
print(my_string[3:10])
print(my_string[:25])
print(my_string[25:])
print(my_string[:])
print(len(my_string))

#3] Lists
#Python list
mylist=[1,3,5,4,2]
mylist2=[1,4.2,"python",4.2]
print(mylist)
print(mylist2)
print(type(mylist2))

#use of slicing operator
a=[10,20,30,40,50,60,70,80]
print(a[2])
print(a[0:3])
print(a[5:])

a[3]=55.0
print(a)

x=list(range(0,11))
print(x)

b=["spam",2.0,5,[10,"raj"]]  #nested list#
print(b[1],b[3][1])

#appending multiple elements#
my_list=[1,3,6,9]
my_new_list=[4,5,6,7,8]
my_list.extend(my_new_list)
my_list.append("nikita")
print(my_list)

#4] Tuples #read only data structure #immutable property#
a=(5,"python",10+2j,5)
print(a)
print(type(a))
print(a[0])

#nested tuple#
n_tuple=("mouse",[8,4,5],(1,2,3),8)
print(n_tuple[1][2])
#n_tuple[2][1]=0  #cannot be modified therefore valu cannot be assign or modified#
del n_tuple

#5] Sets#

my_set={1,2,3,5,7,6,4,3,2,10,38,72,16}
print(my_set)
my_set={1,1.0,"hello","manish",(1,2,4)}
print(my_set)

#nested sets#
#error beacuse dont suppory indexing#
my_set[0]
print(my_set[0])
A=[1,2,3,4,5,9]
B=[4,5,6,7,8,10]
setA =set(A)
setB =set(B)
print(setA|setB)
print(setA.union(setB))
print(setA & setB)
print(setA.intersection(setB))

print(setA-setB)
print(setB.difference(setA))

#6] Dictionaries
#creating a dictionary
my_d1={1:"A",2:"B"}
print(my_d1)
my_d2={"name":["John","Shubham","Mayekar"],"ID":[2,4,3]}
print(my_d2)
print(my_d2["name"])

my_d={"Name":"Shubham","age":21}
my_d["age"]=12
print(my_d)
my_d["address"]="Mumbai"
print(my_d)
my_d.values()
my_d.keys()

A=[1,2,3,4,5]
B=(6,7,8,9,10)
c=dict(zip(A,B))
c #print c

####NUMPY#######
import numpy as np
np.__version__

a=np.array([1,2,3])
print(a)
print(type(a))

a=np.array([(1,2,3),(4,5,6)]) #list of tuples
print(a)
print(a.ndim) #dimension of array
print(a.shape) #2Row and 3Colmns

#indexing and slicing
a=np.array([(1,2,3,4),(3,4,5,6),(8,9,10,11)])
print(a)
print(a[0,2])
print(a[:,2])
print()
print(a[0:2,])
#aggerate functions
print(a.min())
print(a.max())
print(a.sum())
print(a.mean())
print(np.min(a))
#math function
print(np.sqrt(a))
print(np.std(a))
print(np.log(a))
b=np.sqrt(a)
print(b.round(2))


x=np.array([(1,3),(3,4)])
y=np.array([(5,6),(3,4)])
print(x)
print(y)
print(x+y)#np.add()
print(x-y)#np.subtract
print(x*y)#np.multiply
print(x/y)#np.divide
print(x%y)#np.remainder
print(x@y) #print(np.dot(x,y))


































































































#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import numpy as np
np.__version__


# In[ ]:


a=np.array([1,2,3])
print(a)
print(type(a))


# In[ ]:


a=np.array([(1,2,3),(4,5,6)])
print(a)
print(a.ndim)
print(a.shape)


# In[ ]:


# Indexing and slicing
a=np.array([(1,2,3,4),(3,4,5,6),(8,9,7,10)])
print(a)
print(a[0,2])
print(a.ndim)
print(a.shape)
print(a[:,2])
print()
print(a[0:2,])


# In[ ]:


#a=np.linspace(1,10,5)
#print(a)
a=np.arange(0,26,5)
print(a)

a=np.random.random((3,4))
print(a)

a=np.random.random_integers(50,100,(3,4))
print(a)
a=np.random.randint(50,100,(3,4))
print(a)


# In[ ]:


np.random.uniform(50.5,100,(2,3))


# In[ ]:


# aggregation function 
a=np.array([(8,9),(10,11),(12,13)])
print(a.min())
print(a.max())
print(a.sum())
print(a.mean())
print(np.mean(a))


# In[ ]:


# math function 
a=np.array([(1,0,3),(3,4,5)])
print(np.sqrt(a).round(2))
print(np.std(a).round(2))
print(np.square(a))
print(np.log(a))

b=np.sqrt(a)
print(b.round(2))


# In[ ]:


x=np.array([(1,2),(3,4)])
y=np.array([(5,6),(3,4)])
print(x)
print(y)
print(x+y)
print(x-y)
print(x*y)
print(x%y)
print(x@y)
# print(np.dot(x,y))
# print(np.add(x,y))
# print(np.multiply(x,y))
# print(np.divide(x,y))
# print(np.substract(x,y))
# print(np.remainder(x,y))


# In[ ]:


a=np.array([(1,2),(2,4)])
a[0,1]=4
print(a)
print(np.log10(a).round(2))


# In[ ]:


my_array=np.genfromtxt("E:\data\data in array.txt",skip_header=1,delimiter=","
                       ,filling_values=0,unpack=True,dtype=np.int)    # default in dtype=np.float
                        #
print(my_array)


# In[ ]:


my_array=np.genfromtxt("E:\data\data in array.txt",skip_header=1,delimiter=","
                       ,filling_values=0,unpack=True,dtype=np.int)    # default in dtype=np.float
print(my_array)


# In[ ]:


my_array=np.genfromtxt("E:\data\data aray.txt",skip_header=1,delimiter=","
                       ,filling_values=0,unpack=False,dtype=np.str)    # default in dtype=np.float
print(my_array)


# In[ ]:


import pandas as pd


# # Series

# In[ ]:


import numpy as np
data=np.array([101,102,103,104])
s=pd.Series(data)
print(s)
print()

print(s[1])
s[1]=100
s[6]=105
print(s)


# In[ ]:


data=[101,102,103,104]
t=pd.Series(data,index=["a","b","c","d"])
print(t)
print(t["b"])
print(t[1])


# In[ ]:


arr=np.arange(1001,1005,1)
s=pd.Series(data,index=arr)
print(s)
print(s[1002])
#print(s[1])


# In[ ]:


data={"a":0.,"b":1.,"c":2.}
s=pd.Series(data)
print(s)

print(s["a"])
print(s)
print(s[-2])   #  it also allows negative indexing 

data={1:2.0,2:3.0,3:2.5}
s=pd.Series(data)
print(s)
print(s[1:])


# # Data Frames

# In[ ]:


data=[["Mike",40],["Sam",46,],["Joe",36]]
df=pd.DataFrame(data,columns=["Names","Age"])
df

#df.columns=["Names","Age"]   #separately labeing columns names
#print(df)


# In[71]:


# indexed data frame from dict
data={"Names":["Mike","Sam","Clark"],"Age":[20,25,23]}
df=pd.DataFrame(data)
print(df)
df

df=pd.DataFrame(data,index=["rank 1","rank 2","rank 3"])
#print(df)
df


# In[73]:


df["Names"] # shortcut way to call the names from the dataframe


# In[74]:


df[["Names","Age"]]  # shortcut way to call the whole dataframe or some multiple columns data from the dataframe


# In[75]:


df["Address"]=["Mumbai","Pune","Bangalore"]
df


# In[76]:


df.columns


# In[77]:


df=df[["Names","Address","Age"]]        # realigning the columns of the dataframe
df     


# In[78]:


df["Newcol"]=[5,10,16]



df["Revised_col"]=df["Newcol"]*2
#print(df)
df


# In[79]:


# deleting a column
del df["Newcol"]
#print(df)
df


# In[80]:


df=df.drop("rank 1")                      #axis=0---->obs
df=df.drop("Revised_col",axis=1)          #axis=1---->var
#print(df)
df


# In[83]:



# accessing data ekements using indexes and labels
#df.loc[inclusive:inclusive]  #location  with the help of accessing labels
#df.iloc[inclusive:exclusive]       # iloc is used with the help of index numbers
print(df.loc["rank 2"])
print()
print(df.loc["rank 2":"rank 3"])
print()
print(df.iloc[0:1])
print()
#print(df)

print(df.loc["rank 2":"rank 3",["Address","Age"]])
print()
print(df.iloc[:,[1,2]])


# In[ ]:





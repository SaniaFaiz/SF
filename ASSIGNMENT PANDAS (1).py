#!/usr/bin/env python
# coding: utf-8

# In[19]:


import pandas as pd


# In[20]:


df = pd.read_csv("G.outcome.csv")

df.head(16)


# In[21]:


df.tail()


# In[22]:


df.shape


# In[23]:


df.describe()


# In[24]:


df.boxplot()


# In[25]:


df.hist()


# # COLUMNS METHOD

# In[26]:


for col in df.columns: 
    print(col)


# In[27]:


df.rename(columns={"name" : "NAMES"})


# # Data information¶

# In[28]:


print(df.info())


# In[29]:


df.isnull()

#IF THE VALUES ARE NULL IN THE DATASET IT WILL RETURN TRUE OTHERWISE FALSE


# In[30]:


df.isnull().sum()


# # To replace wrong data for larger data sets, e.g. set boundaries for legal values, and replace any values that are outside of the boundaries.
# 

# In[31]:


for x in df.index:
  if df.loc[x, "Acceptance Rate"] > 25:
    df.loc[x, "Acceptance Rate"] = 9
    
print(df.head(21))


# In[32]:


print(df.duplicated())
print(df.head(8))


# In[33]:


#The corr() method calculates the relationship between each column in your data set.

df.corr()
df.head(8)


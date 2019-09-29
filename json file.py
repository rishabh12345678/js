#!/usr/bin/env python
# coding: utf-8

# In[2]:


import json as js
import pandas as pd
import numpy as np
from pandas.io.json import json_normalize


# In[3]:


d = js.loads(open('data.json','r').read())
type(d)


# In[4]:


df = pd.DataFrame.from_dict((json_normalize(d)))


# In[13]:


df


# In[6]:


with open('data.json','r') as gf:
    data = json.load(gf)
    print(data)


# In[14]:


np = pd.DataFrame(json_normalize(data))
np


# In[11]:


df = pd.DataFrame(np)
df


# In[ ]:





#!/usr/bin/env python
# coding: utf-8

# In[30]:


record1

import pandas as pd

record1 = pd.Series({
    "Name": "Trevin",
    "Age": '21',
    "School": "St. Joseph's College",
    "University": "University of Colombo"
})
record1


# In[31]:


record2 = pd.Series({
    "Name": "Seniya",
    "Age": '23',
    "School": "St. Joseph's College",
    "University": "SLIIT"
})

record2


# In[32]:


record3 = pd.Series({
    "Name": "Kavishka",
    "Age": '26',
    "School": "St. Joseph's College",
    "University": "NSBM"
})
record3


# In[33]:


df=pd.DataFrame([record1,record2,record3],index=['Youngest','Middle','Eldest'])
df


# In[34]:




# In[ ]:





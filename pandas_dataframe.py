#!/usr/bin/env python
# coding: utf-8

# In[1]:


from pandas import DataFrame


# In[2]:


data = {'Name': ['John', 'Renju', 'Helen', 'Tinto'],
       'Age': [30, 35, 40, 45],
       'Salary': [15000, 20000, 25000, 30000]}

frame = DataFrame(data=data)

frame


# In[3]:


new_frame = DataFrame(data=data, columns=['Name', 'Salary', 'Age'])

new_frame


# In[4]:


# ADD AN EMPTY COLUMN
new_frame1 = DataFrame(data=data, columns=['Name', 'Profile', 'Salary', 'Age'])

new_frame1


# In[5]:


# COLUMN BASE DATA GET
new_frame1['Salary']


# In[6]:


# ROW BASE DATA GET

# new_frame1.ix[2]      # ix[]: SOME TIMES NOT WORKING, SO USE loc
new_frame1.loc[2]


# In[7]:


# ADD VALUE TO NaN
new_frame1['Profile'] = "Engineer"

new_frame1


# In[8]:


# ADD NEW COLUMN WITH VALUE
new_frame1['Education'] = "BTech"

new_frame1


# In[9]:


# CONVERT HORIZONTALLY/VERTICALLY
new_frame1.T


# In[ ]:





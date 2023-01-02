#!/usr/bin/env python
# coding: utf-8

# In[1]:


from pandas import Series

se = Series([1,3,4,7,9,2,6,5,0,8])


# In[2]:


se


# In[3]:


# TAKE 4TH POSITION VALUE
se[3]


# In[4]:


# SERIES WITH USED DEFIEND INDEXES
se1 = Series([10, 20, 40, 60, 30, 50], index=['a', 'b', 'c', 'd', 'e', 'f'])

se1


# In[5]:


se1['d']


# In[6]:


# DICT TO SERIES
salary = {'john': 15000, 'raju': 20000, 'helen': 25000, 'renju': 30000}

se_salary = Series(salary)

se_salary


# In[7]:


se_salary['renju']


# In[ ]:





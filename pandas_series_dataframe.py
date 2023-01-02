#!/usr/bin/env python
# coding: utf-8

# In[1]:


from pandas import Series
from pandas import DataFrame


# In[2]:


se = Series([100, 200, 400, 600, 300, 500, 700], index=['F', 'C', 'G', 'A', 'E', 'D', 'B'])

se


# In[3]:


# RE-INDEXING 
se = se.reindex(['A', 'B', 'C', 'D', 'E', 'F', 'G'])

se


# In[4]:


data = {'Name': ['John', 'Renju', 'Helen', 'Tinto', 'Mike', 'Sam', 'Peter'],
       'Age': [30, 35, 40, 45, 50, 55, 60],
       'Salary': [15000, 20000, 25000, 30000, 35000, 40000, 45000]}

new_frame = DataFrame(data=data, columns=['Name', 'Salary', 'Age'])

new_frame['Profile'] = "Engineer"

new_frame


# In[5]:


# RE-INDEX DataFrame
new_frame = new_frame.reindex([2, 5, 0, 3, 1, 6, 4])

new_frame


# In[6]:


# MATH OPERATION WITH SERIESES
series1 = Series([5, 10, 15, 20, 25, 30, 35, 40, 45, 50])
series2 = Series([100, 200, 300, 400, 500, 600, 700, 800, 900, 1000, 1100])

series1 + series2


# In[7]:


data1 = {'Speed': [100, 200, 300, 400, 500], 
        'Temp': [20, 30, 40, 50, 60]}

frame1 = DataFrame(data1)

data2 = {'Speed': [100, 200, 300, 400, 500], 
        'Temp': [20, 30, 40, 50, 60],
        'Humi': [50, 60, 70, 80, 90]}

frame2 = DataFrame(data2)

print(frame1)
print('_______________________')
print(frame2)


# In[8]:


frame1 + frame2


# In[9]:


series3 = Series([5, 10, 15], index=['Speed', 'Temp', 'Humi'])

series3


# In[10]:


frame2 - series3


# In[ ]:





# In[11]:


se1 = Series([20, 40, 10, 60, 80, 30, 50, 70], index=[4, 7, 3, 5, 2, 6, 1, 8])

se1.sort_index()


# In[12]:


se1.sort_values()


# In[13]:


# 2 frame set, 2 series set  add sub

series4 = Series([20, 40, 10, 60, 80], index=['Sub1', 'Sub2', 'Sub3', 'Sub4', 'Sub5'])
series5 = Series([5, 30, 15, 50, 70], index=['Sub1', 'Sub2', 'Sub3', 'Sub4', 'Sub5'])

series4 + series5


# In[14]:


data3 = {'Sub1': [50, 60, 70, 80, 90], 
        'Sub2': [20, 30, 40, 50, 60],
        'Sub3': [98, 87, 76, 65, 54],
        'Sub4': [25, 35, 45, 55, 65], 
        'Sub5': [29, 37, 43, 51, 32]}

frame3 = DataFrame(data3)

data4 = {'Sub1': [50, 60, 70, 80, 90], 
        'Sub2': [20, 30, 40, 50, 60],
        'Sub3': [98, 87, 76, 65, 54],
        'Sub4': [25, 35, 45, 55, 65], 
        'Sub5': [29, 37, 43, 51, 32],
        'Sub6': [29, 37, 43, 51, 32]}

frame4 = DataFrame(data4)


# In[15]:


frame3 + series4 + series5 + frame4


# In[16]:


frame4 - series4 - frame3 - series5


# In[17]:


frame4 + (series4 - frame3) + series5


# In[ ]:





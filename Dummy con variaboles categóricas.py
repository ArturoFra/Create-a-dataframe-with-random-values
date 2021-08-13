#!/usr/bin/env python
# coding: utf-8

# # Agregación de datos por categoría 

# In[1]:


import numpy as np
import pandas as pd


# In[49]:


gender = ["Female", 'Male']
income=["Poor","Middle Class","Rich"]


# In[50]:


n=50
gender_data=[]
income_data=[]
for i in range (0, 50):
    gender_data.append(np.random.choice(gender))
    income_data.append(np.random.choice(income))
    


# In[51]:


gender_data[1:10]


# In[52]:


height=160 + 20*np.random.randn(n) 
weight=65 + 25*np.random.randn(n)
age=30 + 12*np.random.randn(n)
income=18000 + 3500*np.random.randn(n)


# In[53]:


data = pd.DataFrame(
    {
            "Gender": gender_data,
            "Economic Status": income_data,
            "Height": height,
            "Weight": weight,
            "Age" : age,
            "Income": income
        
    }

)


# In[54]:


data.head()


# In[ ]:





# # Agrupación de datos

# In[55]:


grouped_gender=data.groupby("Gender")


# In[56]:


grouped_gender.groups


# In[57]:


for names, groups in grouped_gender:
    print(names)
    print(groups)
    


# In[58]:


grouped_gender.get_group("Female")


# In[60]:


double_group=data.groupby(["Gender", "Economic Status"])


# In[61]:


len(double_group)


# In[63]:


for names, groups in double_group:
    print(names)
    print(groups)


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





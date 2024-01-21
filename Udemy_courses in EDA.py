#!/usr/bin/env python
# coding: utf-8

# ## EDA in Udemy courses

# ## importing the Libraries

# In[1]:


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


# ### Read the dataset

# In[2]:


df =pd.read_csv((r"C:\Users\bhara\Downloads\udemy_courses.csv")


# ### get some informations about dataset

# In[3]:


df.head()


# In[5]:


df.sample(5)


# In[6]:


df.info()


# #### ----> there is no null data in every column

# In[7]:


df.describe()


# ## date cleaning 

# ### - null data :

# In[9]:


df.isnull().sum()


# ### ---> there is no null data

# ## - delete unnecessary columns :

# In[10]:


df.drop('course_id',axis=1,inplace=True)


# In[11]:


df.drop('url',axis=1,inplace=True)


# In[12]:


df.head()


# ### unnecessary column removed 

# ## validate columns data types

# In[13]:


df['published_timestamp']=pd.to_datetime(df['published_timestamp'])


# In[14]:


df.head()


# ### ---> all data types is valid 

# ## Remove duplicated rows 

# In[15]:


#showdu plicates
df[df.duplicated()]


# In[16]:


#remove duplicates
df.drop_duplicates(inplace=True)


# ## visualize data and get conclusions

# In[23]:


plt.title("paid courses and free courses")
sns.countplot('is_paid',data=df)


# In[18]:


df['is_paid'].value_counts()


# ### -->most courses is paid

# In[24]:


plt.title(" courses subjects")
sns.countplot('subject',data=df)


# In[21]:


df['subject'].value_counts()


# ### --> web devolopment and Business Finance is the most common cources

# In[25]:


plt.title("courses levels")
sns.countplot('level',data=df)


# ### --> most cources is in (all levels)

# -------
# ## Relation between price and number of subscribers

# In[27]:


plt.title('price vs num_subscribers')
sns.regplot(x='price',y='num_subscribers',data=df)


# ### --> there is no relation between the price and number of subscribers

# -------
# ## Relation between price and content duration

# In[29]:


plt.title('price vs content_duration')
sns.regplot(x='price',y='content_duration',data=df)


# ### --> price increased by increasing of content duration

# -------
# ## Relation between content duration and number if subscribers

# In[30]:


plt.title('content_duration vs num_subscribers')
sns.regplot(x='content_duration',y='num_subscribers',data=df)


# ### --> there is more number of subscribers by increasing content duration

# -------
# ## Relation between content duration and number of reviews

# In[31]:


plt.title('content_duration vs num_reviews')
sns.regplot(x='content_duration',y='num_reviews',data=df)


# ### --> there is more number of reviews by increasing content duration

# In[ ]:





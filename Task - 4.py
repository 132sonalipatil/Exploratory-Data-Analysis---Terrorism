#!/usr/bin/env python
# coding: utf-8

# # NAME - SONALI PATIL
# # TASK 4 - Exploratory Data Analysis - Terrorism (level - Intermediate)
# 

# # Step 1 Importing all labiraries

# In[46]:


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
get_ipython().run_line_magic('matplotlib', 'inline')
import seaborn as sns
import matplotlib as mpl


# # Step 2 Load the data set

# In[2]:


df=pd.read_csv('D:\\globalterrorismdb_0718dist.csv')
print('Data is loaded successfully!!!!!!')


# In[3]:


df.head()# Printing first five row


# In[4]:


df.tail()#Printing last five row


# In[5]:


df.info()


# In[6]:


df.shape


# In[7]:


df.columns


# In[8]:


df.describe()


# In[55]:


df.rename(columns={'iyear':'Year','imonth':'Month','iday':'Day','country_txt':'Country','region':'Region','provstate':'state'
                    ,'city':'City','latitude':'Latitude','longitude':'Longitude','location':'Location','summary':'Summary'
                    ,'attacktype1':'Attack Type','targtype1':'Target Type','gname':'Group Nmae','motive':'Motive'
                    ,'weaptype1_txt':'Weapon Type','nkill':'Killed','nwound':'Wounded','addnotes':'Add Notes'} ,inplace=True)
df.head()


# In[11]:


df.info()


# In[12]:


df.shape


# In[13]:


df.isnull().sum() # Cheacking null values


# In[14]:


df['Killed']=df['Killed'].fillna(0)
df['Wounded']=df['Wounded'].fillna(0)
df['Casuality']=df['Killed']+df['Wounded']


# In[15]:


df.nunique()


# In[16]:


df.describe()


# # Observation
# 
# ### Maximun number of people killed in an event were : 1570
# ### Maximun number of people Wounded in an event were: 8191
# ### Maximun number of total Casualities in an event : 9574
# 

# # Step 3 - Data Visualization
# 
# ## 1 Year Wise Attack
# 
# #### Number of attacks in each year

# In[17]:


attacks=df["Year"].value_counts(dropna=False).sort_index().to_frame().reset_index().rename(columns={"index":"Year","Year":"Attacks"}).set_index("Year")   
attacks.head()


# In[21]:


## Plotting the graph


attacks.plot(kind='bar',color='darkblue',figsize=(15,10),fontsize=13 )
plt.title('Timeline of Attacks in each year',fontsize=15)
plt.xlabel("Years",fontsize=15,fontstyle='oblique')
plt.ylabel('Numbers of attacks in each years',fontsize=15,fontstyle='oblique')
plt.grid()
plt.show()


# # 2 Year Wise Casuality
# ### Number of casualities in each year

# In[22]:


yc=df[["Year","Casuality"]].groupby("Year").sum()
yc.head()


# In[27]:


## Plotting the graph


yc.plot(kind='bar',color='darkblue',figsize=(15,10),fontsize=13 )
plt.title('Timeline of Casuality in each year',fontsize=15)
plt.xlabel("Years",fontsize=15,fontstyle='oblique')
plt.ylabel('Numbers of casuality in each years',fontsize=15,fontstyle='oblique')
plt.grid()
plt.legend(loc='upper left')
plt.show()


# # 3 Year Wise Killed 
# ### Number of killed in each year

# In[29]:


yk=df[["Year","Killed"]].groupby("Year").sum()
yk.head()


# In[39]:


# Plotting The graph
yk.plot(kind='bar',color='darkblue',figsize=(15,10),fontsize=15)
plt.title("Time-line of Killed people in each year",fontsize=15)
plt.xlabel('Years',fontsize=15,fontstyle='oblique')
plt.ylabel('Number of killed people in each year',fontstyle='oblique',fontsize=15)
plt.legend(loc='upper left')
plt.show()


# # 4 Year wise Wounded
# ### Number of people wounded ineach year

# In[35]:


yw=df[["Year","Wounded"]].groupby("Year").sum()
yw.head()


# In[60]:


# Plotting the graph

yw.plot(kind='bar',color='darkblue',figsize=(15,10),fontsize=15)
plt.title("Time-line of wounded people in each year",fontsize=15)
plt.xlabel('Years',fontsize=15,fontstyle='oblique')
plt.ylabel('Number of killed people in each year',fontstyle='oblique',fontsize=15)
plt.legend(loc='upper left')
plt.show()


# # 5 Region Wise Attacks

# In[42]:


reg=pd.crosstab(df.Year,df.Region)
reg.head()


# In[47]:


## Plotting the graph

reg.plot(kind="area",stacked=False,alpha=0.5,figsize=(20,10))
plt.title("Region-wise attacks",fontsize=15)
plt.xlabel('Years',fontsize=15,fontstyle='oblique')
plt.ylabel('Number of attacks in each year',fontstyle='oblique',fontsize=15)
plt.legend(loc='upper left')
plt.show()


# In[58]:


regt=reg.transpose()
regt["Total"]=regt.sum(axis=1)
ra=regt["Total"].sort_values(ascending=False)
ra


# In[59]:


ra.plot(kind="bar",figsize=(12,6))
plt.title("Total number of attacks from1970-2017")
plt.xlabel('year')
plt.ylabel('Total number of attack')
plt.show()


# In[ ]:





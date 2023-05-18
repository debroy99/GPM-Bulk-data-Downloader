#!/usr/bin/env python
# coding: utf-8

# In[3]:


import numpy as np
import pandas as pd
import xarray as xr
from data_downloader import downloader


# In[4]:


netrc = downloader.Netrc()
netrc.add('urs.earthdata.nasa.gov','debjyoti_earthdata99','Debjyoti@1999')
print(netrc.hosts)


# In[82]:


ds=pd.read_csv('E:\Debjyoti\Project Work\GPM Data\Subsets\subset_GPM_3IMERGHH_06_20230503_104114_.txt', header=None, sep='/n')[0]


# In[83]:


ds


# In[28]:


#single data downloaded at a time
for i in range(19,len(ds)):
    url=ds[i]
    downloader.download_data(url, folder=None, file_name=None,
                  client=None, engine='requests',
                  follow_redirects=True, retry=0,
                  authorize_from_browser=False)


# In[97]:


#data downloader using multiple processors #Working
downloader.mp_download_datas(ds, folder=None,file_names=None, ncore=None, desc='',
                       follow_redirects=True, retry=20, engine='requests', authorize_from_browser=True)


# In[98]:


URLS=ds[40:50]
URLS


# In[99]:


#working code bulk data downloader
downloader.download_datas(URLS, folder=None, file_names=None, engine='requests', authorize_from_browser=False)


# In[9]:


#Not working Download files simultaneously with asynchronous mode
downloader.async_download_datas(ds, folder=None, authorize_from_browser=False, file_names=None, limit=30, desc='',retry=0)


# In[ ]:





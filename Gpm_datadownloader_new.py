#!/usr/bin/env python
# coding: utf-8
#author= @debroy99

##############################################
import pandas as pd
from data_downloader import downloader
################################################
#creating netrc file

netrc = downloader.Netrc()
netrc.add('urs.earthdata.nasa.gov','User ID','Password')
print(netrc.hosts)
#####################################################################################
ds=pd.read_csv('E:\Debjyoti\Project Work\GPM Data\Subsets\subset_GPM_3IMERGHH_06_20230503_104114_.txt', header=None, sep='/n')[0]
ds
#####################################################################################################################################
#single data downloaded at a time
for i in range(0,len(ds)):
    url=ds[i]
    downloader.download_data(url, folder=None, file_name=None,
                  client=None, engine='requests',
                  follow_redirects=True, retry=0,
                  authorize_from_browser=False)
########################################################################################################################
#data downloader using multiple processors #Working
downloader.mp_download_datas(ds, folder=None,file_names=None, ncore=None, desc='',
                       follow_redirects=True, retry=20, engine='requests', authorize_from_browser=True)

################################################################################################################
#selecting the remaining links filed in multiprocessor method

URLS=ds[40:50]
URLS

#working code bulk data downloader
downloader.download_datas(URLS, folder=None, file_names=None, engine='requests', authorize_from_browser=False)
###########################################################################################################
#Not working Download files simultaneously with asynchronous mode
#downloader.async_download_datas(ds, folder=None, authorize_from_browser=False, file_names=None, limit=30, desc='',retry=0)








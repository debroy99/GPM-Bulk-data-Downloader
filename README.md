# GPM-Bulk-data-Downloader
The Code Downloads GPM-IMERG L3 final precipitation datasets.  
Input = subset .txt file downloaded from EarthDATA GES DISC containing the links of the dataset
User ID: EarthDATA user ID
Password: EarthDATA password
first have to create netrc file containg user id and password
read the subset file using pandas
mp_downloader download datas using multiprocessor parallely
if fails rerun the downloading section

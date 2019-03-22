#!/usr/bin/env python3
from bs4 import BeautifulSoup
import requests
import os
import subprocess
source=requests.get('https://www.last.fm/user/lastpriest/library/albums').text
soup=BeautifulSoup(source,'lxml')
albums=soup.find_all('img')
imgUrls = []
for album in albums:
  if '/64s' in album['src']:
    imgUrls.append(album['src'].replace('/64s',''))
subprocess.call("rm -r top50images",shell=True)#create dir
subprocess.call("mkdir top50images",shell=True)#create dir
for url in imgUrls:
  subprocess.call("wget "+ url +" -P ./top50images", shell=True) #download image
subprocess.call("ls top50images/ > listOfFiles.txt",shell=True)

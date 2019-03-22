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
for url in imgUrls:
  print(url)

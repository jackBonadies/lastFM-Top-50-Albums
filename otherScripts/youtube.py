#this script is to 
#1. first divide ones music into obscure + older.  
#2. divide ones music into "what is on youtube" and "what is not"
#3. upload a playlist of songs for each album that is not on youtube
import requests
from bs4 import BeautifulSoup
def existsOnYoutube(artistSong):
  artistQuery = artistSong.replace(' ','+')
  src = requests.get("https://www.youtube.com/results?search_query=" + artistQuery).text
  src = BeautifulSoup(src, 'lxml')
  vidtitles = src.find_all('h3')
  legitVids = []
  for vt in vidtitles:
    if(vt.find('a')==None):
      continue
    if (vt.find('a').get('data-sessionlink') != None):
      legitVids.append(vt.find('a'))
    if(len(legitVids) > 3):
      break
  #4 contestants.  if any match then its on youtube.
  searchTerms = artistSong.split()
  invalids = set()
  for lv in legitVids:
    for term in searchTerms:
      if(lv['title'].upper().find(term.upper()) == -1):
        invalids.add(lv)
  i = len(invalids)
  v = len(legitVids)
  if(i == v):  #it exists
    return 1;
  else:
    return 0;
  
print(existsOnYoutube("Brian eno planet water")) #if u get a 1 then it doesnt exist


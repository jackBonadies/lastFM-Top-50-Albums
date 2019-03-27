#this script is to 
#1. first divide ones music into obscure + older.  
#2. divide ones music into "what is on youtube" and "what is not"
#3. upload a playlist of songs for each album that is not on youtube
import requests
from bs4 import BeautifulSoup
import subprocess
def existsOnYoutube(artistSong):
  artistQuery = artistSong.replace(' ','+')
  src = requests.get("https://www.youtube.com/results?search_query=" + artistQuery).text
  src = BeautifulSoup(src, 'lxml')
  vidtitles = src.find_all('h3')
  legitVids = []
  legitSpans = [] #indices will correspond to legit Vids
  for vt in vidtitles:
    if(vt.find('a')==None):
      continue
    if (vt.find('a').get('data-sessionlink') != None):
      legitVids.append(vt.find('a'))
      legitSpans.append(vt.find('span'))
    if(len(legitVids) > 3): 
      break
  #4 contestants.  if any match then its on youtube.
  searchTerms = artistSong.split()
  invalids = set()
  spanMatches = []
  aMatches = []
  for lv in legitVids:
    thisVid = 1 #until proven otherwise
    for term in searchTerms:
      if(lv['title'].upper().find(term.upper()) == -1):
        invalids.add(lv)
        thisVid = 0
    aMatches.append(thisVid)
  for ls in legitSpans:
    thisVid = 1
    for term in searchTerms:
      if(ls['aria-label'].upper().find(term.upper()) == -1):
        thisVid = 0
    spanMatches.append(thisVid)
  #if there is a single 1 (a 1 means a video that matches everythign then its up.  a 1 can be combined between description and title.  i.e. title OR description
  #but that still doesnt work because its for every single search term.
  i = len(invalids)
  v = len(legitVids)
  if(i == v):  #it exists
    return 1;
  else:
    return 0;

def getListOfPaths():
  allPaths = subprocess.check_output(["find",".","-type","f"], stdin=None, stderr=None, shell=False, universal_newlines=True)
  return allPaths
def getTitleArtist(path):
  titleArtist = subprocess.check_output(["ffprobe",path], stdin=None, stderr=subprocess.STDOUT, shell=False, universal_newlines=True)
  lines = titleArtist.split('\n')
  title = ""
  artist = ""
  for line in lines:
    if(line.find("  artist  ")!=-1):
      artist = line[line.find(": ")+2:len(line)]
    if(line.find("  title  ")!=-1):
      title = line[line.find(": ")+2:len(line)]
  return artist + " " + title

def driver():
  allPaths = getListOfPaths()
  allPaths = allPaths.split('\n')[0:-1]
  for path in allPaths:
    terms = getTitleArtist(path)
    if(existsOnYoutube(terms)==1):
      print(terms + " doesnt exist")
    else:
      print(terms + " exists")
print(existsOnYoutube("Brian eno planet water")) #if u get a 1 then it doesnt exist

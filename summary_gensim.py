from gensim.summarization.summarizer import summarize
import requests
from bs4 import BeautifulSoup
from urllib.request import urlopen

def summary(url):

 page = urlopen(url)
 soup = BeautifulSoup(page, "lxml")
 #text returns completely scrapped web page
 text = ' '.join(map(lambda p: p.text, soup.find_all('p')))
 #print(text)
 #print(soup.title.text, text)
 return text


url="https://en.wikipedia.org/wiki/Machine_learning"
text = summary(url)

print("===============Summary==================================")
#here ratio means the percentage of summary message compared to original text
print(summarize(str(text), ratio=0.05))

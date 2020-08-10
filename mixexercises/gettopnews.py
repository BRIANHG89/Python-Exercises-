import base64
from bs4 import BeautifulSoup as soup 
from urllib.request import urlopen

news_url="http://news.google.com/news/rss"
Client=urlopen(news_url)
xml_page=Client.read()
Client.close()


soup_page=soup(xml_page,"xml")
news_list=soup_page.findAll("item")

#print news title
      for news in news_list:
     
        print(news.title.text)
        print(news.link.text)
        print(news.pubDate.text)
        
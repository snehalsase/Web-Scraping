
import csv
import requests
from bs4 import BeautifulSoup

headers = {#'authority': 'phys.org',
    'method': 'GET',
    #'path': '/technology-news/',
    'scheme': 'https',
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-      exchange;v=b3;q=0.9',
    'accept-encoding': 'gzip, deflate, br',
    'accept-language': 'en-US,en;q=0.9',
    'cache-control': 'max-age=0',
    #'cookie':'deviceType=desktop_430c8bfe8bf1cc772d8a7ec27f27106cm; _ga=GA1.2.641443882.1618982763; _gid=GA1.2.1227703645.1618982763;    scx_euconsent=0; __gads=ID=f5a024fd4a29ce7f-2207ffecbab900a4:T=1618982760:RT=1618982760:S=ALNI_MY0HdAGkwP0xbd_QZzpvbmAI97ITg; __qca=P0-819260083-1618982762817',
    #'referer': 'http://phys.org./',
    'sec-ch-ua': '"Google Chrome";v="89", "Chromium";v="89", ";Not A Brand";v="99"',
    'sec-ch-ua-mobile': '?0',
    'sec-fetch-dest': 'document',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-site': 'cross-site',
    'sec-fetch-user': '?1',
    'upgrade-insecure-requests': '1',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.128 Safari/537.36',}

response = requests.get('https://phys.org/technology-news/', headers=headers)
html = response.text
print(html)
soup = BeautifulSoup(html, 'html.parser')
f = open('test.html', 'w')
f.write(html)
f.close()
 

soup_top = soup.find('div', class_='sorted-news-list')
soup_articles = soup_top.find_all('article',class_ = 'sorted-article')
urls = [x.div.a.get('href') for x in soup.find_all("article", class_ = "sorted-article")]
i=0
final_list=[]
for soup_article in soup_articles:
    
    title = soup_article.find('div', class_ = 'sorted-article-content')
    
    title = title.find('a', class_ = 'news-link').text.strip()
    
    links = urls[i]
    
    soup_info = soup_article.find('div', class_ = 'article__info')
    
    subcategory = soup_info.find_all('div', class_ = 'article__info-item')[0].text.strip()
    time = soup_info.find_all('div', class_ = 'article__info-item')[1].find('p', class_= 'text-uppercase').text.strip()
    comment = soup_info.find_all('div', class_ = 'article__info-item')[2].text.strip()
    forward=soup_info.find_all('div', class_ = 'article__info-item')[3].text.strip()
    i+=1
    li= [title,links,subcategory,time,comment,forward]
    final_list.append(li)

fields = ['title','url','subcategory','time','comments','forwards'] 
filename = "tech-news.csv"

with open(filename, 'w',newline='',encoding="utf8") as csvfile:  
    csvwriter = csv.writer(csvfile) 
    csvwriter.writerow(fields)
    csvwriter.writerows(final_list)
    
   
    






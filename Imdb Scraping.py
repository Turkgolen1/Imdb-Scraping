import requests
from bs4 import BeautifulSoup

url="https://www.imdb.com/chart/top/?ref_=nv_mv_250"



headers= {

    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
}

html=requests.get(url,headers=headers).text
soup=BeautifulSoup(html,"html.parser")
list=soup.find("ul",{"class":"ipc-metadata-list"}).find_all("li",limit=10)
for item in list:
    filmadi=item.find("h3",{"class":"ipc-title__text"}).text
    puan=item.find("span",{"class":"ipc-rating-star ipc-rating-star--base ipc-rating-star--imdb sc-9ab53865-1 iXEijC ratingGroup--imdb-rating"}).text
    print(filmadi)
    print(puan)

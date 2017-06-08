from bs4 import BeautifulSoup
from urllib.request import urlopen
url = "http://www.zbjuran.com/mei/xinggan/201611/75241_2.html"
soup = BeautifulSoup(urlopen(url),'lxml')
girl = soup.find_all("div",class_="picbox")
for link in girl:
    imgs = link.find("img")
    links = imgs.get("src")
    flink = links
    print(flink)


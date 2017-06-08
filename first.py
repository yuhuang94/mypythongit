from urllib.request import urlopen
from lxml import etree
url = "http://www.mmjpg.com/mm/1009/2"
def getlink(html):
    sele = etree.HTML(html)
    result = sele.xpath(".//*[@id='content']/a/img/text()")
    return result
print(getlink(url))
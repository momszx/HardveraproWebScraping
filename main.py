import urllib.request
import json
from bs4 import BeautifulSoup


class Item:
    def __init__(self, name, price, link):
        self.name = name
        self.price = price
        self.link = link

    def getInfo(self):
        print(self.name + " Ára:" + self.price + " Link:" + self.link)
    def toJson(self):
        return ('{"name":"'+self.name+'","price":"'+self.price+',"Link":"'+self.link+'"}')


search = input("Enter a search: ")
list = []
fp = urllib.request.urlopen(
    "https://hardverapro.hu/aprok/keres.php?stext=" + search + "&county=&stcid=&settlement=&stmid=&minprice=&maxprice=&company=&cmpid=&user=&usrid=&selling=1&buying=1&stext_none=?offset=100")
mybytes = fp.read()

mystr = mybytes.decode("utf8")
fp.close()

soup = BeautifulSoup(mystr, 'html.parser')
for link in soup.find_all("div", {"class": "media-body"}):
    list.append(Item(link.find("div", {"class": "uad-title"}).h1.a.text,
                     link.find("div", {"class": "uad-info"}).find("div", {"class": "uad-price"}).text,
                     link.find("div", {"class": "uad-title"}).h1.a.get('href')))
print(len(list))
for item in list:
    item.getInfo()

#print(json.dumps(ob.__dict__ for ob in list))

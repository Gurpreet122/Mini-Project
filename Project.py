
import pandas as pd
import requests
from bs4 import BeautifulSoup
Product_name=[]
Prices=[]
Description=[]
Reviews=[]

for i in range(2,12):
    url = "https://www.flipkart.com/search?q=mobile+under+30000&otracker=search&otracker1=search&marketplace=FLIPKART&as-show=off&as=off&page="+str(i)

    r = requests.get(url)

    soup = BeautifulSoup(r.text,"html.parser")
    box=soup.find("div",class_="DOjaWF gdgoEp")

    names = box.find_all("div", class_ ="KzDlHZ")

    for i in names:
        name = i.text
        Product_name.append(name)
    # print(Product_name)


    Price = box.find_all("div", class_="Nx9bqj _4b5DiR")
    for i in Price:
        name = i.text
        Prices.append(name)
    # print(Prices)

    desc = box.find_all('ul',class_="G4BRas")

    for i in desc:
        name = i.text
        Description.append(name)
    # print(Description)

    reviews = box.find_all("div",class_="XQDdHH")
    for i in reviews:
        name=i.text
        Reviews.append(name)
    # print(len(Reviews))


data = list(zip(Product_name, Prices, Description, Reviews))
df = pd.DataFrame(data, columns=["Product Name", "Prices", "Description", "Reviews"])

# df=pd.DataFrame({"Product Name":Product_name,"Prices":Prices,"Description":Description,"Reviews":Reviews})

print(df)

df.to_csv("D:/IMP/mobile.csv")



#
# for i in range(2,10):
#     url = "https://www.flipkart.com/search?q=mobile+under+30000&otracker=search&otracker1=search&marketplace=FLIPKART&as-show=off&as=off&page="+str(i)
#
#     r = requests.get(url)
#     # print(r)
#
#     soup = BeautifulSoup(r.text,"html.parser")
#     # print(soup)
#
#
#     # while True:
#     np = soup.find("a", class_="_9QVEpD").get("href")
#     cnp = "https://www.flipkart.com"+np
#     print(cnp)
#
#     # url=cnp
#     # r=requests.get(url)
#     # soup=BeautifulSoup(r.text,"html.parser")

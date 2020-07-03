from bs4 import BeautifulSoup
import requests

x=0

year=input("Enter a year between 1991-Present:")
saal=int(year)
if saal>1990 and saal<2010:
    url="https://en.wikipedia.org/wiki/"+year+"_FIFA_World_Player_of_the_Year"    #Valid till 1991 to 2009
elif saal>2009 and saal<2017:
    url="https://en.wikipedia.org/wiki/"+year+"_FIFA_Ballon_d%27Or"               #valid from 2010 to 2016
elif saal>2016:
    url="https://en.wikipedia.org/wiki/The_Best_FIFA_Football_Awards_"+year
r=requests.get(url)
soup=BeautifulSoup(r.text,"html.parser")
if saal<2017:
    container=soup.find("table",{"class":"wikitable"})
    table_body=container.findAll("tr")
    row=table_body[1].findAll("td")
    name=row[1].text
elif saal>2016:
    container=soup.find("table",{"class":"wikitable plainrowheaders sortable"})
    body=container.find("tbody")
    table_body=body.findAll("tr")
    row=table_body[2].findAll("td")
    name=row[1].text
if saal>1990 and saal<2010:
    print("The ",year, "FIFA World Player Of the year was",name)
elif saal>2009 and saal<2017:
    print("The ",year," FIFA Ballon D'or winner of was ",name)
elif saal>2016:
    print("The ",year," FIFA The Best winner was ",name)

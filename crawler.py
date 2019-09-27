from bs4 import *
import requests as rq
import os


r2 = rq.get("https://www.pexels.com/@hiteshchoudhary")
soup2 = BeautifulSoup(r2.text,"html.parser")

link = []

x = soup2.select('img[src^="https://images.pexels.com/photos"]')

for img in x:
    link.append(img['src'])


os.mkdir("myphotos")
i = 1

for index,img_link in enumerate(link):
    if i <=10:
        img_data = rq.get(img_link).content
        with open("myphotos/"+str(index+1)+'.jpg','wb+') as f:
            f.write(img_data)
        i = i+1
    else:
        f.close()
        break



import requests
from bs4 import BeautifulSoup
# import mysql.connector
#
# conn=mysql.connector.connect(user='root',password='',host='localhost',database='soulmet')
# mycursor=conn.cursor()


r=requests.get("https://gaana.com/playlist/gaana-dj-bollywood-top-50-1","lxml")

soup=BeautifulSoup(r.content,"lxml")
print(soup)
#print(soup.find_all("a"))

lst=soup.find_all("a",class_="sng_c")
print(lst)
for i in lst:
    m=[i.text for i.find_all("a",class_="sng_c")]
    #print(i.text)
    # query="""insert into `users` (`user_id`,`name`,`email`,`password`,`gender`,`city`) values
    # (NULL,'{}','','','','')""".format(i.text)
    # mycursor.execute(query)
    # conn.commit()
    # print('inserted')
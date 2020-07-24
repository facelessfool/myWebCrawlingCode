import pandas as pd
import requests
from bs4 import BeautifulSoup


#replace the url with your revision history url
url='https://en.wikipedia.org/w/index.php?title=United_States&offset=20030729010851%7C1215590&limit=500&action=history'

#empty lists
date_list=[]
time_list=[]
user_list=[]
m_list=[]
bytes_list=[]

source=requests.get(url).text
soup=BeautifulSoup(source,'lxml')
page=soup.find('ul',id='pagehistory')

list1 = page.find_all('a', class_='mw-changeslist-date')
for date_time in reversed(list1):
        combined_list=date_time.text
        d_t=combined_list.split(',')
        date1=d_t[1]
        date_list.append(date1)
        time1=d_t[0]
        time_list.append(time1)
    
#     print(date1, " ", time1)
# print(time_list)

users = page.find_all('a', class_='mw-userlink')
for user in reversed(users):
        user1=user.text
        user_list.append(user1)
#     print(user1)
# print(user_list)

minor_edits=page.find_all('li')
for li in reversed(minor_edits):
        li=li.text
        li=li.split(" ")
        if "m" in li:
            m=1
    #         print(m)
            m_list.append(m)
        else:
            m=0
            m_list.append(m)
#         print(m)
# print(m_list)

byteSize=page.find_all(dir='ltr')
for byte_num in reversed(byteSize):
        number=byte_num.text
        num=int(number.replace(",",""))
    #     print(num)
        bytes_list.append(num)
#     print(bytes_list)

#creating a dataframe
final_list=[]

for date_item, time_item, user_item, m_item, bytes_item in zip(date_list,time_list,user_list,m_list,bytes_list):
    final_list.append({'Date':date_item, 'Time':time_item,'user1':user_item,'user2':user_item, 'm':m_item, "#bytes changed":bytes_item})

df=pd.DataFrame(final_list)
df


#insert you cav file name you can also give path name of your csv file
df.to_csv('csv_file_name.csv',encoding="utf-8")
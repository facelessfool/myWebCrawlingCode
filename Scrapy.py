import pandas as pd
import requests
<<<<<<< HEAD
from bs4 import BeautifulSoup
=======
import csv


csv_file=open('normal_MainPage9.csv','w',encoding="utf-8")

csv_writer=csv.writer(csv_file)
csv_writer.writerow(['Date', 'Time', 'User1', ' User2', 'm or not', '#bytes changed'])


#add the url of any articles history below

source=requests.get('https://en.wikipedia.org/w/index.php?title=Main_Page&offset=20020909070344%7C207690&limit=500&action=history').text
soup=BeautifulSoup(source, 'lxml')
page=soup.find('ul',id='pagehistory' )

#for date and time

list1=page.find_all('a', class_='mw-changeslist-date')
for date_time in reversed(list1):
	date_time_list=date_time.text
	d_t=date_time_list.split(',')
	date1=d_t[1]			#variable for date is date1
	time=d_t[0]				#variable for time is time
	# print(date1,"	",time)
	# print()
	csv_writer.writerow([date1,time])



users=page.find_all('a', class_='mw-userlink')
for user in reversed(users):

	user2=user.text
	# print(user2)
	csv_writer.writerow([user2,user2])

list_m=page.find_all('li')
for li in reversed(list_m):

	li=li.text
	li=li.split(" ")

	if 'm' in li:
		m=1
		# print("m")
	else:
		m=0
		# print("0")
>>>>>>> 48d7754e043ab848cbd74c808e78257a748fce51


<<<<<<< HEAD
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


df.to_csv('csv_file_name.csv',encoding="utf-8")
=======
	# print(num)
	csv_writer.writerow([num])
csv_file.close()
>>>>>>> 48d7754e043ab848cbd74c808e78257a748fce51

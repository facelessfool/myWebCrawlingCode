from bs4 import BeautifulSoup
import requests
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

	csv_writer.writerow([m])
bytesIncDec= page.find_all(dir='ltr')
for byte_num in reversed(bytesIncDec):
	# print(byte_num.text)
	number=byte_num.text
	num=int(number.replace(",",''))

	# print(num)
	csv_writer.writerow([num])
csv_file.close()

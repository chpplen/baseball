# encoding: utf-8

import csv
import requests 
from bs4 import BeautifulSoup 
import HTMLParser 

from datetime import date
from datetime import timedelta

mapping = {"辛辛那提紅人":0,"匹茲堡海盜":1,"克里夫蘭印地安人":2,"德州遊騎兵":3,"西雅圖水手":4,"科羅拉多落磯山":5,"堪薩斯皇家":6,"亞歷桑那響尾蛇":7,"舊金山巨人":8,"奧克蘭運動家":9,"芝加哥白襪":10,"聖地牙哥教士":11,"洛杉磯道奇":12,"洛杉磯天使":13,"明尼蘇達雙城":14,"華盛頓國民":15,"波士頓紅襪":16,"多倫多藍鳥":17,"紐約洋基":18,"邁阿密馬林魚":19,"坦帕灣光芒":20,"紐約大都會":21,"聖路易紅雀":22,"芝加哥小熊":23,"巴爾的摩金鶯":24,"密爾瓦基釀酒人":25,"亞特蘭大勇士":26,"費城費城人":27,"底特律老虎":28,"休士頓太空人":29}

url = 'http://tslc.stats.com/mlb/scoreboard.asp?day='
links = []

today = date.today()

t = date(2016, 4, 2)
while today > t:
	links.append(url + t.strftime("%Y%m%d"))
	t += timedelta(1)

#print links
#records = []

with open('baseballRecord.csv', 'wb') as csvfile:
	spamwriter = csv.writer(csvfile)
	
	"""for record in records:
		spamwriter.writerow(record)"""

	for link in links: 
		
		print link

		res = requests.get(link) 
		soup = BeautifulSoup(res.text.encode("utf-8"), "html.parser")  
		
		shop_table = soup.findAll('table', {"class":"shsTable shsLinescore"})
		
		record = ""
		for table in shop_table:
			status = table.find('tr',{"class":"shsTableTtlRow"}).find('td').string
			#print status
			if status == "Cancelled" or status.encode('big5') == '延賽':
				continue
			else:
				
				shop_tr = table.findAll('tr', { "class" : "shsRow0Row" })
				for tr in shop_tr:
					record = []
					
					try:
						teamLogo = tr.find('td',{"class":"shsNamD"}).find('a')
						
						teamIndex = mapping[teamLogo.string.encode('big5')]
						
						record.append(teamIndex)
						print teamLogo.string
					except Exception:
						record.append(u'team')
						
					
					
					shop_td = tr.findAll('td',{"class":"shsTotD"})
					for td in shop_td:
						#print td.string
						record.append(td.string.encode('utf8'))
					#records.append(record)	
					spamwriter.writerow(record)

"""
for record in records:
	print record
"""	


			


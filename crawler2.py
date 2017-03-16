# encoding: utf-8

import csv
import requests 
from bs4 import BeautifulSoup 
import HTMLParser 

from datetime import date
from datetime import timedelta

#mapping = {"辛辛那提紅人":0,"匹茲堡海盜":1,"克里夫蘭印地安人":2,"德州遊騎兵":3,"西雅圖水手":4,"科羅拉多落磯山":5,"堪薩斯皇家":6,"亞歷桑那響尾蛇":7,"舊金山巨人":8,"奧克蘭運動家":9,"芝加哥白襪":10,"聖地牙哥教士":11,"洛杉磯道奇":12,"洛杉磯天使":13,"明尼蘇達雙城":14,"華盛頓國民":15,"波士頓紅襪":16,"多倫多藍鳥":17,"紐約洋基":18,"邁阿密馬林魚":19,"坦帕灣光芒":20,"紐約大都會":21,"聖路易紅雀":22,"芝加哥小熊":23,"巴爾的摩金鶯":24,"密爾瓦基釀酒人":25,"亞特蘭大勇士":26,"費城費城人":27,"底特律老虎":28,"休士頓太空人":29}

mapping2 = {u"辛辛那提紅人":'Cincinnati',u"匹茲堡海盜":'Pittsburgh',u"克里夫蘭印地安人":'Cleveland'
			,u"德州遊騎兵":'Texas',u"西雅圖水手":'Seattle',u"科羅拉多落磯山":'Colorado'
			,u"堪薩斯皇家":'Kansas City',u"亞歷桑那響尾蛇":'Arizona',u"舊金山巨人":'San Francisco'
			,u"奧克蘭運動家":'Oakland',u"芝加哥白襪":'Chicago Sox',u"聖地牙哥教士":'San Diego'
			,u"洛杉磯道奇":'LA Dodgers',u"洛杉磯天使":'LA Angels',u"明尼蘇達雙城":'Minnesota'
			,u"華盛頓國民":'Washington',u"波士頓紅襪":'Boston',u"多倫多藍鳥":'Toronto'
			,u"紐約洋基":'NY Yankees',u"邁阿密馬林魚":'Miami',u"坦帕灣光芒":'Tampa Bay'
			,u"紐約大都會":'NY Mets',u"聖路易紅雀":'St. Louis',u"芝加哥小熊":'Chicago Cubs'
			,u"巴爾的摩金鶯":'Baltimore',u"密爾瓦基釀酒人":'Milwaukee',u"亞特蘭大勇士":'Atlanta'
			,u"費城費城人":'Philadelphia',u"底特律老虎":'Detroit',u"休士頓太空人":'Houston'}


url = 'http://espn.go.com/mlb/stats/team/_/stat/batting/split/'
links = []

dateMap = [[]
		  ,[]
		  ,[]
		  ]
for i in range(40,43):
	links.append(url + str(i))


url2 = 'http://tslc.stats.com/mlb/scoreboard.asp?day='

tEnd = date(2016, 5, 31)
tStart = date(2016, 5, 1)
while tEnd > tStart:
	dateMap[0].append(url2 + tStart.strftime("%Y%m%d"))
	tStart += timedelta(1)
tEnd = date(2016, 6, 30)
tStart = date(2016, 6, 1)
while tEnd > tStart:
	dateMap[1].append(url2 + tStart.strftime("%Y%m%d"))
	tStart += timedelta(1)
tEnd = date(2016, 7, 21)
tStart = date(2016, 7, 1)
while tEnd > tStart:
	dateMap[2].append(url2 + tStart.strftime("%Y%m%d"))
	tStart += timedelta(1)

#print dateMap[0]
records = {}

with open('baseballRecord2.csv', 'wb') as csvfile:
	spamwriter = csv.writer(csvfile)
	for link in range(len(links)): 
			
		print links[link]

		res = requests.get(links[link]) 
		soup = BeautifulSoup(res.text.encode("utf-8"), "html.parser")  
		
		shop_table = soup.findAll('table', {"class":"tablehead"})
		
		shop_tr = shop_table[0].findAll('tr')
		
		for i in range(2,32):
			shop_td = shop_tr[i].findAll('td')
			
			teamName = shop_td[1].find('a').string
			print teamName
			
			temp = []
			for j in range(2,len(shop_td)):
				temp.append(float(shop_td[j].string))
				
			records.update({teamName:temp})
		
		for dayFight in dateMap[link]:
			print dayFight
		
			res = requests.get(dayFight) 
			soup = BeautifulSoup(res.text.encode("utf-8"), "html.parser")

			shop_table = soup.findAll('table', {"class":"shsTable shsLinescore"})
			
			record = ""
			for table in shop_table:
				status = table.find('tr',{"class":"shsTableTtlRow"}).find('td').string
				#print status
				if status == "Cancelled" or status == u'延賽':
					continue
				else:
					
					
					shop_tr = table.findAll('tr', { "class" : "shsRow0Row" })
					for tr in shop_tr:
						record = []
						
						try:
							teamLogo = tr.find('td',{"class":"shsNamD"}).find('a')
							#print teamLogo.string
							teamName = mapping2[teamLogo.string]
							print teamName
							
							record.append(teamName)
							
							features = records[teamName]
							for feature in features:
								record.append(feature)
							
							shop_td = tr.findAll('td')
							record.append(shop_td[13].string)
							#print teamLogo.string
						except Exception:
							print tr
							record.append(u'team')

						spamwriter.writerow(record)
						
		
#print records

"""
with open('baseballRecord2.csv', 'wb') as csvfile:
	spamwriter = csv.writer(csvfile)
	

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
"""
for record in records:
	print record
"""	


			


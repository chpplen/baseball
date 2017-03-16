# encoding: utf-8

import csv
import requests 
from bs4 import BeautifulSoup 
import HTMLParser 

from datetime import date
from datetime import timedelta

mapping = {"�����������H":0,"�ǯ������s":1,"�J�������L�a�w�H":2,"�w�{�C�M�L":3,"�趮�Ϥ���":4,"��ù�Ԧh���F�s":5,"���Ĵ��Ӯa":6,"�Ⱦ��ᨺ�T���D":7,"�ª��s���H":8,"���J���B�ʮa":9,"�ۥ[������":10,"�t�a�����Фh":11,"�����F�D�_":12,"�����F�Ѩ�":13,"����Ĭ�F����":14,"�ز��y���":15,"�i�h�y����":16,"�h�ۦh�ų�":17,"�ì��v��":18,"�ڪ��K���L��":19,"�Z���W���~":20,"�ì��j���|":21,"�t��������":22,"�ۥ[���p��":23,"�ں��������a":24,"�K���˰��C�s�H":25,"�ȯS���j�i�h":26,"�O���O���H":27,"���S�ߦѪ�":28,"��h�y�ӪŤH":29}

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
			if status == "Cancelled" or status.encode('big5') == '����':
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


			


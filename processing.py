
import csv

feature = {}
for i in range(30):
	feature.update({str(i):{"enemy":-1,"rate":0.0,"score":0.0,"hit":0.0,"error":0.0,"gameNumber":0,"lastFiveResults":[0]*5,"winResults":[0]*30,"lossResults":[0]*30}})

data = []
with open('baseballRecord.csv', 'rb') as csvfile:
	spamreader = csv.reader(csvfile)
	
	for row in spamreader:
		data.append(row)


teamData = {}
for i in range(30):
	teamData.update({str(i):[]})

print len(data)
for i in xrange(0,len(data),2):
	#print i

	teamA = data[i]
	teamB = data[i+1]
	
	teamAName = teamA[0]
	teamBName = teamB[0]
	
	if teamAName == 'team':
		continue
	
	teamAF = feature[teamAName]
	teamBF = feature[teamBName]
	
	
	ANumber = teamAF["gameNumber"]
	Ascore = float(teamA[10])
	teamAF.update({"score":(teamAF["score"]*ANumber + Ascore)/(ANumber + 1)})
	teamAF.update({"hit":(teamAF["hit"]*ANumber + float(teamA[11]))/(ANumber + 1)})
	teamAF.update({"error":(teamAF["error"]*ANumber + float(teamA[12]))/(ANumber + 1)})
	
	BNumber = teamBF["gameNumber"]
	Bscore = float(teamB[10])
	teamBF.update({"score":(teamBF["score"]*BNumber + Bscore)/(BNumber + 1)})
	teamBF.update({"hit":(teamBF["hit"]*BNumber + float(teamB[11]))/(BNumber + 1)})
	teamBF.update({"error":(teamBF["error"]*BNumber + float(teamB[12]))/(BNumber + 1)})
	
	
	Aresult = 0
	Bresult = 0
	if Ascore > Bscore:
		Aresult = 1
	else:
		Bresult = 1

	AlastFiveResults = teamAF["lastFiveResults"][:]
	del AlastFiveResults[0]
	AlastFiveResults.append(Aresult)
	teamAF.update({"lastFiveResults":AlastFiveResults})
	teamAF.update({"rate":(teamAF["rate"]*ANumber + Aresult)/(ANumber + 1)})
	teamAF.update({"gameNumber":ANumber + 1})
	
	AlossResults = teamAF["lossResults"][:]
	AwinResults = teamAF["winResults"][:]
	if Aresult == 1:
		AwinResults[int(teamBName)] += 1
	else:
		AlossResults[int(teamBName)] += 1
	teamAF.update({"lossResults":AlossResults})
	teamAF.update({"winResults":AwinResults})
	teamAF.update({"result":Aresult})
	teamAF.update({"enemy":int(teamBName)})
	
	
	BlastFiveResults = teamBF["lastFiveResults"][:]
	del BlastFiveResults[0]
	BlastFiveResults.append(Bresult)
	teamBF.update({"lastFiveResults":BlastFiveResults})
	teamBF.update({"rate":(teamBF["rate"]*BNumber + Bresult)/(BNumber + 1)})
	teamBF.update({"gameNumber":BNumber + 1})
	
	BlossResults = teamBF["lossResults"][:]
	BwinResults = teamBF["winResults"][:]
	if Bresult == 1:
		BwinResults[int(teamAName)] += 1
	else:
		BlossResults[int(teamAName)] += 1
	teamBF.update({"lossResults":BlossResults})
	teamBF.update({"winResults":BwinResults})
	teamBF.update({"result":Bresult})
	teamBF.update({"enemy":int(teamAName)})
	
	feature[teamAName] = teamAF
	feature[teamBName] = teamBF
	
	teamData[teamAName].append(teamAF.copy())
	teamData[teamBName].append(teamBF.copy())

print teamData['0']
#rint teamData['1']
print len(teamData)

for tt in range(30):
	with open('team' + str(tt) + '.csv', 'wb') as csvfile:
		spamwriter = csv.writer(csvfile)
		
		spamwriter.writerow(["enemy","result","rate","score","hit","error","gameNumber"])
		test = teamData[str(tt)]
		for t in test:
			temp = []
			temp.append(t["enemy"])
			temp.append(t["result"])
			temp.append(t["rate"])
			temp.append(t["score"])
			temp.append(t["hit"])
			temp.append(t["error"])
			temp.append(t["gameNumber"])
			for last in t["lastFiveResults"]:
				temp.append(last)
			for last in t["winResults"]:
				temp.append(last)
			for last in t["lossResults"]:
				temp.append(last)
			spamwriter.writerow(temp)
	
		
	
	




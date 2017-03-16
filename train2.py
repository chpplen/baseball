from LogisticRegression import LogisticRegression
from FeatureSelection import FeatureSelection
from sklearn import datasets
import csv
"""
iris = datasets.load_iris()
X = iris.data[:, :3]  # we only take the first two features.
Y = iris.target
"""


data = []
with open('baseballRecord2.csv', 'rb') as csvfile:
	spamreader = csv.reader(csvfile)
	
	for row in spamreader:
		data.append(row)

X = []
Y = []

testX = []
testY = []
for i in xrange(0, len(data), 2):
	temp1 = []
	temp2 = []
	for f in range(1,14):
		temp1.append(float(data[i][f]))
		temp2.append(float(data[i+1][f]))
	X.append(temp1)
	X.append(temp2)
	
	score1 = int(data[i][14])
	score2 = int(data[i+1][14])
	
	if score1 > score2:
		Y.append(1)
		Y.append(0)
	else:
		Y.append(0)
		Y.append(1)
		
#for x in X:
#	print x
#print Y
		
		


"""
for i in range(40,len(data)-1):
#for i in range(6,70):
	temp = []
	
	thisOne = data[i]
	nextOne = data[i+1]
	
	enemy = nextOne[0]
	
	loss = float(thisOne[12+int(enemy)])
	win = float(thisOne[42+int(enemy)])
	for index in range(2,12):
		temp.append(float(thisOne[index]))
	
	try:
		temp.append(win/(loss+win))
	except Exception:
		temp.append(0)
		
	if i < 80:
		Y.append(int(nextOne[1]))
		X.append(temp)
	else:
		testY.append(int(nextOne[1]))
		testX.append(temp)
"""	
	
#print len(X)
#print len(testX)


fs = FeatureSelection(4)
fs.forward(X,Y)

print fs.summary()

X = fs.getFeature(X)
testX = fs.getFeature(testX)

#print X
#print testX


"""
for i in range(len(X)):
	X[i].append(1)
for i in range(len(testX)):
	testX[i].append(1)

"""


lg = LogisticRegression(X,Y)
lg.train()

print lg.accuracy(X,Y)

#print lg.accuracy(testX,testY)
for x in testX:
	print lg.predict(x)
	print lg.probability(x)

#print lg.predict(testX[len(testX)-1])
#print testY[len(testY)-1]



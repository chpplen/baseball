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
with open('team10.csv', 'rb') as csvfile:
	spamreader = csv.reader(csvfile)
	
	for row in spamreader:
		data.append(row)
		
#print data[1]
X = [
	[0.266,0.328,0.41,5.4],
	[0.266,0.324,0.437,4.49],
	[0.266,0.327,0.436,4.91],
	[0.264,0.321,0.426,9.72],
	[0.261,0.333,0.408,4.89],
	[0.261,0.334,0.449,4],
	[0.261,0.328,0.439,4.26],
	[0.261,0.334,0.405,2.64],
	[0.259,0.322,0.435,4.58],
	[0.254,0.345,0.432,2.89],
	[0.253,0.334,0.438,3.98],
	[0.252,0.307,0.401,4.25],
	[0.25,0.316,0.413,5.02],
	[0.25,0.325,0.426,4.91],
	[0.25,0.311,0.395,4.96],
	[0.249,0.313,0.397,4.14],
	[0.245,0.322,0.391,2.45],
	[0.244,0.318,0.396,3.25],
	[0.244,0.304,0.404,4.55],
	[0.244,0.323,0.417,4.75],
	[0.24,0.293,0.388,4.98],
	[0.239,0.299,0.395,4.66],
	[0.238,0.306,0.419,5.64],
	[0.237,0.309,0.414,3.56],
	[0.237,0.301,0.348,4.67],
	[0.289,0.357,0.471,4.36],
	[0.272,0.335,0.456,3.43],
	[0.272,0.331,0.408,3.03],
	[0.271,0.321,0.409,3.75],
	[0.269,0.33,0.462,4.05]]
Y = [1,1,1,0,1,1,1,0,0,1,1,1,0,0,1,0,0,0,0,0,0,1,0,0,0,0,1,1,1,0]

testX = [[0.237,0.309,0.414,2.43],
		 [0.261,0.334,0.449,2.83],
		 [0.266,0.327,0.436,3.74],
		 [0.289,0.357,0.471,2.83]]
testY = []

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
	
print len(X)
print len(testX)

"""
fs = FeatureSelection(4)
fs.forward(X,Y)

print fs.summary()

X = fs.getFeature(X)
testX = fs.getFeature(testX)

print X
print testX
"""
for i in range(len(X)):
	X[i].append(1)
for i in range(len(testX)):
	testX[i].append(1)




lg = LogisticRegression(X,Y)
lg.train()

print lg.accuracy(X,Y)

#print lg.accuracy(testX,testY)
for x in testX:
	print lg.predict(x)
	print lg.probability(x)

#print lg.predict(testX[len(testX)-1])
#print testY[len(testY)-1]




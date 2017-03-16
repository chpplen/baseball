from LogisticRegression import LogisticRegression

class FeatureSelection(object):
	def __init__(self, forwardNumber):
		self.forwardNumber = forwardNumber
		self.forwardIndex = []
		self.forThres = 0.01
		self.summaryText = "forward selected not run yet!"
		
	def forward(self, X, Y):
		
		self.summaryText = "forward selected begin!\n------------------------------------------------------------\n"
		lastRsquared_adj = 0
		while(len(self.forwardIndex)<self.forwardNumber):
			
			tempX = []
			for x in X:
				tempx = []
				for i in self.forwardIndex:
					tempx.append(x[i])
				tempX.append(tempx)
				
			for j in range(0,len(tempX)):
				tempX[j].append(-1)
						
			maxRsquared_adj = 0
			featureThisRound = 0
			for i in range(0,len(X[0])):
				if i in self.forwardIndex:
					continue
				else:
					index = len(tempX[0]) - 1
					
					for j in range(0,len(tempX)):
						tempX[j][index] = X[j][i]
				
				lg = LogisticRegression(tempX,Y)
				lg.train()
				
				rsquared_adj = lg.accuracy(tempX,Y)
				self.summaryText += "Feature: " + str(i) + ", adjust R-squared: " + str(rsquared_adj) + "\n"
				
				
				if rsquared_adj > maxRsquared_adj:
					maxRsquared_adj = rsquared_adj
					featureThisRound = i
			
			if lastRsquared_adj + self.forThres > maxRsquared_adj:
				self.summaryText += "There is no enough improve, Stop\n"
				self.summaryText += "------------------------------------------------------------\n"
				break
			else:
				self.summaryText += "adjust R-square before: " + str(lastRsquared_adj) + ", adjust R-square after: " + str(maxRsquared_adj) + "\n"
				self.forwardIndex.append(featureThisRound)
				lastRsquared_adj = maxRsquared_adj
				self.summaryText += "Forward this round: " + str(self.forwardIndex) + "\n";
				self.summaryText += "------------------------------------------------------------\n"
	
	def getFeature(self, X):
		newX = []
		for x in X:
			newx = []
			for i in self.forwardIndex:
				newx.append(x[i])
			newX.append(newx)
		return newX
	
	def summary(self):
		return self.summaryText
				
				
					
	
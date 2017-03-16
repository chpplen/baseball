from sklearn import linear_model
from math import exp

class LogisticRegression(object):
	def __init__(self,X,Y):
		self.X = X
		self.Y = Y
		self.logreg = linear_model.LogisticRegression(C=1e5)
			
	def train(self):
		self.logreg.fit(self.X, self.Y)
	
	def predict(self, X):
		return self.logreg.predict(X)
		
	def probability(self, X):
		score = self.logreg.decision_function(X)
		return 1/(1+exp(-score))
	
	def accuracy(self, X, Y):
		return self.logreg.score(X,Y)
		
	

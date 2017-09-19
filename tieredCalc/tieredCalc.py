#File: tieredCalc.py

#Define list of rates as dictionary, ideally should be loaded from file...



#def calc(startingSR, targetSR)
	#"""
	#Does work
	#"""
	
	
	
import collections
	
	
	
	
tierPrices = {
4450 : 2.8,
4400 : 2.6,
4350 : 2.4,
4300 : 2.3,
4250 : 2.0,
4200 : 1.2,
4150 : 1.1,
4100 : 0.9,
4050 : 0.8,
4000 : 0.6,
3750 : 0.48, 
3500 : 0.36, 
3250 : 0.26, 
3000 : 0.22, 
2750 : 0.18, 
2500 : 0.14, 
2000 : 0.1, 
1500 : 0.08, 
1000 : 0.05, 
500 : 0.04, 
1 : 0.04}


targetSR = int(input("Enter targetSR"))

print() #new line
#print(targetSR) #prints whatever the user entered
	
	
	
	
def closestTier(key):
	"""
	Finds the key value closest to input value
	"""
	return min(tierPrices,key=lambda x:abs(x-key))
	
highestTier = closestTier(targetSR)
print (highestTier)







#print (tierPrices[4400])




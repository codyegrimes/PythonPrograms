def getInput():
	"""
	#reStructuredText (reST) format: https://stackoverflow.com/questions/3898572/what-is-the-standard-python-docstring-format#
	Prompts user for two numbers.
	
	
	:returns: the two numbers entered by the users
	"""
	
	inputs = []
	
	input1 = int(input("Enter starting SR: "))
	inputs.append(input1)
	
	input2 = int(input("Enter target SR: "))
	inputs.append(input2)
	
	return inputs
	
#startingSR, targetSR = getInput()
	
	
def calculate(currentTierPrice, targetSR, price, tierCieling):
	tierSR = targetSR - tierCieling
	priceForTier = tierSR * currentTierPrice
	price += priceForTier
	targetSR -= tierSR
	return currentTierPrice, targetSR, price


	
	
	
def recursiveCalc(startingSR, targetSR, price, currentTierPrice): #price/currentTier start at 0, get replaced by actual value...
	if(targetSR<=startingSR):
		return price - ((startingSR - targetSR) * currentTierPrice)
	elif(targetSR>4450):
		currentTierPrice = 2.8
		currentTierPrice, targetSR, price = calculate(2.8, targetSR, price, 4450)
		return recursiveCalc(startingSR, targetSR, price, currentTierPrice)

	
	
	
	
	
	
price = 0
currentTierPrice = 0	

#run calculator --> what the user sees
def calc(startingSR, targetSR):
	return recursiveCalc(startingSR,targetSR, price, currentTierPrice) #INTERNAL call with other params
	
result = calc(4451, 4455)
print (result)
	

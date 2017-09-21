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
	#DEPRECATED: has been split into four methods
	tierSR = targetSR - tierCieling
	priceForTier = tierSR * currentTierPrice
	price += priceForTier
	targetSR -= tierSR
	return currentTierPrice, targetSR, price
	
	
	
def calcTierSR(targetSR, tierCieling): #determines how much SR to be price at this tier
	tierSR = targetSR - tierCieling
	return tierSR
	
def priceForTier(tierSR, currentTierPrice): #determines what the price for this tier is
	priceForTier = tierSR * currentTierPrice
	return priceForTier
	
def adjustTargetSR(targetSR, tierSR): #adjusts targetSR before next call
	targetSR -= tierSR
	return targetSR

def accumulatePrice(price, priceForTier): #think of better function name; adds to running total
	price += priceForTier
	return price
	
	
	
	
def recursiveCalc(startingSR, targetSR, price): #todo revise: price/currentTier start at 0, get replaced by actual value...
	if(targetSR>4450):
		currentTierPrice = 2.8
		tierSR = calcTierSR(targetSR, 4450)
		priceInTier = priceForTier(tierSR, currentTierPrice)
		price = accumulatePrice(price, priceInTier)
		targetSR = adjustTargetSR(targetSR, tierSR)
	elif(targetSR>4400):
		currentTierPrice = 2.6
		tierSR = calcTierSR(targetSR, 4400)
		priceInTier = priceForTier(tierSR, currentTierPrice)
		price = accumulatePrice(price, priceInTier)
		targetSR = adjustTargetSR(targetSR, tierSR)
	elif(targetSR>4350):
		currentTierPrice = 2.4
		tierSR = calcTierSR(targetSR, 4350)
		priceInTier = priceForTier(tierSR, currentTierPrice)
		price = accumulatePrice(price, priceInTier)
		targetSR = adjustTargetSR(targetSR, tierSR)
		
	if(targetSR<=startingSR):
		return price - ((startingSR - targetSR) * currentTierPrice)
	else:
		return recursiveCalc(startingSR, targetSR, price)


	
	
	
	
	
	
price = 0


#run calculator --> what the user sees
def calc(startingSR, targetSR):
	return recursiveCalc(startingSR,targetSR, price) #INTERNAL call with other params
	
#hard coding for now in order to test
result = calc(4370, 4401)
print (result)
	

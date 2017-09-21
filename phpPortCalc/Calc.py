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
	elif(targetSR>4300):
		currentTierPrice = 2.3
		tierSR = calcTierSR(targetSR, 4300)
		priceInTier = priceForTier(tierSR, currentTierPrice)
		price = accumulatePrice(price, priceInTier)
		targetSR = adjustTargetSR(targetSR, tierSR)
	elif(targetSR>4250):
		currentTierPrice = 2.0
		tierSR = calcTierSR(targetSR, 4250)
		priceInTier = priceForTier(tierSR, currentTierPrice)
		price = accumulatePrice(price, priceInTier)
		targetSR = adjustTargetSR(targetSR, tierSR)
	elif(targetSR>4200):
		currentTierPrice = 1.2
		tierSR = calcTierSR(targetSR, 4200)
		priceInTier = priceForTier(tierSR, currentTierPrice)
		price = accumulatePrice(price, priceInTier)
		targetSR = adjustTargetSR(targetSR, tierSR)
	elif(targetSR>4150):
		currentTierPrice = 1.1
		tierSR = calcTierSR(targetSR, 4150)
		priceInTier = priceForTier(tierSR, currentTierPrice)
		price = accumulatePrice(price, priceInTier)
		targetSR = adjustTargetSR(targetSR, tierSR)
	elif(targetSR>4100):
		currentTierPrice = 0.9
		tierSR = calcTierSR(targetSR, 4100)
		priceInTier = priceForTier(tierSR, currentTierPrice)
		price = accumulatePrice(price, priceInTier)
		targetSR = adjustTargetSR(targetSR, tierSR)
	elif(targetSR>4050):
		currentTierPrice = .8
		tierSR = calcTierSR(targetSR, 4050)
		priceInTier = priceForTier(tierSR, currentTierPrice)
		price = accumulatePrice(price, priceInTier)
		targetSR = adjustTargetSR(targetSR, tierSR)
	elif(targetSR>4000):
		currentTierPrice = .6
		tierSR = calcTierSR(targetSR, 4000)
		priceInTier = priceForTier(tierSR, currentTierPrice)
		price = accumulatePrice(price, priceInTier)
		targetSR = adjustTargetSR(targetSR, tierSR)
	elif(targetSR>3750):
		currentTierPrice = .48
		tierSR = calcTierSR(targetSR, 3750)
		priceInTier = priceForTier(tierSR, currentTierPrice)
		price = accumulatePrice(price, priceInTier)
		targetSR = adjustTargetSR(targetSR, tierSR)
	elif(targetSR>3500):
		currentTierPrice = .36
		tierSR = calcTierSR(targetSR, 3500)
		priceInTier = priceForTier(tierSR, currentTierPrice)
		price = accumulatePrice(price, priceInTier)
		targetSR = adjustTargetSR(targetSR, tierSR)
	elif(targetSR>3250):
		currentTierPrice = .26
		tierSR = calcTierSR(targetSR, 3250)
		priceInTier = priceForTier(tierSR, currentTierPrice)
		price = accumulatePrice(price, priceInTier)
		targetSR = adjustTargetSR(targetSR, tierSR)
	elif(targetSR>3000):
		currentTierPrice = .22
		tierSR = calcTierSR(targetSR, 3000)
		priceInTier = priceForTier(tierSR, currentTierPrice)
		price = accumulatePrice(price, priceInTier)
		targetSR = adjustTargetSR(targetSR, tierSR)
	elif(targetSR>2750):
		currentTierPrice = .18
		tierSR = calcTierSR(targetSR, 2750)
		priceInTier = priceForTier(tierSR, currentTierPrice)
		price = accumulatePrice(price, priceInTier)
		targetSR = adjustTargetSR(targetSR, tierSR)
	elif(targetSR>2500):
		currentTierPrice = .14
		tierSR = calcTierSR(targetSR, 2500)
		priceInTier = priceForTier(tierSR, currentTierPrice)
		price = accumulatePrice(price, priceInTier)
		targetSR = adjustTargetSR(targetSR, tierSR)
	elif(targetSR>2000):
		currentTierPrice = .1
		tierSR = calcTierSR(targetSR, 2000)
		priceInTier = priceForTier(tierSR, currentTierPrice)
		price = accumulatePrice(price, priceInTier)
		targetSR = adjustTargetSR(targetSR, tierSR)
	elif(targetSR>1500):
		currentTierPrice = .08
		tierSR = calcTierSR(targetSR, 1500)
		priceInTier = priceForTier(tierSR, currentTierPrice)
		price = accumulatePrice(price, priceInTier)
		targetSR = adjustTargetSR(targetSR, tierSR)
	elif(targetSR>1000):
		currentTierPrice = .05
		tierSR = calcTierSR(targetSR, 1000)
		priceInTier = priceForTier(tierSR, currentTierPrice)
		price = accumulatePrice(price, priceInTier)
		targetSR = adjustTargetSR(targetSR, tierSR)
	elif(targetSR>500):
		currentTierPrice = .04
		tierSR = calcTierSR(targetSR, 500)
		priceInTier = priceForTier(tierSR, currentTierPrice)
		price = accumulatePrice(price, priceInTier)
		targetSR = adjustTargetSR(targetSR, tierSR)
	elif(targetSR>1):
		currentTierPrice = .04
		tierSR = calcTierSR(targetSR, 1)
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
	

startingSR, targetSR = getInput()
result = calc(startingSR, targetSR)
print (result)
	

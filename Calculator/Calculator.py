#File: Calculator.py


def getInput():
	"""
	#reStructuredText (reST) format: https://stackoverflow.com/questions/3898572/what-is-the-standard-python-docstring-format#
	Prompts user for two numbers.
	
	
	:returns: the two numbers entered by the users
	"""
	
	inputs = []
	
	input1 = int(input("Enter a number: "))
	inputs.append(input1)
	
	input2 = int(input("Enter a number: "))
	inputs.append(input2)
	
	return inputs
	
def addition(num1, num2):
	"""
	Adds the two numbers.
	
	:param1 num1: first number to be used for addition operation
	:param1 num1: second number to be used for addition operation
	
	:returns: sum of the two parameters
	"""
	
	sum = num1 + num2
	return sum
	
def subtraction(num1, num2):
	"""
	Subtracts the two numbers.
	
	:param1 num1: first number to be used for subtraction operation
	:param1 num1: second number to be used for subtraction operation
	
	:returns: difference of the two parameters
	"""
	
	difference = num1 - num2
	return difference

def multiplication(num1, num2):
	"""
	Multiplies the two numbers.
	
	:param1 num1: first number to be used 
	:param1 num1: second number to be used 
	
	:returns: Product of the two parameters
	"""
	
	product = num1 * num2
	return product	

def division(num1, num2):
	"""
	Divides	the two numbers.
	
	:param1 num1: first number to be used 
	:param1 num1: second number to be used 
	
	:returns: Quotient of the two parameters
	"""
	
	quotient = num1 / num2
	return quotient	
	
def modulus(num1, num2):
	"""
	Performs modulus operation. num 1 % num 2
	
	:param1 num1: first number to be used 
	:param1 num1: second number to be used 
	
	:returns: Remainder of the two parameters
	"""
	
	remainder = num1 % num2
	return remainder	
	
def power(num1, num2):
	"""
	num1^num2
	
	:param1 num1: first number to be used 
	:param1 num1: second number to be used 
	
	:returns: num1 to the power of num2
	"""
	
	power = num1 ** num2
	return power	
	
	
num1, num2 = getInput()
operationsList = [
"Press '1' to add the two numbers",
"Press '2' to subtract the two numbers",
"Press '3' to multiply the two numbers",
"Press '4' to divide the two numbers",
"Press '5' to modulus the two numbers",
"Press '6' to raise the first number to the power of the second"]

for choice in operationsList:
	print(choice)
	
selectedOperation = input()

if selectedOperation == '1':
	print(addition(num1,num2))
elif selectedOperation == '2':
	print(subtraction(num1,num2))
elif selectedOperation == '3':
	print(multiplication(num1,num2))
elif selectedOperation == '4':
	print(division(num1,num2))
elif selectedOperation == '5':
	print(modulus(num1,num2))
elif selectedOperation == '6':
	print(power(num1,num2))
else:
	print('ERROR: Did not recognize your input!')

	
	




	
	
	

	
	
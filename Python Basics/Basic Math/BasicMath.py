#File: BasicMath.py

#addition & subtraction
number = 1     #store "1" in variable "number"
print(number)  #print what is stored in variable "number" to std.out

number2 = 2  
addition = number + number2  #add 1 + 2
print(addition)              #print out result: 3

subtraction = number2 - number
print(subtraction)            #subtract 2-1 = 1

#Test: Can we reassign values?
number2 = 1
subtraction = number2 - number2
print(subtraction)
#Result: YES -- prints 1-1="0"


#multiplication & division
number3 = 5
multiply = number * number2 * number3  
#expect 1 * 1 * 5 = 5
print(multiply)

number4 = 10
divide = number4/number3
#expect 10/5=2
print(divide) #research: this prints out "2.0" instead of "2" 


#power/exponents & modulus
power = 2 ** number3 
#expect: 2^5 = 32
print(power)


modulus = 11%3
#expect 11/3 = 3 R2
print(modulus)


#Neat, python stuff

#MULTIPLY STRINGS
exampleString = "Hello"
tenHellos = exampleString * 10
print(tenHellos) #prints HelloHelloHello...

#CONCATENATE LISTS with '+' operator
even_numbers = [2,4,6]
odd_numbers = [1,3,5]
all_numbers = even_numbers + odd_numbers #prints 2 4 6 1 3 5

#Can also multiply lists
print(even_numbers*3) #prints 2 4 6 2 4 6 2 4 6



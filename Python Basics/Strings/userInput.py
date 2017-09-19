#File: userInput.py

#Prompt user
#tab to indent right, SHIFT+TAB to indent left

print ('Please enter a number: ')
userInput = input()

print() #new line
print(userInput) #prints whatever the user entered


#Testing adding two user inputted numbers
#Getting fancy, saving prompt in a string
prompt = ('Please enter the first number: ')
print(prompt)
number1 = input()

print ('Please enter a second number: ')
number2 = input()

print()
addition = number1 + number2
print(addition) #if user enters '10' and '20', this prints '1020' --> need to convert to int

prompt = ('Please enter the first number: ')
print(prompt)
number1 = int(input())

print ('Please enter a second number: ')
number2 = int(input())

print()
addition = number1 + number2
print(addition)
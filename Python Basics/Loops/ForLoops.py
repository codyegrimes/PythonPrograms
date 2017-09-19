#File: ForLoops.py

#For loops are pre-condition loops (check, THEN run code until condition becomes FALSE)


for x in range(0,3): #loops 3 times: 0, 1, 2
	print ("The value of x is: {}".format(x)) #NOTE: WATCH PARANTHESES! .format(X)) <-- must be enclosed in paranth
	#print("The value of x is: {}").format(x) DOES NOT WORK!!
	print ('hello') #this loops 'hello' three times
		#print('hello') // THIS DOES NOT WORK --> "Unexpected indent"
		
print('hiya') #this prints 'hiya' once as if it wasn't part of the loop
		
		
		
#Nested Loop
for x in range(0,3): #this is outer loop
	print('3 times')
	for y in range(0,4): #this is nested, inner loop
		print('4 times') #total of 12 times: 3*4=12
		

#For Each loop -- print out contents of structures

list = ['hello','hiya','how','are','you']
for x in list:
	print (x) #prints hello hiya how are you
	
	
#Practice problem: star problem -- expected output:
# *
# **
# ***
# ****
# *****

#THINK: 5 outer, 1-5 inner

for column in range (0,5): #loops 5 times
	for y in range(0,column+1):
		print('*',end="") #by default, print() puts a newline. 'end' parameter defaults to \n, can specify blank space to stay on same line
	print() #new line after each row of stars

	
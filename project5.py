def task1():
	print 'This is task 1'

def task2():
	print 'This is task 2'

def task3():
	print 'This is task 3'
#These are the definitions for the tasks.
choice = 0
while choice != 4:
	print '\n'
	print 'Select 1 to run task 1'
	print 'Select 2 to run task 2'
	print 'Select 3 to run task 3'
	print 'Select 4 to end the program'
	choice = input('Enter number from above: ')
#This is the main menu.
	if choice == 1:
		task1()
		num = input('Enter a number greater than 0: ')
		while num > 0:
			num = num / 2
			rem = num % 2
			print rem,
#This code operates task 1.
	if choice == 2:
		task2()
		POSTNET = raw_input("Enter a 5 digit zip code: ")
		SUM = 0
		for digit in POSTNET: 
			SUM = SUM + int(digit)
		check = 10 - (SUM % 10)
		
		print check
#This code operates task 2.
	if choice == 3:
		task3()
		check = input('Enter a number greater than 0: ')
		SumFactors = 0
		for x in range(1,check - 1):
			if check % x == 0:
				SumFactors = x + SumFactors
		if SumFactors > check:
			print check, "is abundant"
		else:
			print check, "is not abundant"
#This code operates task 3.
		
print '\nThe program will now end!'
#This this is the message that will appear when the program is ended.
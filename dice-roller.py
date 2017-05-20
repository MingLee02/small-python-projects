import random

def getDiceRoll():
	print('please input number of dice')
	return input()

def getDiceSides():
	print('input type of dice')
	return input()

def checkValid(num):
	if num.isdigit():
		return True
	else:
		return False

def rollDice(num, sides):
	count = 0
	min = 1
	max = int(sides)
	while (count < max):
		print(random.randint(min, max))
		count += 1

rollAgain = 1

print('How many dice would you like to roll')
print('How many sides')

while rollAgain != '0':
	num = getDiceRoll()
	sides = getDiceSides()
	is_valid = checkValid(num)

	if is_valid:
		rollDice(num, sides)
	rollAgain = input('roll again 0 for stop:')
	continue

print ("Good bye!")
def collatz(number):
    if number % 2 == 0:
        return number // 2
    elif number % 2 == 1:
        return 3 * number + 1

while True:
	try:
		print('Please enter a number:')
		number = int(input())
		break
	except:
		print('You must enter an integer. Please try again.')
		continue

counter = 0

while number != 1:
    number = collatz(number)
    print(number)
    counter += 1

print('Finished in ' + str(counter) + ' steps.')
def listToString(oldList):
	newString = ''

	for i in range(len(oldList)):
		if i != len(oldList) - 1:
			newString = newString + oldList[i] + ', '
		else:
			newString = newString + 'and ' + oldList[i]

	return newString

userList = []
while True:
	print('Enter item ' + str(len(userList) + 1) +
		' (or enter nothing to stop):')
	item = input()
	if item == '':
		break
	userList.append(item)

print(listToString(userList))
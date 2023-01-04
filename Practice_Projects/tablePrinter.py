def printTable(tableData):
	colWidth = [0] * len(tableData)		# [0, 0, 0]
	colLength = len(tableData[0])

	# Determine the length of each column
	for x in range(len(tableData)):
		colWidth[x] = len(max(tableData[x], key=len))

	# Loop through the 'tableData' and print each row
	for y in range(colLength):
		for x in range(len(tableData)):
			print(tableData[x][y].rjust(colWidth[x]) + ' ', end='')
		print()

tableData = [['apples', 'oranges', 'cherries', 'banana'],
             ['Alice', 'Bob', 'Carol', 'David'],
             ['dogs', 'cats', 'moose', 'goose']]

printTable(tableData)
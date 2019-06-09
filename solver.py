board = [
		["....82.4."],
        [".3......7"],
        [".98.4...1"],
        ["8....61.."],
        ["7.39.84.5"],
        ["..41....8"],
        ["5...9.87."],
        ["2......3."],
        [".7.85...."]
    ]

def main():
	convertBoard()
	print("Value at position (6,5) is: ", getValue(6,5))
	solve(6,5)
	


def printBoard():
	for row in board:
		print(row)

# convert board so that list contents are 
# individual characters rather than a single string
# doing list(line) will create another nested list [[]]
def convertBoard():
	for idx,row in enumerate(board):
		for line in row:
			convertedRow = list(line)
			board[idx] = convertedRow


# checks what numbers exist in a positions
# respective row, column and 3x3 grid
def solve(x,y):
	
	# row values
	rowValues = board[y]
	#print("Row:",rowValues)

	# Column values
	colValues = []
	for i in range(0,9):
		colValues.append(board[i][x])
	#print("Col:", colValues)

	# Grid values
	gridValues = []

	gridX = x // 3
	gridY = y // 3

	gridX *= 3
	gridY *= 3

	for i in range(0,3):
		for j in range(0,3):
			gridValues.append(getValue(gridX + i, gridY + j))

	print("Valid numbers are: ", getPossibilities(rowValues, colValues, gridValues))

def getPossibilities(lstA, lstB, lstC):
	# generate list of strings from 1 to 9
	possibilities = [str(x) for x in range(1,10)]

	# probably better to use sets in the future
	# https://www.geeksforgeeks.org/python-set-operations-union-intersection-difference-symmetric-difference/ 
	for i in range(0,9):
		if lstA[i] in possibilities:
			possibilities.remove(lstA[i])
		if lstB[i] in possibilities:
			possibilities.remove(lstB[i])
		if lstC[i] in possibilities:
			possibilities.remove(lstC[i])
	return possibilities


def getValue(x,y):
	return board[y][x]

main()
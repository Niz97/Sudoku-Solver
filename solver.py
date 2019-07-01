import copy

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
	printBoard()

	fill()

	print()
	printBoard()
	
	


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



			
def getPossibilities(x,y):

	if board[x][y] != ".":
		return False

	rowValues = board[x]
	# print("Row", rowValues)

	colValues = []
	for i in range(0,9):
		colValues.append(board[i][y])
	# print("Col", colValues)

	# Grid values
	gridValues = []

	gridX = (x // 3) * 3
	gridY = (y // 3) * 3

	for i in range(0,3):
		for j in range(0,3):
			gridValues.append(getValue(gridY + j, gridX + i))
	# print("Grid", gridValues)

	# generate list of strings from 1 to 9
	possibilities = [str(x) for x in range(1,10)]

	# probably better to use sets in the future
	# https://www.geeksforgeeks.org/python-set-operations-union-intersection-difference-symmetric-difference/ 
	for i in range(0,9):
		if rowValues[i] in possibilities:
			possibilities.remove(rowValues[i])
		if colValues[i] in possibilities:
			possibilities.remove(colValues[i])
		if gridValues[i] in possibilities:
			possibilities.remove(gridValues[i])
	return possibilities


def guess(x,y):
	pos = getPossibilities(x,y)
	global board
	

	if pos != False:
		if len(pos) != 0:
			print("X,Y", x,y)
			print(pos)
			print("Length:", len(pos))	
			board[x][y] = pos[0]
	
def fill():
	for i in range(0,9):
		for j in range(0,9):
			guess(i,j)



def isFull():
	for row in board:
		for col in row:
			if col == ".":
				return False

	return True

def getValue(x,y):
	return board[y][x]

main()
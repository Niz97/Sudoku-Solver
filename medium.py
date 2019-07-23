import copy

# easy difficulty board
board = [
		["3.2..176."],
        [".7....8.."],
        ["9..4.5.1."],
        ["..6.54..7"],
        ["........."],
        ["5..12.6.."],
        [".5.9.2..3"],
        ["..7....2."],
        [".297..5.1"]
    ]




boardPossibilities = [[ [] for i in range(9)] for j in range(9)]

# medium difficulty board
# board = [
# 		["6.9..7..."],
#         [".4.32..6."],
#         [".5.96...."],
#         ["..86...7."],
#         [".96...45."],
#         [".3...16.."],
#         [".....6.4."],
#         [".6..73.9."],
#         ["...8..5.6"]
#     ]

def main():

	convertBoard()
	generateCellPos()
	
	for i in range(100):
		fill()

	# print()
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
	pos = boardPossibilities[x][y]
	global board
	

	if pos != False:
		if len(pos) == 1:
			# print("X,Y", x,y)
			# print(pos)
			# print("Length:", len(pos))	
			board[x][y] = pos[0]
	

def cellPossibility(x,y):
	pos = getPossibilities(x,y)
	return pos

	
def generateCellPos():

	for i in range(0,9):
		for j in range(0,9):
			boardPossibilities[i][j] = cellPossibility(i,j)

def updatePossibilities(x,y):
	boardPossibilities[x][y] = getPossibilities(x,y)

def fill():
	for i in range(0,9):
		for j in range(0,9):
			guess(i,j)
			updatePossibilities(i,j)



def isFull():
	for row in board:
		for col in row:
			if col == ".":
				return False

	return True

def getValue(x,y):
	return board[y][x]

main()
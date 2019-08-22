# if you like, create a data type for a 'cell' as well

class Sudoku:

	def __init__(self, grid=None): # make grid an optional parameter
		self.grid = grid
		# constructor
		# set up a possibilities grid, first assume the board is empty,
		#  then every cell should contain ALL possible digits
		# when only one possibility remains in a cell, we'll consider it solved
		self.possibilities = []
		self.generatePossibilities()
		
		# if grid != None:
			# loop through the grid values are use 'set'
			#  to place digits on the board


	def getPossibilities(self,y,x):
		
		if self.grid[y][x] != "0":
			return False
		possibilities = {str(x) for x in range(1,10)}

		row = set(self.grid[y])
		for val in row:
			possibilities -= set(val)

		for line, ele in enumerate(self.grid):
			val = self.grid[line][x]
			possibilities -= set(val)

		# find respective 3x3 area values
		gridX = (x // 3) * 3
		gridY = (y // 3) * 3 

		gridVal = []
		for y in range(3):
			for x in range(3):
				val = self.grid[y + gridY][x + gridX]
				possibilities -= set(val)

		return list(possibilities)
	

	def generatePossibilities(self):
		for x in range(9):
			for y in range(9):
				pos = self.getPossibilities(x,y)
				self.possibilities.append(pos)


	def set(self, x, y, digit):
		# place digit on board 
		row = self.grid[y]
		newRow = row[0:x] + str(digit) + row[x+1:]
		self.grid[y] = newRow

		# eliminate 'digit' from any connected cells
		# y * 9 + x

		

	# def isSolved(self):
	# 	# has the board been solved?

	# def solveEliminatedCells(self):
	# 	# go through the board and find cells that have been fully eliminated down to 1 option
	# 	# return True if any were found, false otherwise
	def printGrid(self):
		for line in self.grid:
			print(line)

	def printPos(self):
		for pos in self.possibilities:
				print(pos)
		print(len(self.possibilities))

	def copy(self): # implement this if you want... will be handy later
		pass

testGrid = [
	"003020600",
	"900305001",
	"001806400",
	"008102900",
	"700000008",
	"006708200",
	"002609500", 
	"800203009",
	"005010300"
]

testSudoku = Sudoku(testGrid)
testSudoku.set(8,0,1)
testSudoku.printPos()

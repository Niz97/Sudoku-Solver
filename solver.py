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


def printBoard():
	for row in board:
		print(row)

# convert board so that list contents are 
# individual characters
def convertBoard():
	for idx,row in enumerate(board):
		for line in row:
			row = list(line)
			board[idx] = row

main()
from board import *
from solution import *

if __name__ == "__main__":
	
	#create board
	filename = 'test_case.txt'
	board = Board()	
	board.grid = board.load_board(filename)

	#find answer
	sol = Solution()
	board.grid = sol.solution_(board.grid)

	# load actual answer:
	filename = 'answer.txt'
	answer_board = Board()
	answer_board.grid = answer_board.load_board(filename)

	# compare 2 answers:
	if answer_board.is_same(board) == True:
		print("The solution is true ")
		board.print_board()
	else :
		print("Wrong solution")


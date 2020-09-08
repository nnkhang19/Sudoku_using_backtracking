class Solution:
	def __init__(self):
		pass

	def check_valid(self, grid, row, col, number):

		# check for row:
		for i in range(len(grid)):
			if grid[row][i] == number:
				return False

		# check for column:
		for i in range(len(grid)):
			if grid[i][col] == number:
				return False

		# check for 3x3 square:
		row = row - row % 3
		col = col - col % 3

		for i in range(3):
			if grid[row + i][col + i] == number:
				return False

		return True


	def safe_board(self, grid):
		for i in range(len(grid)):
			for j in range(len(grid)):
				if grid[i][j] == 0:
					return False
		return True

	def zero_slots(self, grid):
		temp = []
		for i in range(len(grid)):
			for j in range(len(grid)):
				if grid[i][j] == 0:
					temp.append((i,j))

		return temp

	def back_tracking_algo(self,grid, index):
		if self.safe_board(grid):
			return True

		if index == len(self.zero_set):
			return False

		row, col = self.zero_set[index]

		for i in range(1, 10):
			if self.check_valid(grid, row, col, i):
				grid[row][col] = i
				if self.back_tracking_algo(grid, index + 1) == True:
					return True
				grid[row][col] = 0

		return False
				

	def solution_(self, grid):
		self.zero_set = self.zero_slots(grid)
		result = self.back_tracking_algo(grid, 0)
		
		return grid


	

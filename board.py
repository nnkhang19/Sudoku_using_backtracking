class Board:
	def __init__(self):
		self.grid = []

	def load_board(self, filename):
		with open(filename, 'r') as file:
			while True:
				line = file.readline()
				if not line:
					break
				row  = list(map(int, line.split()))
				self.grid.append(row)

		return self.grid

	def print_board(self):
		for i  in range (len(self.grid)):
			R = ""
			if i % 3 == 0:
				print("----------------------")
			for j in range(len(self.grid[0])):
				if j % 3 == 0:
					R += "| "
			
				R += str(self.grid[i][j]) + " "
			print(R)

	def is_same(self, other):
		for i in range(len(self.grid)):
			for j in range(len(self.grid)):
				if self.grid[i][j] != other.grid[i][j]:
					return False
		return True


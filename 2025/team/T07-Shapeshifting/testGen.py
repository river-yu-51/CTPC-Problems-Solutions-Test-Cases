import random

pieces = ["Bishop", "Knight", "Rook"]

m = random.randint(50, 50)
n = random.randint(50, 50)

f = open("test.txt", 'w')

f.write(random.choice(pieces))
f.write('\n' + str(m) + ' ' + str(n) + '\n')

obstaclePercent = 65

grid = []
for i in range(m):
	gridline = []
	for j in range(n):
		if (i + j) % 3 == 0:
			gridline.append('.')
		else:
			gridline.append('o')
	grid.append(gridline)

grid[0][0] = '.'
grid[m - 1][n - 1] = '.'

for i in range(m):
	gridStr = ""
	for j in range(n):
		gridStr += (grid[i][j])
	f.write(gridStr + '\n')

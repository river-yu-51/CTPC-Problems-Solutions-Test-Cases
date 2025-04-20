# Get inputs
[w, h] = [int(x) for x in input().split()]

grid = [] # store grid
gridCosts = [] # store minimum moves per cell
gridSearched = [] # store whether or not each cell has been traversed

# Assign filler values to the above arrays
for i in range(h):
	grid.append(list(input()))
	gridCosts.append([10**10] * w)
	gridSearched.append([False] * w)

gridCosts[0][0] = 0 # you start in top left so it takes no moves to reach that cell

# Function to check if a landing square is valid (within the boundaries and is not an obstacle)
def isValid(y, x):
	return (x < w and x >= 0 and y < h and y >= 0 and grid[y][x] != '#')

def move(y, x, cost):
	newSquares = [] # tracks new squares that have not been visited
	# Bishop movement pattern
	bmovements = [
		[-1, -1],
		[-1, 1],
		[1, -1],
		[1, 1]
	]
	
    # Check all movement directions
	for i in range(4):
		moveDist = 1 # current move distance
		searching = True # stores whether or not you're still searching - search ends when you hit an obstacle or edge
		# While the next move in the current direction is valid, see if reaching that square through the square you are currently on is a new faster route. If it is, update the gridCosts array. Move on to the next square in the diagonal afterwards
		while searching:
			# coordinates of next square
			newY = y + bmovements[i][1]*moveDist
			newX = x + bmovements[i][0]*moveDist
			if isValid(newY, newX):
				gridCosts[newY][newX] = min(gridCosts[newY][newX], (cost + 1))
				# Add unvisited squares to the newSquares array
				if not gridSearched[newY][newX]: newSquares.append([newY, newX])
				gridSearched[newY][newX] = True
			else:
				searching = False
			moveDist += 1
	
	return newSquares

queue = [[0, 0]] # queue of squares that need distance updating

# While the queue is nonempty, update the minimum number of moves for any square that is reachable through the first square in the queue. Remove the first element and add any new elements as needed
while len(queue) > 0:
	nextNode = queue.pop(0)
	queue += move(nextNode[0], nextNode[1], gridCosts[nextNode[0]][nextNode[1]])

# Output results
if gridCosts[-1][-1] == 10**10: print(-1)
else: print(gridCosts[-1][-1])

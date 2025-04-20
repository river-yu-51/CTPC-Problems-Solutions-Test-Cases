piece = input()
[m, n] = [int(x) for x in input().split()]

grid = []
gridCosts = []
gridSearched = []
empty = 0

for i in range(m):
	grid.append(list(input()))
	gridCosts.append([1000] * n)
	gridSearched.append([False] * n)

for i in range(m):
    for j in range(n):
        if grid[i][j] == 'o':
            gridSearched[i][j] = True
        else:
            empty += 1

gridCosts[0][0] = 0

def isValid(y, x):
	return (x < n and x >= 0 and y < m and y >= 0 and grid[y][x] != 'o')

def move(y, x, directions, maxDist, cost):
    for d in directions:
        newY = y + d[0]
        newX = x + d[1]
        dist = 0
        while isValid(newY, newX) and dist < maxDist:
            gridCosts[newY][newX] = min(gridCosts[newY][newX], gridCosts[y][x] + cost)
            newY += d[0]
            newX += d[1]
            dist += 1

def knightMove(y, x):
    directions = [[-1, -2], [-1, 2], [1, -2], [1, 2],
                  [-2, -1], [2, -1], [-2, 1], [2, 1]]
    cost = 2
    if "Knight" in piece:
        cost -= 1
    move(y, x, directions, 1, cost)

def bishopMove(y, x):
    directions = [[-1, -1], [-1, 1], [1, -1], [1, 1]]
    cost = 2
    if "Bishop" in piece:
        cost -= 1
    move(y, x, directions, 1000, cost)

def rookMove(y, x):
    directions = [[-1, 0], [1, 0], [0, -1], [0, 1]]
    cost = 2
    if "Rook" in piece:
        cost -= 1
    move(y, x, directions, 1000, cost)
    
def nextCell():
    bestCoord = [0, 0]
    bestVal = 1000
    for i in range(m):
        for j in range(n):
            if not gridSearched[i][j] and gridCosts[i][j] < bestVal:
                bestCoord = [i, j]
                bestVal = gridCosts[i][j]
    return bestCoord
    
for i in range(empty):
    nextCoord = nextCell()
    knightMove(nextCoord[0], nextCoord[1])
    bishopMove(nextCoord[0], nextCoord[1])
    rookMove(nextCoord[0], nextCoord[1])
    gridSearched[nextCoord[0]][nextCoord[1]] = True
    
print(gridCosts[-1][-1])

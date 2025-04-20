import copy

# Get inputs
[C, m, n] = [int(x) for x in input().split()]

candies = [] # hold candy coordinates
candyPaths = [] # hold paths of candies to get to each candy (AKA what other candies you can collect on your way towards a particular candy)
maxCandySteps = [0] * C # hold maximum number of steps per candy

# Assign inputs
for i in range(C):
	candies.append([int(x) for x in input().split()])
	candyPaths.append([])
	maxCandySteps[i] = 0

# Compare every pair of candies: if candy A is not lower and not to the right of candy B, then you can collect A first and then B in the same pass, so we add A to B's candy path - paths will be in reverse order
# Candies from now on are essentially represented by their index in the candies array
for i in range(C):
	for j in range(C):
		if i != j and candies[i][0] <= candies[j][0] and candies[i][1] <= candies[j][1]:
			candyPaths[j].append(i)

# Fill maxCandySteps array by seeing if there is a longer candy path that leads to the candy j. If there is, update maxCandySteps index j
for i in range(C):
	for j in range(C):
		for k in range(C):
			if k in candyPaths[j]:
				maxCandySteps[j] = max(maxCandySteps[j], maxCandySteps[k] + 1)

maxCandies = max(maxCandySteps) # max candies through any path
optimalLastCandies = [] # store all possible ending candies that give the maximal amount

# add candy to optimalLastCandies if there exists a path ending at that candy with maxCandies total candies
for i in range(C):
	if maxCandySteps[i] == maxCandies:
		optimalLastCandies.append(i)

# Find optimal paths (last candies) and store them
optimalPaths = []
for optimalLastCandy in optimalLastCandies:
	optimalPaths.append([optimalLastCandy])

# Now it's time to generate the paths will get the maximum number of candies. We do this by updating the next candy one step at a time, for a total of maxCandies passes
for i in range(maxCandies):
	# At this point, optimalPaths is filled with last pass's optimal paths
	newPaths = [] # store new paths for the next pass
	# Check each path and each candy to see if said candy can be added to the path
	for path in optimalPaths:
		for k in range(C):
			# Add kth candy to path if kth candy is next in line in the current path you're looking at. Copy and store the new path in the newPaths array
			if k in candyPaths[path[-1]] and maxCandySteps[k] == maxCandySteps[path[-1]] - 1:
				newPath = copy.deepcopy(path)
				newPath.append(k)
				newPaths.append(newPath)
	# Reset the optimalPaths array and assign it to the previous pass's newPaths array
	optimalPaths.clear()
	for path in newPaths:
		optimalPaths.append(path)

pathCount = 0 # hold number of paths

# Factorial function
def factorial(n):
	if n == 0: return 1
	if n == 1: return 1
	return n * factorial(n - 1)

# Choose function
def nCk(n, k):
	return factorial(n) // factorial(k) // factorial(n - k)

# Loop through every path of candies in optimalPaths to find the number of ways to traverse the path (branches)
for path in optimalPaths:
	# Get coordinates of each candy
	for i in range(len(path)):
		path[i] = candies[path[i]]
	# Add start and end points (candies were in reverse order when we made the paths)
	path.append([0, 0])
	path.insert(0, [m - 1, n - 1])
	currentPathBranches = 1 # hold number of branches
	# "Paths in boards" formula to efficiently calculate number of paths. Essentially it multiplies together every possible count of paths between two adjacent candies in the path
	for i in range(len(path) - 1):
		length = path[i][0] - path[i + 1][0]
		width = path[i][1] - path[i + 1][1]
		currentPathBranches *= nCk(length + width, width)
	pathCount += currentPathBranches # update total path count

# Output results
print(maxCandies + 1)
print(pathCount)

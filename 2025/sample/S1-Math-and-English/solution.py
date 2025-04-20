# Get inputs
N = int(input())

solutions = [] # array to store results

# Loop through each question, checking whether it's math or english
for i in range(N):
	problem = input().split()
	# For math problems, convert the arguments to integers and append their sum to solutions
	if problem[0] == 'M':
		solutions.append(int(problem[1]) + int(problem[2]))
	# For english problems, concatenate the arguments and append that result string to solutions
	else:
		solutions.append(problem[1] + problem[2])

# Output results
for solution in solutions:
	print(solution)

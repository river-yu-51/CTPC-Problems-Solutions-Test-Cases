# Get T and Q
[T, Q] = [int(x) for x in input().split()]

questions = [] # array to hold questions

# Add inputs to questions array
for i in range(Q):
	nextQuestion = input().split()
	questions.append([int(x) for x in nextQuestion[1:]])

# Create a tab array that stores the best possible total score of questions from minute 0 to minute i (0 <= i <= T), accessed by index
tab = [0] * (T + 1)

# Loop through the tab array, updating indices from left to right
for i in range(1, T + 1):
	# For each index, check all the questions - if the question start time is at least i, check if the maximum score for the end minute can be increased by answering said question. If it can, than update the tab array
	for question in questions:
		if question[0] >= i:
			tab[question[1]] = max(tab[question[1]], tab[i - 1] + question[2])

# Output the maximum value in the tab array - this corresponds to the maximum possible score across all minutes
print(max(tab))

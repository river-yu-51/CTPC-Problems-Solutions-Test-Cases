# Get inputs
N = int(input())
marks = input().split()
exam = int(input())

testTotal = 0 # store total marks from tests

# Get test total
for mark in marks:
	testTotal += int(mark)

# Get the average of the tests and then multiply it by a weight of 0.7
testTotal /= len(marks)
testTotal *= 0.7

# Add the exam with weight 0.3
testTotal += exam * 0.3

# Output (rounded) result
print(round(testTotal))

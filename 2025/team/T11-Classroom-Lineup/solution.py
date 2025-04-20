# Get inputs
[N, Q, k] = [int(x) for x in input().split()]
people = input().split()

nums = [] # store everybody by 1-indexed lexicographical position (which I'll refer to as 1ILP from now on)
friends = [] # store friendships

for i in range(Q):
	friends.append(input().split()) # add friends to friends array

people.sort() # sort people lexicographically

# Replace people by 1ILP
for friendPair in friends:
	friendPair[0] = people.index(friendPair[0]) + 1
	friendPair[1] = people.index(friendPair[1]) + 1

# For everyone without a friend, add their 1ILP as an array to the nums array
for i in range(N):
	friended = False
	for friend in friends:
		if (i + 1) in friend: friended = True
	if not friended: nums.append([i + 1])

# Add everyone with a friend to the nums array, again with 1ILP. Do this twice: once for each order
for friend in friends:
	nums.append(friend)
	nums.append([friend[1], friend[0]])

nums.sort() # sort everyone

# Define factorial function, recursively
def factorial(n):
	if n == 1 or n == 0: return 1
	else: return n * factorial(n - 1)

# Count the number of permutations, given the number of individuals and pairs. This works by arranging each pair and individual as single elements and then multiplying the total by 2 for each pair due to the two orders
def countPermutations(individuals, pairs):
	return factorial(individuals + pairs) * 2 ** pairs

# Create function that stores the breakpoints of when the first element in lexicographical order switches
def constructBreakpoints(arr):
	bkps = [] # hold breakpoints
	individuals = 0 # store number of individuals
	pairs = 0 # store number of pairs
	
	# Count individuals and pairs
	for a in arr:
		if len(a) == 2: pairs += 1
		else: individuals += 1
		
	pairs //= 2 # since pairs are stored twice (once in each order, divide pairs by 2)
	
    # Loop through array, if the next element is a pair then get the number of permutations without that pair. Otherwise, the next element must have been an individual, so get the number of permutations without that individual. This builds up an array that holds the difference in number of permutations between every two elements
	for a in arr:
		if len(a) == 2: bkps.append(countPermutations(individuals, pairs - 1))
		else: bkps.append(countPermutations(individuals - 1, pairs))

    # Create the sum left to right so instead of differences it stores totals
	for i in range(1, len(arr)):
		bkps[i] += bkps[i - 1]

	return bkps # return breakpoints

kthPermutation = [] # store the kth permutation

# Remove elements from nums one by one in the required order
while len(nums) > 0:
	breakpoints = constructBreakpoints(nums) # get breakpoints for remaining elements
	
    # Set the top barrier, the index of the lowest breakpoint that is greater than k
	topBarrier = len(breakpoints) - 1
	for i in range(len(breakpoints)):
		if k <= breakpoints[i]:
			topBarrier = i
			break
	
    # If the top barrier is not the first index, then remove the amount of permutations that the previous breakpoints hold from k to get ready for the next cycle
	if topBarrier != 0: k -= breakpoints[topBarrier - 1]
	# Remove the desired element from nums
	removedEl = nums[topBarrier]
	
    # If the removed element is a pair, remove the flipped version of it as well
	if len(nums[topBarrier]) == 2:
		reversed = [removedEl[1], removedEl[0]]
		nums.remove(reversed)
	
    # Remove the required element from nums and add it to kthPermutation - the desired order
	kthPermutation.append(removedEl)
	nums.remove(removedEl)

stringPermutation = "" # hold string of kthPermutation, as the output requests
for arr in kthPermutation:
	# Loop through all elements of kthPermutation and add them to the string. If an element is a pair, add both friends
	stringPermutation += people[arr[0] - 1]
	stringPermutation += " "
	if len(arr) == 2:
		stringPermutation += people[arr[1] - 1]
		stringPermutation += " "

# Output result (removing the last unneeded whitespace)
print(stringPermutation[:-1])

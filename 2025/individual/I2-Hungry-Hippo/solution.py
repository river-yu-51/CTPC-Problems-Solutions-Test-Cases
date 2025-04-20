# Get inputs
[N, Q] = [int(x) for x in input().split()]

# Store sizes of pies in the pies array
pies = [int(x) for x in input().split()]

# Function to calculate the score you can get with a specific tolerance by summing up the squares of the sizes of all eatable pies
def getScore(arr, tolerance):
	score = 0
	for pie in arr:
		if tolerance >= pie:
			score += pie ** 2
	return score

# Binary search function to efficiently find the lowest tolerance level by binary searching within a range
def binarySearch(low, high):
	# Base case - if the range is narrowed down to two integers, if the low one works, return it. Otherwise, return the higher one
	if high - low <= 1:
		if getScore(pies, low) >= Q: return low
		return high

    # Get the midpoint of the current searched range
	mid = (low + high) // 2

    # If a tolerance level equal to the midpoint of the current range works, we can eliminate the top half of the range as there is a lower value (the midpoint) that yields enough score
	if getScore(pies, mid) >= Q: return binarySearch(low, mid)
	# Otherwise, we can eliminate the bottom half of the range as no tolerance level there will yield the required score
	else: return binarySearch(mid, high)

# If an essentially infinite tolerance level (all pies have size <= 30000) doesn't work, output -1
if getScore(pies, 10**5) < Q: print(-1)
# Otherwise, binary search the whole range from 1 to the max pie size as the minimum tolerance level must be within that range
else:
	print(binarySearch(1, max(pies)))

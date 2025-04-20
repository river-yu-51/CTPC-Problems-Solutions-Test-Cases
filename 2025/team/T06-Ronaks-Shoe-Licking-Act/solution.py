# Get inputs
act = input()
S = int(input())

subActs = [] # store all sub-acts

# Fill subActs array
for i in range(S):
	subActs.append(input())

# See if a sub-act can be acted out next based on what remaining shoes are required to be licked. If it is impossible to be used next, return None. Otherwise, return the number of missing shoes
def getMissingShoes(subAct, remainingAct):
	missingShoes = 0 # store number of underscores
	if len(subAct) > len(remainingAct): return None # return None if there are not enough shoes remaining

    # Go through each shoe individually
	for i in range(len(subAct)):
		# If the next character is _, add missing shoe
		if subAct[i] == '_':
			missingShoes += 1
		# If the next character is not _ and doesn't match, this sub-act cannot be used since there are shoes that don't match so we return None
		elif subAct[i] != remainingAct[i]:
			return None

    # If we reach this point, the sub-act must be viable and thus we return the number of missing shoes
	return missingShoes

# Tab array to keep track of the minimum number of missing shoes at each index of the act (including index 0, where no acts are selected)
tab = []
for i in range(len(act) + 1):
	tab.append(10**6)

tab[0] = 0 # initialize starting value to 0

# Loop through each index of the act, trying to find fits for the next act as we go
for i in range(len(act)):
	remainingAct = act[i:] # get remaining shoes

	# Try all sub-acts
	for subAct in subActs:
		subActShoeCount = getMissingShoes(subAct, remainingAct)
		# If the sub-act is doable, update the minimum value of the end index in the tab array
		if subActShoeCount != None:
			tab[i + len(subAct)] = min(tab[i + len(subAct)], tab[i] + subActShoeCount)

# Output result
print(tab[-1])

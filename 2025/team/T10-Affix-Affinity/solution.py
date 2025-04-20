# Get inputs
K, Rn, Pn, Sn, P, S = [int(x) for x in input().split()]
counts = [Rn, Pn, Sn] # affix counts

minLengthAll = 10**10 # hold absolute minimum length

totalAffixSet = [] # hold affixes

# Add affixes to their respective sets
# Also note that the affix makeup doesn't matter, it's just the length
for i in range(3):
	nextAffixSet = [] # temporary array to store affixes
	for j in range(counts[i]):
		nextAffix = input().split()
		length = len(nextAffix[0])
		score = int(nextAffix[1])
		nextAffixSet.append([score, length])
	totalAffixSet.append(sorted(nextAffixSet))
	
affixDicts = [{}, {}, {}] # dictionaries for each set of words, in the format score:length

for i in range(3):
	index = 0
	for a in totalAffixSet[i]:
		if a[0] not in affixDicts[i]:
			affixDicts[i][a[0]] = a[1] # since the affixes are in sorted order, if two affixes have the same score, this only stores the shorter one

rtd = affixDicts[0] # root dict
pfxd = affixDicts[1] # prefix dict
sfxd = affixDicts[2] # suffix dict

def dpPts(target, ptsDict, maxUse):
	tab = [] # initialize 2d dp array with the rows as used affix count and the cols as points. Entries indicate the shortest length to get said points
	for i in range(maxUse + 1):
		tab.append([10**6] * (target + 1))
		
	tab[0][0] = 0
	
	for i in range(1, maxUse + 1):
		for j in range(target + 1):
			for k in range(j):
				if (j - k) in ptsDict: tab[i][j] = min(tab[i][j], tab[i - 1][k] + ptsDict[j - k]) # check all earlier entries in the previous row and try adding an affix

	fullMin = [] # get the minimum length of any column
	for j in range(target + 1):
		currentMin = 10**6
		for i in range(maxUse + 1):
			currentMin = min(currentMin, tab[i][j])
		fullMin.append(currentMin)
	
	return fullMin

prefixMins = dpPts(K, pfxd, P)
suffixMins = dpPts(K, sfxd, S)

best = 3*10**6

for i in range(len(prefixMins)):
	bscore = i # base score
	blength = prefixMins[i] # base length

	for key in rtd:
		cscore = bscore + key # case score
		clength = blength + rtd[key] # case length

		remaining = K - cscore # remaining length needed from suffixes

		if remaining >= 0:
			best = min(best, clength + suffixMins[remaining])

print(best)

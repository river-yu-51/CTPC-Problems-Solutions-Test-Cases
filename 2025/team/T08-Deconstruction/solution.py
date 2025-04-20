n = int(input().split()[1]) # get rows

linearSchematic = [] # grid doesn't actually do anything here, we can flatten the schematic and store all strengths in an array
detonations = 0 # hold detonation count

for i in range(n):
	linearSchematic += [int(x) for x in input().split()] # add row to schematic

linearSchematic.sort(reverse=True) # sort schematic, greatest to least

detonateTestNum = 0 # initialize detonate test number, details below

# Cycle through the schematic, one tile at a time, setting that tile to the detonateTestNum. Its strength will be equal to target. Then, we check if detonating only tiles with index detonateTestNum or lower (that is, tiles with strength target or higher) will demolish the whole building.
while True:
	totalCollateralDetonation = 0
	detonateTestNum += 1
	if detonateTestNum == len(linearSchematic): break
	target = linearSchematic[detonateTestNum]
	for i in range(detonateTestNum):
		totalCollateralDetonation += (linearSchematic[i] - target)
	if totalCollateralDetonation >= target:
		break

linearSchematic = linearSchematic[0:detonateTestNum] # get only tiles that you need to detonate, every other tile will be detonated by collateral damage

excessStrength = 0 # get the total excess strength of all tiles with strengths higher than the target
for strength in linearSchematic:
	excessStrength += (strength - linearSchematic[-1])

detonations += excessStrength # detonate all tiles with strength higher than target to the point where they all have equal strength values to the (detonate test num)th tile

S = linearSchematic[-1] - excessStrength # strength of all tiles after excess strength has been removed
L = len(linearSchematic) # total tiles with strength S after the excess removal

fullDetonations = S // (L + 1) # detonating each tile once will do a total of L + 1 damage to each one (since it gets hit L - 1 times with 1 damage and once with 2 damage), this is the total number of cycles to detonate everything

detonations += fullDetonations * L # add the previous number of detonations times L (since each cycle detonates L tiles) to the total detonations

S -= fullDetonations * (L + 1) # update S

detonations += S # remaining tiles all need to be damaged once since none can now be demolished through collateral damage alone, add that amount to detonations

# Output result
print(detonations)

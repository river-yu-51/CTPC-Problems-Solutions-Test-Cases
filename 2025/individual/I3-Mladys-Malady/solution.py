# Get inputs
target = (input().split())[0]
line2 = input().split()
P = int(line2[0])
N = int(line2[1])

supplies = {} # supplies dict - key: name, value: quantity
storeTypes = input().split()
storeQuants = input().split()

for i in range(P):
    supplies[storeTypes[i]] = int(storeQuants[i])

recipes = {} # recipes dict - key: product, value: [reactant1, reactant2]
for i in range(N):
    reaction = input().split()
    recipes[reaction[2]] = reaction[:2]

queue = [target] # priority queue of remaining needed potions
requiredDict = {target: 1}
spent = 0 # track spent potions
ended = False

while len(queue) > 0: # pop elements one at a time from the queue, popping from the front and adding to the back
    first = queue.pop(0)
    if first in supplies and supplies[first] >= requiredDict[first]:
        supplies[first] -= requiredDict[first]
        spent += requiredDict[first]
        requiredDict[first] = 0
    elif first in supplies:
        requiredDict[first] -= supplies[first]
        supplies[first] = 0
    
    if requiredDict[first] > 0:
        if first not in recipes:
            ended = True
            print(-1)
            break
        reactants = recipes[first]
        for i in range(2):
            if reactants[i] not in requiredDict: requiredDict[reactants[i]] = requiredDict[first]
            else: requiredDict[reactants[i]] += requiredDict[first]
            queue.append(reactants[i])
        requiredDict[first] = 0

if not ended: print(spent)

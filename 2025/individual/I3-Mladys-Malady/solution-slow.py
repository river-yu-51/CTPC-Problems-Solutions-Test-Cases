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
spent = 0 # track spent potions
ended = False

while len(queue) > 0: # pop elements one at a time from the queue, popping from the front and adding to the back
    first = queue.pop(0)
    if first in supplies and supplies[first] > 0:
        supplies[first] -= 1
        spent += 1
    elif first not in recipes:
        ended = True
        print(-1)
        break
    else:
        reactants = recipes[first]
        for i in range(2):
            if reactants[i] in supplies and supplies[reactants[i]] > 0:
                supplies[reactants[i]] -= 1
                spent += 1
            else:
                queue.append(reactants[i])
    
if not ended: print(spent)

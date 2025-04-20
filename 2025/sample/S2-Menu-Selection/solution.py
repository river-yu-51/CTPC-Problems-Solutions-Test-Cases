# Get inputs
line1 = input().split()
k, rw = int(line1[0]), int(line1[1])
line2 = [int(x) for x in input().split()]
# Sort weights in reverse order
line2.sort(reverse=True)

total = 0 # hold total weight

# Get next big mac weight (if it exists)
while len(line2) > 0:
    # Using a greedy approach we always select the first available big mac and add it to our total weight since it's sorted in reverse order and thus must be the heaviest
    currentElement = line2[0]
    total += currentElement
    # Remove all other big macs that are now no longer selectable (does not satisfy the required weight difference)
    index = 0
    while index < len(line2):
        if line2[index] > currentElement - rw:
            line2.pop(index)
            index -= 1
        index += 1

# Output result
print(total)

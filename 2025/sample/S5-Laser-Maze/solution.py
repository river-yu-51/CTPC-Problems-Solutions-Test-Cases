# Get inputs
[N, W, H] = [int(x) for x in input().split()]
# Declare empty arrays to hold lasers based on what direction the laser is pointing
# Positive: bottom right to top left (positive slope)
# Negative: bottom left to top right (negative slope)
[horizontal, vertical, positive, negative] = [[], [], [], []]

baseLaser = 0 # holds number of laser tiles

# Loop through all lasers, get their slope, and add the lasers to the correct array based on their slope
# Also adds the total number of laser tiles to the baseLaser variable. This will overcount which we need to solve with PIE (principle of inclusion-exclusion) later as looping through every array tile to see if it's a laser will be too slow
for _ in range(N):
    laser = [int(x) for x in input().split()]
    rise = laser[3] - laser[1]
    run = laser[2] - laser[0]
    # For lasers that only contain one square (a corner), append them to their appropriate slope array
    if rise == 0 and run == 0:
        if laser == [0, 0, 0, 0] or laser == [W - 1, H - 1, W - 1, H - 1]:
            negative.append(laser)
        else:
            positive.append(laser)
        baseLaser += 1
    # Horizontal laser
    elif rise == 0:
        horizontal.append(laser)
        baseLaser += W
    # Vertical laser
    elif run == 0:
        vertical.append(laser)
        baseLaser += H
    # Diagonal laser
    elif rise // run == 1:
        positive.append(laser)
        baseLaser += abs(laser[2] - laser[0]) + 1
    # Diagonal laser
    else:
        negative.append(laser)
        baseLaser += abs(laser[2] - laser[0]) + 1

intersections = {} # hold number of intersection detections per intersection point: this number will be greater than 1 for points with 3 or more lasers intersecting

# Function to add coordinate instance to intersection
def addCoord(c):
    if c in intersections:
        intersections[c] += 1
    else:
        intersections[c] = 1

# Function to calculate the intersection point of two diagonal lasers (if it exists)
def solveSys(sum, diff):
    if (sum + diff) % 2 == 1: return None
    return [(sum + diff) // 2, (sum - diff) // 2]

# Loop through every possible combination of intersections. This includes horizontal-vertical, horizontal-diagonal, vertical-diagonal, and diagonal-diagonal
# For each pair of lines, check if they intersect, and if they do, find their intersection point and call addCoord on it
for h in horizontal:
    for v in vertical:
        coord = str(v[0]) + '_' + str(h[1])
        addCoord(coord)

    for p in positive:
        if max(p[1], p[3]) >= h[1] and min(p[1], p[3]) <= h[1]:
            coord = str(p[0] - p[1] + h[1]) + '_' + str(h[1])
            addCoord(coord)

    for n in negative:
        if max(n[1], n[3]) >= h[1] and min(n[1], n[3]) <= h[1]:
            coord = str(n[0] + n[1] - h[1]) + '_' + str(h[1])
            addCoord(coord)

for v in vertical:
    for p in positive:
        if max(p[0], p[2]) >= v[0] and min(p[0], p[2]) <= v[0]:
            coord = str(v[0]) + '_' + str(v[0] - (p[0] - p[1]))
            addCoord(coord)
    
    for n in negative:
        if max(n[0], n[2]) >= v[0] and min(n[0], n[2]) <= v[0]:
            coord = str(v[0]) + '_' + str(n[0] + n[1] - v[0])
            addCoord(coord)

for p in positive:
    for n in negative:
        unparsed = solveSys(n[0] + n[1], p[0] - p[1])
        if unparsed != None and 0 <= unparsed[0] and unparsed[0] < W and 0 <= unparsed[1] and unparsed[1] < H:
            coord = str(unparsed[0]) + '_' + str(unparsed[1])
            addCoord(coord)

# Store the number of intersections of each type: 2 lasers, 3 lasers, 4 lasers - they would be counted 1 time, 3 times, and 6 times respectively in the intersections array
[int2, int3, int4] = [0, 0, 0]

# Count the number of each type of intersection
for i in intersections:
    if intersections[i] == 1:
        int2 += 1
    elif intersections[i] == 3:
        int3 += 1
    else:
        int4 += 1

# Remove overcount and output result
print(W * H - (baseLaser - int2 - 2*int3 - 3*int4))

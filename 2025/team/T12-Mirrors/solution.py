# Get inputs
[m, n] = [int(x) for x in input().split()]
[re, ce] = [int(x) - 1 for x in input().split()]
coord = [re, ce]

grid = [] # store grid
visited = [] # store visited tiles

for i in range(m):
    grid.append(list(input())) # populate grid from input
    visited.append([False] * n) # initialize all visited values to false

directions = { 'u': [-1, 0], 'r': [0, 1], 'd': [1, 0], 'l': [0, -1] } # movement definitions of each direction
slashSwitch = { 'u': 'r', 'r': 'u', 'd': 'l', 'l': 'd' } # direction change of slash for all directions
backslashSwitch = { 'u': 'l', 'r': 'd', 'd': 'r', 'l': 'u' } # direction change of backslash for all directions
direction = None # intialize direction

# Assign direction based on light start location
if re == 0: direction = 'd' # top row -> light starts going down
elif ce == 0: direction = 'r' # left side -> light starts going right
elif re == m - 1: direction = 'u' # bottom row -> light starts going up
else: direction = 'l' # right side -> light starts going left

history = [] # hold visited tiles
cornerHistory = [] # hold visited corners

# Function that calculates area of a polygon in the coordinate grid based on the Shoelace Theorem
def shoelace(corners):
    cumulative1 = 0
    cumulative2 = 0
    for i in range(len(corners)):
        cumulative1 += corners[i][1] * corners[i - 1][0]
        cumulative2 += corners[i][0] * corners[i - 1][1]

    return abs(cumulative1 - cumulative2) // 2

# Move the light beam one step at a time and stop if and only if it either hits itself or if it travels off the map
while True:
    # If the current coordinate has been visited, end the loop
    if visited[coord[0]][coord[1]]:
        cutoff = history.index(coord) # don't add the current coordinate to the history array, instead find the last time it was added and delete everything before that from history and cornerHistory, so only coordinates that form the polygon remain
        history = history[cutoff:]
        cornerHistory = cornerHistory[cutoff:]
        cornerHistory = [x for x in cornerHistory if x] # remove non-corners from cornerHistory
        cornerHistory.append(coord) # add current coordinate to cornerHistory, as it can form a corner. Note that for the purpose of the shoelace theorem, it doesn't matter if this corner is included twice.
        area = shoelace(cornerHistory) # get area of polygon with the shoelace theorem

        # Output the number of lattice points inside the polygon by rearranging Pick's Theorem for area, and break out of the loop
        print(area + 1 - len(history) // 2)
        break
    
    # If the program reaches this point, it must have not seen the current coordinate yet

    history.append([coord[0], coord[1]]) # add coordinate to history
    visited[coord[0]][coord[1]] = True # set the visited value of the current coordinate to true

    # If the current tile is / or \, the light must have hit a mirror and now creates a corner in the polygon, switch the direction of light as required
    # If the current tile is not / or \, it must have been # so append None to the cornerHistory (will be removed later, it just helps to have filler elements to cut the history at the right index later)
    if grid[coord[0]][coord[1]] == '/':
        direction = slashSwitch[direction]
        cornerHistory.append([coord[0], coord[1]])
    elif grid[coord[0]][coord[1]] == '\\':
        direction = backslashSwitch[direction]
        cornerHistory.append([coord[0], coord[1]])
    else:
        cornerHistory.append(None)

    # Move coordinate
    coord[0] += directions[direction][0]
    coord[1] += directions[direction][1]

    # If the coordinate is off the grid, then the light must have escaped before hitting itself and thus we output -1 and break out of the loop
    if coord[0] < 0 or coord[1] < 0 or coord[0] >= m or coord[1] >= n:
        print(-1)
        break

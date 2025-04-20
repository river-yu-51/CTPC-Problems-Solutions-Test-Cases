# Get inputs
[N, C] = [int(x) for x in input().split()]
[start, end] = [x for x in input().split()]

adjacencyMap = {} # map of which nodes can be reached from each node in a single flight
flightLengths = {} # map with the length of each flight

for _ in range(N):
    # Get inputs for each flight
    [fstart, fend, ftime] = [x for x in input().split()]
    # Add cities to map if they do not yet exist
    if fstart not in adjacencyMap: adjacencyMap[fstart] = []
    if fend not in adjacencyMap: adjacencyMap[fend] = []
    # Add flight to adjacencyMap
    adjacencyMap[fstart].append(fend)
    # Add flight time with flight id (start and end points) to flightLengths
    flightLengths[str(fstart) + '_' + str(fend)] = int(ftime)

# Function to pick next node to analyze
def pickNextNode(q, dists):
    minDist = 10**15 # initialize minimum distance
    minNode = 0 # initialize minimum distance node index

    # Check all elements of q, if their distance is the lowest seen so far, update minDist and minNode accordingly
    for i in range(len(q)):
        if dists[q[i]] < minDist:
            minDist = dists[q[i]]
            minNode = i

    return minNode # return minimum distance index

# Dijkstra's algorithm for finding shortest path in a weighted graph
def dijkstras(graph, startNode, endNode, times):
    explored = { x:False for x in graph } # keeps track of which nodes have been visited
    minDists = { x:10**15 for x in graph } # keeps track of the minimum distance of each node from the start node
    minDists[startNode] = 0 # set start node distance to 0
    q = [startNode] # initialize queue of nodes that need to be explored

    # While the queue isn't empty and the end node isn't explored yet, find the optimal node to explore and explore it
    while len(q) > 0 and not explored[endNode]:
        currentNode = q.pop(pickNextNode(q, minDists)) # get best node to explore (lowest distance)
        explored[currentNode] = True # set explored to true for that node

        # Update the minimum distance of every neighbor connected to the currently explored node if they have not been explored, as if a node has been explored it must already have the minimum distance
        for neighbor in graph[currentNode]:
            if not explored[neighbor]:
                minDists[neighbor] = min(minDists[neighbor], minDists[currentNode] + times[str(currentNode) + '_' + str(neighbor)])
                if neighbor not in q: q.append(neighbor) # If a neighbor isn't in the queue, add it

    # Return the minimum distance of the destination node
    return minDists[endNode]

maxMinTime = 0 # hold the maximum min time of Rauson for every attempted flight disable

for flight in flightLengths:
    flightLengths[flight] += 10**15 # for every flight, "disable" it by setting its wait time to an absurdly high value
    maxMinTime = max(maxMinTime, dijkstras(adjacencyMap, start, end, flightLengths)) # get minimum time of vacation
    flightLengths[flight] -= 10**15 # reset the flight's time

if maxMinTime >= 10**15: print(-1) # if any disabled flight resulted in a time of 10**15 or more, the flight must have been disconnected from the "disable"
else: print(maxMinTime) # otherwise, output result

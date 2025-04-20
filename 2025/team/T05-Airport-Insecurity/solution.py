# Get inputs
row1 = input().split()
row2 = input().split()
row3 = input().split()

N = int(row1[0])
T = int(row1[1])

limits = {} # store limits for each item

for i in range(len(row2)):
    limits[row2[i]] = int(row3[i])

orders = [] # store orders

for i in range(N):
    order = input().split()
    orders.append([order[0], int(order[1])])

def isUnderLimit(l, s): # function to see if all items are under their limit
    for key in l:
        if s[key] > l[key]:
            return False
    return True

window = [] # sliding window of orders
smuggled = {} # track order amounts
maxOrders = 0 # track current max orders

for key in limits:
    smuggled[key] = 0

# sliding window approach, add items onto the end until we exceed a limit, and then remove items at the start until it's valid again
# update window, smuggled, and maxOrders every step
for i in range(N):
    window.append(orders[i])
    smuggled[orders[i][0]] += orders[i][1]
    while not isUnderLimit(limits, smuggled):
        smuggled[window[0][0]] -= window[0][1]
        window.pop(0)
    maxOrders = max(maxOrders, len(window))

print(maxOrders)

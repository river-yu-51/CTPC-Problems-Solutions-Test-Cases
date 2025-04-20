# Get inputs
coins = input().split()
values = [1, 5, 10, 25, 100, 200] # worth of each coin

# Multiply each coin count by their value and output result
print(sum([int(coins[i]) * values[i] for i in range(6)]))

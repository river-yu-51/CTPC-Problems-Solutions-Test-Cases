N = int(input())
start = input()
downs = [int(x) for x in input().split()]

points = [0, 0]
dist = 0
possession = 0

if 'B' in start: possession += 1

for d in downs:
    dist += d
    if dist >= 50:
        points[possession%2] += 1
        dist = 0
        possession += 1
    elif d < 10:
        dist = 0
        possession += 1

print(points[0], points[1])



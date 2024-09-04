n = int(input())
coordinates = []
for i in range(n):
    x, y = map(int, input().split())
    coordinates.append((x, y))
coordinates = sorted(coordinates, key=lambda x: (x[0], x[1]))
for i in range(n):
    print(*coordinates[i])
wire = int(input())
bird = [int(i) for i in input().split()]
m = int(input())

for i in range(m):
    x, y = map(int, input().split())
    x -= 1  
    if 0 <= x < wire and 1 <= y <= bird[x]:  # Check if the shot is valid
        if x > 0:
            bird[x - 1] += y - 1

        if x < wire - 1:
            bird[x + 1] += bird[x] - y
        bird[x] = 0

for num in bird:
    print(num)

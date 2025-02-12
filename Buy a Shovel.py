k, r = map(int, input().split())
n = 1

while True:
    total_cost = n * k
    if total_cost % 10 == 0 or total_cost % 10 == r % 10:
        break
    n += 1

print(n)

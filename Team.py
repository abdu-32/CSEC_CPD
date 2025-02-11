n = int(input())
count = 0

for i in range(n):

    nums = [int(i) for i in input().split()]
    
    if sum(nums) >= 2:
        count += 1

print(count)



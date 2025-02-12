nums = int(input())
num = [int(i) for i in input().split()]
left = 0
right = nums - 1
sum1 = 0
sum2 = 0
turn = 0
while left <= right:
    if num[left] >= num[right]:
        chosen = num[left]
        left += 1
    else:
        chosen = num[right]
        right -= 1

    if turn == 0:
        sum1 += chosen
    else:
        sum2 += chosen
    turn = 1 - turn
print(sum1,sum2)

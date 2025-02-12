num = int(input())
teams = []
for i in range(num):
    a,b = map(int, input().split())
    teams.append((a,b))
count = 0

for i in range(num):
    for j in range(num):
        if i != j:  
            if teams[i][0] == teams[j][1]:
                count += 1

print(count)

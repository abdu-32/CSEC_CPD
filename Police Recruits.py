num = int(input())
police_crime = [int(i) for i in input().split()]
available_officer = 0
untreated_crime = 0

for i in range(num): 
    if police_crime[i] == -1:

        if available_officer > 0:
            available_officer -= 1
        else:
            untreated_crime += 1

    else:
        available_officer += police_crime[i]

print(untreated_crime)

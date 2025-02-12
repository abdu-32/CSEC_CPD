a1, a2, a3, a4 = map(int, input().split())
string = input()
hashMap = {'1': a1, '2': a2, '3': a3, '4': a4}
calories = 0

for char in string:
    calories += hashMap[char]
  
print(calories)

nums = int(input())
list = []
count = 0

for i in range(nums):
    num = int(input())
    list.append(num)
  
for i in range(nums-1):
    if list[i] == list[i+1]:
        continue
    elif list[i] != list[i+1]: 
        count += 1
      
print(count+1)

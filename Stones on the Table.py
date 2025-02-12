num = int (input())
colour = input()
count = 0 

for i in range(num-1):
    if colour[i] == colour[i+1]:
        count += 1
      
print(count)

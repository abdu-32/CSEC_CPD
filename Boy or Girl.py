str = input()
unique_chars = set()

for i in range(len(str)):
    unique_chars.add(str[i])
    
if len(unique_chars)%2 == 0:
    print("CHAT WITH HER!")
else:
    print("IGNORE HIM!")

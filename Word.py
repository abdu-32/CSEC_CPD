string = input()
upper = 0
lower = 0

for char in string:
    if char.islower():
        lower += 1
    elif char.isupper():
        upper += 1
      
if lower >= upper:
    print(string.lower())
elif upper > lower:
    print(string.upper())

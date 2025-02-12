s = input()
t = input()
pos = 1

for i in t:
    if pos <= len(s) and i == s[pos - 1]:
        pos += 1

print(pos)

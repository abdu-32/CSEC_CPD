s = input()

current = 'a'
total_time = 0

for char in s:
    diff = abs(ord(char) - ord(current))

    distance = min(diff, 26 - diff)
    total_time += distance
    current = char

print(total_time)

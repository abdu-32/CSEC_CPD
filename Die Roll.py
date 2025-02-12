from math import gcd

y, w = map(int, input().split())
max_roll = max(y, w)

favorable = 6 - max_roll

numerator = favorable + 1 
denominator = 6
common_divisor = gcd(numerator, denominator)
numerator //= common_divisor
denominator //= common_divisor

print(f"{numerator}/{denominator}")

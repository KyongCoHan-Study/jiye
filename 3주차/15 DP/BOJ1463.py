## 1로 만들기 ##

n = int(input())
count = 0

while n % 6 != 0:
    n //= 6
    count += 2

while n % 3 != 0:
    n //= 3
    count += 1

while n%2 != 0:
    n //= 2
    count += 1

count += n-1

print(count)
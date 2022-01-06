## 빠른 A+B ##
import sys

t = int(input())
out = 0

for _ in range(t):
    a, b = map(int, sys.stdin.readline().rstrip().split(' '))
    print(a + b)
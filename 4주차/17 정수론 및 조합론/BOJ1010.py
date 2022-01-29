## 다리 놓기 ##
'''
난이도 : 실5
체감 난이도 : 하
실행시간 제한이 있길래 혹시 몰라서 sys를 썼다,
'''

import sys

def pac(n):
    tot = 1
    while n > 0:
        tot *= n
        n -= 1
    return tot

def com(n, k):
    return pac(n) // (pac(k) * pac(n - k))


t = int(input())

for i in range(t):
    n, m = map(int, sys.stdin.readline().rstrip().split())
    print(com(m, n))

## BOJ11399 ##
'''
난이도 : 하
사용 : 그리디
'''
n = int(input())
Ptime = [int(i) for i in input().split(' ')]
Ptime.sort()
count = 0

for i in range(n):
    count += Ptime[i] * (n-i)

print(count)
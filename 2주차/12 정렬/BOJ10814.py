## 나이순 정렬 ##
'''
난이도 : 하
사용 : 퀵정렬
에러난다.. 버블로 다시 쓸거임ㅋㅋ
'''
import sys
sys.setrecursionlimit(10000000000)
def quicksort(a, left, right):
    pl = left
    pr = right
    x = a[(left + right) // 2][0]

    while pl <= pr:
        while a[pl][0] < x: pl += 1
        while a[pr][0] > x: pr -= 1
        if pl<=pr:
            a[pl], a[pr] = a[pr], a[pl]
            pl += 1
            pr -= 1

        if left < pr: quicksort(a, left, pr)
        if pl < right: quicksort(a, pl, right)

n = int(input())
member = []

for i in range(n):
    member.append(list(input().split(' ')))
    member[i][0] = int(member[i][0])

quicksort(member, 0, n - 1)

for i in range(n):
    print(f'{member[i][0]} {member[i][1]}')
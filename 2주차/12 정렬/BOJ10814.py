## 나이순 정렬 ##
'''
난이도 : 하
사용 : 버블정렬
백준은 버블 정렬을 쓰면 느리다고 시간초과를 띄워서
안될 것 같은데... 라고 쓰는 순간 시간 초과가 떴다.
'''
n = int(input())
member = []

for i in range(n):
    member.append(list(input().split(' ')))
    member[i][0] = int(member[i][0])

for i in range(n):
    for j in range(n-1, i, -1):
        if member[j][0] < member[j-1][0]:
            member[j], member[j-1] = member[j-1], member[j]

for i in range(n):
    print(f'{member[i][0]} {member[i][1]}')
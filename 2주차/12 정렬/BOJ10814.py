## 나이순 정렬 ##
'''
난이도 : 하
사용 : 버블정렬
버블 개선해보았다 ㅜㅜ 근데 시간초과 뜨지 않을까 .. 아~~
'''
n = int(input())
member = []

for i in range(n):
    member.append(list(input().split(' ')))
    member[i][0] = int(member[i][0])
last, count = 0, 0

for i in range(n):
    last = i
    for j in range(n-1, i, -1):
        if member[j][0] < member[j-1][0]:
            member[j], member[j-1] = member[j-1], member[j]
            last = j
            count += 1

    i = last
    if count == 0:
        break

for i in range(n):
    print(f'{member[i][0]} {member[i][1]}')
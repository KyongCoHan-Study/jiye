## 좌표 정렬하기 2 ##
'''
난이도 : 중하
사용 : 버블정렬
이게..되네?
list가 중첩됐을 때의 index가 헷갈려서 처음에 작동이 안 됐다.
마지막 출력문을 작성할 때 알아채서 바로 바꿨다.
근데 시간초과 ㅎㅎ
for문을 이렇게 잔뜩 넣었으니 예상은 했다만 다시해야지
'''


n = int(input())
x = [None] * n

for i in range(n):
    x[i] = list(map(int, input().split(' ')))

#y좌표 먼저 정렬합니다.
for i in range(n):
    last = i
    for j in range(n-1, i, -1):
        if x[j][1] < x[j-1][1]:
            x[j], x[j-1] = x[j-1], x[j]
            j = last
    i = last

#x좌표를 정렬합니다.
ran = [None, None]
for i in range(n):
    for j in range(n-1): #정렬할 범위를 추려냅니다.
        if x[j][1] == x[j+1][1]:
            if ran[0] == None:
                ran[0] = i
            ran[1] = j + 1

    for k in range(ran[1] - 1, ran[0], -1):
        if x[k][0] < x[k-1][0]:
            x[k], x[k-1] = x[k-1], x[k]

    ran = [None, None]

for i in range(n):
    print(f'{x[i][0]} {x[i][1]}')
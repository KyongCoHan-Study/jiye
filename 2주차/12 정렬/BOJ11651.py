## 좌표 정렬하기 2 ##
'''
난이도 : 중하
사용 : 단순선택정렬
버블이 아니라 선택정렬로 하니 훨씬 효율적인 코드가 나왔다.
근데 또 시간초과다
...
질문란을 보니 다른 알고리즘을 쓰라는 것 같다
그럼 오늘의 풀이는 여기까지...
'''


n = int(input())
x = [None] * n

for i in range(n):
    x[i] = list(map(int, input().split(' ')))

for i in range(n-1):
    min = i
    for j in range(i+1, n):
        if x[j][1] < x[min][1]:
            min = j
        elif x[j][1] == x[min][1]:
            if x[j][0] < x[min][0]:
                min = j
    x[i], x[min] = x[min], x[i]

for i in range(n):
    print(f'{x[i][0]} {x[i][1]}')
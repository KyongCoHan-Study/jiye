## 수 정렬하기 ##
'''
난이도 : 하
사용 : 버블정렬

어제 공부한 버블정렬의 예제코드를 그대로 쓴거나 마찬가지의 코드.
최적화도 하지 않았다.
그래도 잘 돌아간다.
잘 공부해서 잘 복습해서 잘 사용했으니 만족한다.
'''


n = int(input())
x = [None] * n

for i in range(n):
    x[i] = int(input())

for i in range(n):
    for j in range(n-1, i, -1):
        if x[j] < x[j-1]:
            x[j], x[j-1] = x[j-1], x[j]

for i in range(n):
    print(x[i])
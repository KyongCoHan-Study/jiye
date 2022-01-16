## 수 정렬하기 3 ##
'''
난이도 : 하
사용 : 카운팅 정렬(도수 정렬)
도수 정렬 코드 그대로 썼다.
개념이 조금 복잡하지마 이해하면 간단한 듯 하다.
'''
n = int(input())
x = [None] * n
min, max = 10000000, 0
for i in range(n):
    x[i] = int(input())
    if x[i] < min:
        min = x[i]
    elif x[i] > max:
        max = x[i]

f = [0] * (max + 1) # 누적 도수분포표 배열
b = [0] * n         #작업용 배열

for i in range(n):              f[x[i]] += 1
for i in range(1, max + 1):     f[i] += f[i - 1]
for i in range(n-1, -1, -1):    f[x[i]] -= 1; b[f[x[i]]] = x[i]
for i in range(n):              x[i] = b[i]

for i in range(n):
    print(x[i])

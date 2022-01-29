## 팩토리얼 0의 개수 ##
'''
난이도 : 실4
체감 난이도 : 하
풀이가 얻어걸린 감은 있는데 뭐 풀었으니 됐음
'''

n = int(input())
tot = 0
t, f = 0, 0

while n > 0:
    now = n
    while now % 2 == 0:
        t += 1
        now //= 2

    while now % 5 == 0:
        f += 1
        now //= 5

    n -= 1

print(t if t < f else f)

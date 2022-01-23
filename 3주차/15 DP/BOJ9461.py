## 파도반 수열 ##
'''
난이도 : 하
사용 : DP(메모제이션)
DP로 푼 피보나치랑 똑같아서 금방 했다.
'''


p = [0, 1, 1, 2, 2, 3, 4, 5, 7, 9]


def three(n):
    while len(p) < n + 1:
        p.append(0)
    if n <= 1:
        return p[1]
    if p[n]:
        return p[n]
    else:
        p[n] = three(n - 1) + three(n - 5)
    return p[n]

t = int(input())
for i in range(t):
    print(three(int(input()) - 1))



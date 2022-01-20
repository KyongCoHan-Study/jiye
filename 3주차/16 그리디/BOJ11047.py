## 동전 0 ##
'''
난이도 : 최하
유형 : 그리디
    분석 이유
        1. 명시된 유형이 그리디임
        2. 동전이 각자의 배수라서 다른 것을 생각할 필요가 없음
'''

n, k = map(int, input().split(' '))
coin = [int(input()) for i in range(n)]
count = 0

for i in coin[::-1]:
    count += k // i
    k %= i

print(count)





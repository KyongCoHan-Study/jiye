## 영화감독 숌 ##
'''
n번째로 666이 포함되는 수를 출력하는 문제

난이도 : 하
사용 : 브루트포스
저번에는 완전 복잡하게 풀고...
이번엔 저번에 다른 사람들 코드 봤던 걸 기억해서 풀었다.
'''

n = int(input())
tot = 0
i = 0

while True:
    i += 1
    if '666' in str(i):
        tot += 1
    if tot == n:
        print(i)
        break

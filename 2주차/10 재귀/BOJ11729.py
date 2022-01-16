## 하노이 탑 ##
'''
난이도 : ?
사용 : 재귀
도저히 모르겠어서 책 코드 보고 썼다.
note : 나중에 분석 해볼 것!!!!!!!!!!!!!!!!!!
'''

def hnoi(n:int, x:int, y:int)->None:
    if n > 1:
        hnoi(n - 1, x, 6 - x - y)

    print(f'{x} {y}')

    if n > 1:
        hnoi(n - 1, 6 - x - y, y)

n = int(input())

print(2**n-1)
hnoi(n, 1, 3)
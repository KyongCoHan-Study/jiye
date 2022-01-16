## 좌표 정렬하기 2 ##
'''
퀵소트로... 시간초과 뜰 것 같던데 시간초과떴다..ㅎㅎ
모르겟다
'''


def quickSort(a: list, n: int):
    Range = []
    Range2 = []
    pl = 0
    pr = n - 1
    Range.append((pl, pr))
    x = a[n // 2][1]

    while Range:
        tem = Range.pop()
        pl, pr = left, right = tem[0], tem[1]
        x = a[(left + right) // 2][1]

        while pl <= pr:
            while a[pl][1] < x: pl += 1
            while a[pr][1] > x: pr -= 1
            if pl < pr:
                a[pl], a[pr] = a[pr], a[pl]
                pl += 1
                pr -= 1
        if left < pr: Range.append((left, pr))
        if pl < right: Range.append((pl, right))

        if a[pl][1] == a[pr][1]:  # 가운데 그룹이 존재하는 경우
            pl2 = pr
            pr2 = pl
            Range2.append((pl2, pr2))
            while Range2:
                tem2 = Range2.pop()
                pl2, pr2 = left2, right2 = tem2[0], tem2[1]
                x2 = a[(left2 + right2) // 2][0]

                while pl2 <= pr2:
                    while a[pl2][0] < x: pl2 += 1
                    while a[pr2][0] > x: pr2 -= 1
                    if pl2 < pr2:
                        a[pl2], a[pr2] = a[pr2], a[pl2]
                        pl2 += 1
                        pr2 -= 1
                if left2 < pr2: Range.append((left2, pr2))
                if pl2 < right2: Range.append((pl2, right2))


n = int(input())
a = [None] * n
Range = []
RangeX = []

for i in range(n):
    a[i] = list(map(int, input().split(' ')))

quickSort(a, n)

for i in range(n):
    print(f'{a[i][0]} {a[i][1]}')

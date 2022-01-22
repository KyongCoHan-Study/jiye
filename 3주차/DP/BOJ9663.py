## 피보나치 함수 ##
'''
난이도 : 중
설명 :
    이전에 처리한 적 있는 fibo수는 True로 두어서 반복적인 call을 하지 않게 함
아!!!!!!! 스스로 해낸게 진짜 뿌듯하다
fiboHow를 True로 만드는 모든 조건을 생각하기,,,
'''

fiboHow = [[1, 0, True], [0, 1, True]]


def fiboNum(f, n):
    global fiboHow
    if fiboHow[f][2]:
        return
    if not fiboHow[n - 1][2]:
        fiboNum(f, n - 1)
        fiboHow[n - 1][2] = True
    fiboHow[n][0] += fiboHow[n - 1][0]
    fiboHow[n][1] += fiboHow[n - 1][1]


    if not fiboHow[n - 2][2]:
        fiboNum(f, n - 2)
        fiboHow[n - 2][2] = True
    fiboHow[n][0] += fiboHow[n - 2][0]
    fiboHow[n][1] += fiboHow[n - 2][1]

    fiboHow[n][2] = True


t = int(input())

for i in range(t):
    n = int(input())
    for j in range(len(fiboHow), n + 1):
        fiboHow.append([0, 0, False])
    fiboNum(n, n)
    print(f'{fiboHow[n][0]} {fiboHow[n][1]}')

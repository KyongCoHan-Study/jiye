## 주유소 ##
'''
난이도 :
사용 : 그리디
'''
n = int(input())
length = list(map(int, input().split()))
cost = list(map(int, input().split()))
totalCost = 0
last = 0
i = 0

while i < n:
    if cost[i] == 1: #가격이 1보다 싼 경우는 없으므로 탈출합니다.
        # print(f'{i}에서 주유수 가격 1을 만났으므로 탈출합니다.')
        totalCost += sum(length[i:])
        break
    minCost = min(cost[i:-1])
    j = cost.index(minCost)
    if i == j:
        j = n
    # print(f'i = {i}부터 {j}까지 총 {sum(length[i:j])}미터를 {cost[i]}로 이동')
    totalCost += sum(length[i:j]) * cost[i]
    # print(f'현재 totalCost : {totalCost}')
    i = j

print(totalCost)

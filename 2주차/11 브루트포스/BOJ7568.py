## 덩치 ##
'''
문제 요약
(P, Q), (x, y) 에서 x>p and y>q 일때 덩치가 크다고 한다
자신보다 더 큰 덩치의 사람이 k명인 사람의 등수를 k+1등이라고 할 때,
주어진 집단에서 덩치 등수를 출력하시오.

난이도 : 하
사용 : 브루트포스
저번에는 문제를 이해 못해서 한참 해매고 코드도 이상하게 짰는데,
문제를 요약해보니 직관적으로 문제가 이해되어 금방 풀었다
알게된 점:
join 함수는 str list만 가능하다.
int 등의 경우 map(str, list)로 한번 변환해주면 된다.
'''

n = int(input())
people = []
for i in range(n):
    people.append(list(map(int, input().split(' '))))
rank = [1 for i in range(n)]

for i in range(n):
    for j in range(n):
        if people[i][0] < people[j][0] and people[i][1] < people[j][1]:
            rank[i] += 1

print(' '.join(map(str, rank)))
## 블랙잭 ##
'''
문제 요약
카드 3장의 합이 m을 넘지 않으면서 가장 가깝게 만들 것

난이도 : 하
사용 : 넓이 우선 탐색(브루트포스)
저번에 풀었을 떄는 얼마나 시간이 걸렸는지 잘 기억이 안나지만
이번엔 딱히 코드를 수정할 필요도 없이 한큐에 통과가 됐다.
card리스트를 컴프리헨션으로 바로 초기화 한 것이 마음에 들고
range 인수를 생각나는 대로 직관적으로 넣었는데 작동해서 기분이 좋았다.
저번 코드랑 비교해 봤더니, 저번에는 마지막 변수를 헷갈리게 넣었다.
최대한 적은 횟수를 돌리기 위해 card.sort()도 들어있는데 어차피 모든 경우의 수를 돈다면
굳이 sort해줄 필요는 없는 것 같다.
'''

n, m = map(int, input().split(' '))
card = [i for i in map(int, input().split(' '))]
output = 0

for a in range(n):
    for b in range(a, ):
        for c in range(b, ):
            if output < card[a] + card[b] + card[c] <= m:
                output = card[a] + card[b] + card[c]

print(output)

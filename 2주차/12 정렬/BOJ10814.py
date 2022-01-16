## 나이순 정렬 ##
'''
난이도 : 하
사용 : 내부함수
몰라서 내부함수 썼다. 근데 시간초과?뜨겠지?
와!!!!!!!!!!!!!
하다가 톡방에 다 못 할 것 같다고 올리고 산책하고 왔는데 채점창에 맞았습니다 떠있었다 ㅜㅜ
'''
n = int(input())
member = []

for i in range(n):
    member.append(list(input().split(' ')))
    member[i][0] = int(member[i][0])

member.sort(key= lambda x:x[0])

for i in range(n):
    print(f'{member[i][0]} {member[i][1]}')
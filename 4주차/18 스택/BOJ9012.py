## 괄호 ##
'''
난이도 : 실4
체감난이도 : 하
사용 : 스택
다시 문제를 봤을 때 이걸 스택으로 풀 수 있을지 모르겠다...
'''
import sys
input = sys.stdin.readline

n = int(input().rstrip())

for i in range(n):
    stack = []
    lists = list(input().rstrip())
    for j in range(len(lists)):
        if lists[j] == '(':
            stack.append(0)
        else:
            try:
                stack.pop()
            except:
                print('NO')
                break
        if j == len(lists) - 1:
            if len(stack) == 0:
                print('YES')
            else:
                print('NO')
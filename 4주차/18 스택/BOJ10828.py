## 스택 ##
'''
난이도 : 실4
체감 난이도 : 하
처음에 input 썼다가 시간초과났다.
앞으로는 그냥 sys를 써야할 것 같다.
'''
import sys

n = int(input())
stack = []
for i in range(n):
    co = sys.stdin.readline().rstrip().split()
    command = co[0]
    if command == 'push':
        stack.append(co[1])
    elif command == 'pop':
        if len(stack) == 0:
            print(-1)
            continue
        print(stack[-1])
        del stack[-1]
    elif command == 'size':
        print(len(stack))
    elif command == 'empty':
        print(int(len(stack) == 0))
    elif command == 'top':
        if len(stack) != 0:
            print(stack[-1])
        else:
            print(-1)
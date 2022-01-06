## 별 찍기 - 2 ##
n = int(input())

for i in range(n):
    for j in range(n):
        if n - i -1 <= j:
            print('*', end='')
        else:
            print(' ', end='')
    print()
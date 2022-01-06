## X보다 작은 수 ##
n, x = map(int, input().split())
for i in list(map(int, input().split(' '))):
    if i < x:
        print(i, end=' ')
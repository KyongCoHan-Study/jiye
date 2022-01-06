## A+B - 5 ##
a, b = None, None

while True:
    a, b = map(int, input().split(' '))
    if a == 0 and b == 0:
        break
    print(a + b)
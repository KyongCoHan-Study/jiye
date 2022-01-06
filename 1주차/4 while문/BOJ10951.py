## A+B - 4 ##
a, b = None, None

while True:
    try:
        a, b = map(int, input().split(' '))
        print(a + b)
    except:
        break
## 배수와 약수 ##
'''
난이도 : 하
'''
num = [None, None]

while True:
    num = list(map(int, input().split()))
    if num == [0, 0]:
        break
    if num[1] % num[0] == 0:
        print('factor')
    elif num[0] % num[1] == 0:
        print('multiple')
    else:
        print('neither')


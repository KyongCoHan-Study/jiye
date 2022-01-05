list = list(map(int, input().split(' ')))
print((list[0] + list[1])%list[2])
print(((list[0]%list[2]) + (list[1]%list[2]))%list[2])
print((list[0] * list[1])%list[2])
print(((list[0]%list[2]) * (list[1]%list[2]))%list[2])

'''
옛날 코드가 낫다
A, B, C = map(int, input().split())
print((A+B)%C)
print( ((A%C) + (B%C))%C)
print((A*B)%C)
print(((A%C) * (B%C))%C)
'''
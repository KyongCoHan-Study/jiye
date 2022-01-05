n = int(input())
m = input()
list = [n * int(i) for i in m]
list.reverse()

list.append(n * int(m))

for i in list:
    print(i)
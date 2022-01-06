n = input()
if int(n) < 10:
    n = '0' + n
new = n
tot = 0

while True:
    tot += 1
    if len(n) == 1:
        new = '0' + new
    new = new[1] + str((int(new[0]) + int(new[1]))% 10)
    if new == n:
        print(tot)
        break
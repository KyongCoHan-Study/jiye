## 01타일 ##

n = int(input())
nums = {i: None for i in range(n+1)}
for i in range(3):
    nums[i] = i


def likeFibo(n):
    global nums
    if nums[n] == None:
        nums[n] = likeFibo(n - 1) + likeFibo(n - 2)
    return nums[n]



print(likeFibo(n) % 15746)

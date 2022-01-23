## 01타일 ##

n = int(input())
nums = [0] * 4
for i in range(1, 4):
    nums[i] = i

if n in range(4):
    print(nums[n] - 1)
else:
    for i in range(3, n+1):
        nums[0] = nums[1]
        nums[1] = nums[2]
        nums[2] = nums[0] + nums[1]

print(nums[2] % 15746)

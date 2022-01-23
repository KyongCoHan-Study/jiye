## 01타일 ##

n = int(input())
nums = {i: None for i in range(n+1)}
for i in range(3):
    nums[i] = i
for i in range(3, n+1):
    nums[i] = nums[i-1] + nums[i-2]

print(nums[n] % 15746)

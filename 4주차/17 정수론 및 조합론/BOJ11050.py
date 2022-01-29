## 이항 계수 1 ##
'''
난이도 : 브1
체감 난이도 : 하
이산수학 잘 모른다. 다음학기에 배움..
재귀호출 없이 효율적으로 구성하려고 노력함
'''

def pac(a):
    tot = 1
    if a > 0:
        while a > 0:
            tot *= a
            a -= 1
    return tot

n, k = map(int, input().split())

if 0 <= k <= n:
    print(pac(n) // (pac(k) * pac(n - k)))
else:
    print(0)

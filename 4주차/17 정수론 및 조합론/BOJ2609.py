## 최대공약수와 최소공배수 ##
'''
난이도 : 실5
체감 난이도 : 하
GCM : 최대공약수, GCD : 최소공배수
유클리드 호제법
GCM( 큰 수, 작은 수 ) == GCM(작은 수, 큰 수 % 작은 수)
GCD = 큰 수 * 작은 수 / 최소공배수
'''

a, b = map(int, input().split())
if a < b: a, b = b, a
gcd = a * b

while True:
    if a % b == 0:
        gcm = b
        gcd //= b
        print(gcm)
        print(gcd)
        break
    else:
        a, b = b, a % b

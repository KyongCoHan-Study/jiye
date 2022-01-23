## 신나는 함수 실행 ##
'''
난이도 : 하
사용 : DP(메모제이션)
아주 간단한 문제...였지만!! 딕셔너리를 써서 시간초과가 났다.
딕셔너리는 아주 느리니 리스트를 쓰자.
'''
memo = [[[None] * 21 for _ in range(21)] for _ in range(21)]

def w(a, b, c):
    global memo

    if a <= 0 or b <= 0 or c <= 0:
        return 1
    elif a > 20 or b > 20 or c > 20:
        return w(20, 20, 20)

    if memo[a][b][c]:
        return memo[a][b][c]

    if a < b < c:
        memo[a][b][c] = w(a, b, c - 1) + w(a, b - 1, c - 1) - w(a, b - 1, c)
    else:
        memo[a][b][c] = w(a - 1, b, c) + w(a - 1, b - 1, c) + w(a - 1, b, c - 1) - w(a - 1, b - 1, c - 1)
    return memo[a][b][c]

if __name__ == '__main__':
    while True:
        num = list(map(int, input().split()))
        if num == [-1, -1, -1]:
            break

        print(f'w({num[0]}, {num[1]}, {num[2]}) = {w(num[0], num[1], num[2])}')
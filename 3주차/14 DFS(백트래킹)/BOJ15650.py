## N과 M (2) ##
'''
난이도 : 하
백트래킹 기초 개념으로 풀 수 있는 문제였다
'''

def dfs(v):
    if v > n:
        if sum(ch) == m:
            for i in range(1, len(ch)):
                if ch[i] == 1:
                    print(i, end=' ')
            print()
        return

    if sum(ch) > m: # 컷에지
        return

    else:  # 상태트리
        ch[v] = 1  # 사용하는 경우
        dfs(v + 1)
        ch[v] = 0  # 사용안하는 경우
        dfs(v + 1)

if __name__ == '__main__':
    n, m = map(int, input().split())
    ch = [0] * (n + 1)
    dfs(1)

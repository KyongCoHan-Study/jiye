## N과 M (1) ##


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

'''
def DFS(v):
    if v == n + 1:
        for i in range(1, len(ch)):
            if ch[i] == 1:
                print(i, end=' ')
        print()
    else:  # 상태트리
        ch[v] = 1  # 사용하는 경우
        DFS(v + 1)
        ch[v] = 0  # 사용안하는 경우
        DFS(v + 1)


if __name__ == "__main__":
    n = int(input())
    ch = [0] * (n + 1)
    DFS(1)
'''
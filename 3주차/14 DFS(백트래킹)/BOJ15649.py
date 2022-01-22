## N과 M (1) ##
'''
잘 안돼서 인터넷 보고 해결했음
'''

n, m = map(int, input().split())
v = [False] * n
res = []

def dfs(d, n, m):
    if d == m:
        print(' '.join(map(str, res)))
        return
    for i in range(len(v)):
        if not v[i]:
            v[i] = True
            res.append(i + 1)
            dfs(d+1, n, m)
            v[i] = False
            res.pop()

dfs(0, n, m)
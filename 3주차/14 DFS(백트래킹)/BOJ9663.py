## N - Queen ##
'''
난이도 : ?
사용 : BFS?
아~~~
퀸이 어떻게 움직이는지 몰라서 처음에 대각선 방향을 안 고려하고
문제 쉽네 ㅎㅎ 이럼..
대각선 검사 하는 법을 아직 모르겠따.
'''
def dfs(v, nd):
    global count
    global chess
    global lis

    if nd == n:
        count += 1
        return
    if nd > n:
        return
    else:
        for i in range(n):
            if chess[i] is None:
                chess[i] = nd
                dfs(v - 1, nd + 1)
                chess[i] = None


if __name__ == '__main__':
    n = int(input())
    lis = 0
    count = 0
    chess = [None] * n

    dfs(n, 0)

    print(count)
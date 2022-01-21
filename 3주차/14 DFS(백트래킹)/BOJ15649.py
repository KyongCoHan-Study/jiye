## N과 M (1) ##

def dfs(m, n, nodes):
    '''
    :param nodes: 노드들
    :param m: 현재 숫자
    :param n: 앞으로 방문해야하는 노드 개수
    :return: 방문 노드 개수가 0개일 시 true리턴과 수 출력
    '''
    if n == 0:
        print(m, end=' ')
        return True  # 노드 방문을 끝낸 경우
    # 현재 노드를 아직 방문하지 않았다면
    if nodes[m][m] == 0:
        nodes[m][m] = 1  # 노드 방문 처리
        # 나머지 노드도 재귀적으로 호출
        for j in range(m):
            if nodes[i][j] == 0:
                dfs(j, n - 1, nodes)
            else:
                continue


n, m = map(int, input().split())
nodes = [[0] * n] * n

for i in range(n):
    dfs(i, m, nodes)



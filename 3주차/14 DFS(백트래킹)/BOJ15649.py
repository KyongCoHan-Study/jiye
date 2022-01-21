## N과 M (1) ##

def makingGraph(n, m):
    '''
    문제 조건에 맞는 그래프를 만듭니다
    :param n: 문제에서 주어진 자연수 n
    :param m: 깊이 m
    :return: 인접 리스트 표현법으로 나타낸 그래프
    여기서 m은 사용하지 않으며,
    각 노드와 노드 사이에 간선이 모두 있는 그래프를 만듬.
    인덱스 0은 무시합니다.
    '''
    graph = [[i for i in range(n + 1)] for i in range(m + 1)]
    graphVisitTime = [[0, 0] for i in range(n + 1)]
    for i in range(len(graph)):
        graph[i].remove(i)

    return graph, graphVisitTime


def dfs(g, v):
    '''
    dsf
    :param g: graph의 리스트
    :param v: visit time의 리스트,
                [0][1]이 모두 None이라면 White
                [0]의 값이 있다면 Gray
                [1]의 값이 있다면 black
    :return: None
    '''
    for i in range(len(v)):
        if i == 0 or v[i][0] == 0:
            dfsVisit(g[i], v, i)


time = 0


def dfsVisit(g, v, i):
    '''
    dfs 탐색을 합니다.
    :param g: graph의 리스트
    :param v: visit time의 리스트,
                [0][1]이 모두 None이라면 White
                [0]의 값이 있다면 Gray
                [1]의 값이 있다면 black
    :param i: 현재 정점의 값
    :return: None
    '''
    global time
    global m

    time += 1
    v[i][0] = time
    for b in g:  # 간선 (a, b)를 탐색한다
        print(v[i][0])
        if v[i][0] == 0:
            pi = i
            dfsVisit(g, v, b)
    time += 1
    v[i][1] = time
    if v[i][0] - v[i][1] >= m:
        return None


n, m = map(int, input().split())
g, v = makingGraph(n, m)
dfs(g, v)

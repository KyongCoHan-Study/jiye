## N과 M (1) ##

def makingTree(i, n, m):
    """
    :param i: root의 수
    :param n: 자연수의 범위
    :param m: 트리의 깊이 (여기서는 원소의 개수와 같음)
    :return: 조건의 맞는 tree의 list
    """
    treeVisit = []
    treeNum = [[]] * m

    for i in range(m):  # m:깊이
        if i == 0:
            treeVisit.append([0])
            treeNum[i].append(i)
        else:
            treeVisit.append([0] * (n - i))
            for j in range(n):
                if j not in treeNum[i - 1]:
                    treeNum[i].append(j)

    # 중간 확인용 출력
    for i in range(m):
        print(treeNum[i])


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


for i in range(n):
    makingTree(i, n, m)


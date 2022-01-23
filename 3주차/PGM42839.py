## 소수 구하기 ##
'''
난이도 : 중
사용 : BFS
DFS를 사용하고 싶었는데 결과적으론 BFS를 사용한 것이 됐다.
근데 이진 트리가 아니라 그래프로 만들어 풀었으니까 BFS가 맞는 것 같다.
처음으로 내 힘으로 풀어서 뿌듯했다.
'''

import math


def dfs(d, nd):
    '''
    d : depth (수열의 길이)
    nd : nowdepth
    '''
    global numlist
    if nd == d:
        numlist.append(0)
        for i in range(len(innum)):
            if ch[i] is not None:
                numlist[-1] += int(innum[i]) * (10 ** ch[i])
        return

    # if sum(1 if ch[i] else 0 for i in range(n)) + len(ch[n:]) < d: #컷에지
    #     return

    else:
        for i in range(len(innum)):
            if ch[i] is None:
                ch[i] = nd
                dfs(d, nd+1)
                ch[i] = None


def primenum(n):
    if n in range(2):
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True


def solution(numbers):
    global numlist
    global ch
    global innum

    innum = list(numbers)
    ch = [None] * len(innum)
    numlist = []

    for i in range(1, len(innum) + 1):
        dfs(i, 0)


    numlist = list(set(numlist))

    i = 0
    while i < len(numlist):
        if not primenum(numlist[i]):
            del numlist[i]
        else:
            i += 1

    answer = len(numlist)
    return answer

if __name__ == '__main__':
    n = '011'
    print(solution(n))
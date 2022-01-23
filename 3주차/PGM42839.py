import math


def dfs(n, d, nd):
    '''
    n : 현재 숫자
    d : depth (수열의 길이)
    nd : nowdepth
    '''
    global numlist
    if nd == d:
        numlist.append('')
        for i in range(len(ch)):
            if ch[i] == 1:
                numlist[-1] += innum[i]
        return
    if sum(ch[:n]) + len(ch[n:]) < d:
        return

    else:  # 상태트리
        # 사용하는 경우
        ch[n] = 1
        dfs(n + 1, d, nd + 1)
        # 사용하지 않는 경우
        ch[n] = 0
        dfs(n + 1, d, nd)


def primenum(n):
    if n == 0:
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
    ch = [0] * len(innum)
    numlist = []

    for i in range(1, len(innum) + 1):
        dfs(0, i, 0)

    numlist = list(map(int, numlist))
    numlist = list(set(numlist))

    i = 0
    while i < len(numlist):
        if not primenum(numlist[i]):
            del numlist[i]
        i += 1

    answer = len(numlist)
    return answer

if __name__ == '__main__':
    n = '7843'
    print(solution(n))
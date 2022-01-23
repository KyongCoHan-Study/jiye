import math


def dfs(d, nd):
    '''
    n : 현재 숫자
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
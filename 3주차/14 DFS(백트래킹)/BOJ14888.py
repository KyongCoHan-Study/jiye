## 연산자 끼워넣기 ##
def dfs(d, nd, li:list, ch:list, tot:list):
    '''
    d : depth (수열의 길이)
    nd : nowdepth
    li: 조사중인 리스트
    ch : 조사중인 리스트의 check 리스트
    tot : 저장하는 리스트
    '''
    if nd == d:
        tot.append('')
        for i in range(len(li)):
            if ch[i] is not None:
                tot[-1] += str(li[i])
        return

    else:
        for i in range(len(li)):
            if ch[i] is None:
                ch[i] = nd
                dfs(d, nd + 1, li, ch, tot)
                ch[i] = None


if __name__ == '__main__':
    n = int(input())
    numlist = list(map(int, input().split()))
    oprator = ['+', '-', '*', '/']
    opnum = list(map(int, input().split()))
    chnum = [None] * n
    totnum = []
    for i in range(1, len(numlist) + 1):
        dfs(i, 0, numlist, chnum, totnum)


    chop = [None] * (n - 1)
    totop = []
    for i in range(1, len(numlist) + 1):
        dfs(i, 0, oprator, chop, totop)

    ##아래로는 리스트 취합 한 뒤 eval함수쓰기

    print() #디버깅 중 값 확인용 BreakPoint
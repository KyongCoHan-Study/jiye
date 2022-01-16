'''
난이도 : ?
사용 : 버블정렬
실패 사유 : 시간초과
퀵정렬로 다시 시도해봐야겠다.
'''

numbers = [3, 30, 34, 5, 9]
numbers = [str(i) for i in numbers]
def solution(numbers):
    i = 0
    numbers = list(map(str, numbers))
    for i in range(len(numbers)):
        last = i
        for j in range(i, len(numbers)):
            for k in (range(len(numbers[i])) if len(numbers[i])<len(numbers[j]) else range(len(numbers[j]))):
                if int(numbers[i][0]) < int(numbers[j][0]):
                    numbers[i], numbers[j] = numbers[j], numbers[i]
                    break
            last = j
        i = j

    return ''.join(numbers)



print(solution(numbers))
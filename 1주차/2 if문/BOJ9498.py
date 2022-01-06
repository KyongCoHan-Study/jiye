## 시험 성적 ##
'''
숫자의 규칙성을 이용해봤다
단, 이렇게 계산할 경우 100점은 -1이 되어 F가 출력되었기 떄문에
따로 빼주었다.
'''

score = int(input())
list = ['A', 'B', 'C', 'D', 'F']
if score == 100:
    print(list[0])
else:
    score = 9 - score // 10
    print(list[score] if score < 5 else list[4])
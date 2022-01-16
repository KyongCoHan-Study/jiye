## 수 정렬하기 3 ##
'''
난이도 : 상
사용 : 카운팅 응용

카운팅 정렬을 사용한다고 해서 너무 그것에 얽매여서 코드가 복잡해졌었다.
다른 분이 푸신 코드를 보니 쉽게 해결할 수 있는 걸 너무 정렬의 예제 코드에 얽매여있었다는 것을 알았다.
조금 더 유연한 사고를 가져야겠다.

이렇게도 해보고! 저렇게도 해보고! 시간초과나고! 열받아서 정답 봐도 시간 초과^^
결국 input()를 sys.stdin.readline()으로 바꾸고 나서야 끝났다.
'''
import sys

f = [0] * 10001

for i in range(int(input())):
    f[int(sys.stdin.readline())] += 1

for i in range(10001):
    for j in range(f[i]):
        print(i)
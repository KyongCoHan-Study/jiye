## 두 수 비교하기 ##
'''
아는 문제를 복습하지 좋은 점은
조금 더 파이써닉 한 코드를 고민해볼 수 있는 점 같다.
'''

a, b = map(int, input().split(' '))

print('>' if a > b else '<' if a < b else '==')
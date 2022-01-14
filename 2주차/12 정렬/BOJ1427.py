## 소트인사이드 ##
'''
난이도 : 하
사용 : 버블정렬
버블정렬에 last의 인덱스를 사용해 약간의 최적화를 해줬다.
for문의 마지막에 i = last를 해줄 때 i = j라고 잘못 써서 Nameerror가 났었다.
지역변수를 밖에 썼기 때문인데, 이런 실수를 하지 않도록 조심해야겠다.
'''


x = [i for i in input()]
n = len(x)

for i in range(n):
    last = i
    for j in range(n-1, i, -1):
        if x[j] > x[j-1]:
            x[j-1], x[j] = x[j], x[j-1]
            last = j
    i = last

print(''.join(x))
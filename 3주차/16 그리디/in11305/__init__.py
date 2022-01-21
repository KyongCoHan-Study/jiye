from random import *
import sys

def ini():
    n = randint(2, 10)
    length = [str(randint(1, 15)) for i in range(n - 1)]
    cost = [str(randint(1, 15)) for i in range(n)]
    f = open("in11305.txt", 'w')
    f.write(str(n) + '\n')
    f.write(' '.join(length) + '\n')
    f.write(' '.join(cost))
    print(n)
    print(' '.join(length))
    print(' '.join(cost))
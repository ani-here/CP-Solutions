from collections import defaultdict
from collections import deque
from itertools import permutations
from math import *

 
import sys
input = lambda: sys.stdin.readline().rstrip("\r\n")
ii = lambda: int(input())
mii = lambda: map(int, input().split())
lmii = lambda: list(map(int, input().split()))
tmii = lambda: tuple(map(int, input().split()))
mfi = lambda: map(float, input().split())
lmfi = lambda: list(map(float, input().split()))

T = ii()
ct = 0


def solve():
    n,k = mii()
    mat = []
    for _ in range(n):
        mat.append(input())
    #print(mat)

    for i in range(0,n,k):
        for j in range(0,n,k):
            print(mat[i][j],end='')
        print()


#solve()  
for _ in range(T):
    solve() 

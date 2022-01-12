'''
N과 M (3)

'''
import sys
input = sys.stdin.readline

N, M = map(int,input().split())

def dfs(idx,nums):
    global N, M

    if idx == M:
        print(*nums)
        return
    
    for i in range(1,N+1):
        dfs(idx+1,nums + [i])


for i in range(1,N+1):
    dfs(1,[i])
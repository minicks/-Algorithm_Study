'''
N과 M (1)

'''
import sys
input = sys.stdin.readline
N, M = map(int,input().split())
used = [0] * (N+1)
def dfs(idx,nums):
    if idx == M:
        print(" ".join(nums))
        return

    for i in range(1,N+1):
        if used[i] == 1:
            continue
        used[i] = 1
        dfs(idx + 1,nums + [str(i)])
        used[i] = 0

dfs(0,[])

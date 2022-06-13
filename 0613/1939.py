'''
중량 제한

'''
import sys
input = sys.stdin.readline
import heapq

N, M = map(int,input().split())

maps = [[] for _ in range(N+1)]
visit = [0] * (N+1)

for _ in range(M):
    A, B, C = map(int,input().split())

    maps[A].append((-C,B))
    maps[B].append((-C,A))

st, ed = map(int,input().split())
q = [(-1 * (10 ** 9),st)]

while q:
    W, now = heapq.heappop(q)
    visit[now] = 1

    if now == ed:
        print(-W)
        break

    for C, next in maps[now]:
        
        if visit[next]:
            continue

        heapq.heappush(q,(max(W,C),next))


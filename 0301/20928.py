'''
걷는 건 귀찮아

'''
import sys

input = sys.stdin.readline

N, M = map(int,input().split())

rickshaw = list(map(int,input().split()))
dist = list(map(int,input().split()))

road = [[0] * 1000001 for _ in range(2)]

for i in range(N):
    road[0][rickshaw[i]] = 1
    road[1][rickshaw[i]] = dist[i]

road[0][M] = 1
idx = rickshaw[0]
next_idx = rickshaw[0]
cnt = -1

while 1:
    max_d = 0
    cnt += 1
    for i in range(1,road[1][idx]+1):
        if idx + i <= M and road[0][idx + i] == 1:
            if max_d <= idx + i + road[1][idx + i]:
                max_d = idx + i + road[1][idx + i]
                if max_d >= M:
                    max_d = M
                next_idx = idx + i
    if idx == next_idx:
        break
    
    if next_idx >= M:
        idx = M
        break
    else:
        idx = next_idx

if idx == M:
    print(cnt)
else:
    print(-1)
    

'''
4 10
1 3 5 9
5 5 4 1

4 10
2 3 5 9
5 5 4 1

4 11
1 3 5 9
5 5 4 1

1 10
1
9

1 10
2
9

1 1
1
1


5 6
1 2 3 4 5
1 1 1 1 1

1 10
9
1

5 10
1 2 3 4 5
9 11 1 1 1

5 11
1 2 3 4 5
9 1 1 1 1


5 100
1 11 30 50 90
10 19 20 40 1000

4 20
1 6 11 30
10 5 9 5


'''
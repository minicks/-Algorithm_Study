def pprint(list_):
    for lis in list_:
        print(lis)

import sys
input = sys.stdin.readline

M, N, V = map(int,input().split())
X, Y = map(int,input().split())
X -= 1
Y -= 1
maps = [list(map(int,input().split())) for _ in range(M)]
vol_visit = [[0] * N for _ in range(M)]
per_visit = [[0] * N for _ in range(M)]

volcanos = [[] for _ in range(300)]
for _ in range(V):
    vol = list(map(int,input().split()))
    volcanos[vol[2]].append([vol[0]-1,vol[1]-1])
    per_visit[vol[0]-1][vol[1]-1] = 1


per_q = [[X,Y]]
vol_q = []
max_h = maps[X][Y]
max_t = 0
t = 0

dirs = [[-1,0],[0,1],[1,0],[0,-1]]
while per_q:
    for vol_loc in volcanos[t]:
        if vol_visit[vol_loc[0]][vol_loc[1]]:
            continue
        vol_visit[vol_loc[0]][vol_loc[1]] = 1
        for dir in dirs:
            next_vol_loc_x = vol_loc[0] + dir[0]
            next_vol_loc_y = vol_loc[1] + dir[1]

            if 0 <= next_vol_loc_x < M and 0 <= next_vol_loc_y < N:
                pass
            else:
                continue

            if vol_visit[next_vol_loc_x][next_vol_loc_y]:
                continue

            volcanos[t+1].append([next_vol_loc_x,next_vol_loc_y])

    next_per_q = []
    for per_loc in per_q:
        # print(per_loc)
        if per_visit[per_loc[0]][per_loc[1]]:
            continue
        if vol_visit[per_loc[0]][per_loc[1]]:
            continue
        per_visit[per_loc[0]][per_loc[1]] = 1
        if maps[per_loc[0]][per_loc[1]] > max_h:
            max_h = maps[per_loc[0]][per_loc[1]]
            max_t = t
        for dir in dirs:
            # print(next_per_q)
            next_per_loc_x = per_loc[0] + dir[0]
            next_per_loc_y = per_loc[1] + dir[1]

            if 0 <= next_per_loc_x < M and 0 <= next_per_loc_y < N:
                pass
            else:
                continue
            if per_visit[next_per_loc_x][next_per_loc_y]:
                continue
            if vol_visit[next_per_loc_x][next_per_loc_y]:
                continue

            next_per_q.append([next_per_loc_x,next_per_loc_y])
            
    per_q = next_per_q[:]


    
    t += 1

print(max_h,max_t)



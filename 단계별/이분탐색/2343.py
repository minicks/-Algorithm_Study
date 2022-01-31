'''
화살을 쏘자!

'''
import sys
input = sys.stdin.readline

N, M = map(int,input().split())

blue_rays = list(map(int,input().split()))

l = max(blue_rays)
r = sum(blue_rays)

while l <= r:
    mid = (r+l)//2
    
    cnt = 0
    sum = 0
    for blue_ray in blue_rays:
        if sum + blue_ray > mid:
            cnt += 1
            sum = 0
        sum += blue_ray
    if sum > 0:
        cnt += 1

    if cnt <= M:
        r = mid - 1
    else:
        l = mid + 1

print(l)
'''
동전 0

'''
import sys

N, K = map(int,sys.stdin.readline().split())

coins = []

for _ in range(N):
    coins.append(int(sys.stdin.readline()))

coins.reverse()
count = 0
for coin in coins:
    if K//coin:
        count += K//coin
        K %= coin
    if K == 0:
        break
print(count)
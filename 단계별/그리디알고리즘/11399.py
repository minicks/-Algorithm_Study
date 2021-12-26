'''
ATM

'''
import sys

N = int(sys.stdin.readline())

Pi = list(map(int,sys.stdin.readline().split()))
Pi.sort()

time = 0

for i in range(N):
    time += Pi[i] * (N-i)
print(time)
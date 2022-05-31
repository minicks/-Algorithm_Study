'''
신기한 소수

'''
import sys
input = sys.stdin.readline


if __name__ == "__main__":
    T = int(input().strip())

    for _ in range(T):
        N = int(input().strip())

        timer = [0,0,0,0,0]

        timer[0] = N // 60
        N %= 60

        if N > 35:
            timer[0] += 1
            timer[2] += (6 - N//10)
        else:
            timer[1] += N//10
        N %= 10

        if N > 5:
            timer[1] += 1
            timer[4] += (10 - N)
        elif N == 5 and timer[2]:
            timer[2] -= 1
            timer[4] += N
        else:
            timer[3] += N

        if timer[1] and timer[2]:
            min_v = min(timer[1],timer[2])
            timer[1] -= min_v
            timer[2] -= min_v

        print(*timer)
'''
자리수로 나누기

'''
import sys
input = sys.stdin.readline

input_num = input().strip()

num_set = set(map(int,input_num))
if 0 in num_set:
    num_set.remove(0)
idx = 1
flag = False

for num in num_set:
    now_num = int(input_num)
    if now_num % num:
        break
else:
    flag = True

if not flag:
    while 1:
        for i in range(10**idx):
            now_num = int(input_num + str(i).zfill(idx))
            
            for num in num_set:
                if now_num % num:
                    break
            else:
                flag = True
                break
            
        idx += 1
        if flag:
            break

print(now_num)
'''
심심한 준규

'''
import sys
input = sys.stdin.readline

N = int(input().strip())
enco_message = list(input().split())

for i in range(N):
    if int(enco_message[i],16) >= 64:
        print('-',end='')
    else:
        print('.',end='')

# print(46^30,46^31,46^32,46^33,46^34,46^35,46^36,46^37,46^38,46^39)
# print(32^30,32^31,32^32,32^33,32^34,32^35,32^36,32^37,32^38,32^39)
# for i in range(97,123):
#     for j in range(30,40):
#         print(i^j,end = ' ')
#     print()


'''
48 49 14 15 12 13 10 11 8 9
62 63 0 1 2 3 4 5 6 7
127 126 65 64 67 66 69 68 71 70
124 125 66 67 64 65 70 71 68 69
125 124 67 66 65 64 71 70 69 68 
122 123 68 69 70 71 64 65 66 67
123 122 69 68 71 70 65 64 67 66 
120 121 70 71 68 69 66 67 64 65 
121 120 71 70 69 68 67 66 65 64 
118 119 72 73 74 75 76 77 78 79 
119 118 73 72 75 74 77 76 79 78 
116 117 74 75 72 73 78 79 76 77 
117 116 75 74 73 72 79 78 77 76 
114 115 76 77 78 79 72 73 74 75 
115 114 77 76 79 78 73 72 75 74
112 113 78 79 76 77 74 75 72 73
113 112 79 78 77 76 75 74 73 72
110 111 80 81 82 83 84 85 86 87 
111 110 81 80 83 82 85 84 87 86 
108 109 82 83 80 81 86 87 84 85
109 108 83 82 81 80 87 86 85 84
106 107 84 85 86 87 80 81 82 83
107 106 85 84 87 86 81 80 83 82
104 105 86 87 84 85 82 83 80 81
105 104 87 86 85 84 83 82 81 80
102 103 88 89 90 91 92 93 94 95 
103 102 89 88 91 90 93 92 95 94
100 101 90 91 88 89 94 95 92 93
'''

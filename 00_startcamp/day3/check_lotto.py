# my == real ->1등
# 5개 같고 보너스 맞으면 2등
# 5개 맞으면 3등 
# 4개 4등 
# 3개 5등
# else 꽝
import random

# numbers = [0 for a in range(1,46,1)]
# for a in range(0,45, 1):
#   numbers[a] = a + 1
# my = random.sample(numbers,6)
my = [1, 2, 3, 4, 5, 6]
real = [1, 2, 3, 4, 5, 7]

bonus = 6
bns = 0
cnt = 0

for i in range(0, 6, 1):
    for j in range(0, 6, 1):
        if my[i] == real[j]:
            cnt += 1
        elif my[i] == bonus:
            bns += 1
if cnt == 6:
    print('1등')
elif cnt == 5:
    if bns == 6:
        print('2등')
    else:
        print('3등')
elif cnt == 4:
    print('4등')
elif cnt == 3:
    print('5등')
else:
    print('꽝')

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
# 실제 번호로 교체
bns = 0
cnt = 0
# is_bonus = False
# if bonus in my: 파이썬에서 할 수 있는 코드 배열안에 해당 값 있는 지 확인.
#     is_bonus = True
for i in range(0, 6, 1):
    # if i == bonus:
    #     is_bonus = True
    for j in range(0, 6, 1):
        if my[i] == real[j]:
            cnt += 1
        elif my[i] == bonus:
            bns += 1
'''
[1, 2, 3]=리스트 | {1, 2, 3}=셋  |(1, 2, 3)= 튜플 | {'a': 'A'}=> 딕셔너리
# 3번째 방법집합느낌으로
match = set(my).intersection(set(real)) 교집합 비교할 수 있음.가장 파이썬같이 쓴 코드
match_count = len(match)
'''

if cnt == 6:
    result = '1등'
elif cnt == 5:
    # if is_bonus == True:
    if bns == 6:
        # if bonus in my:여기다 쓰면 위에 쓰는거 줄일 수 있음.
        #  어쩌구 in 어쩌구로 비교가능.
        result = '2등'
    else:
        result = '3등'
elif cnt == 4:
    result = '4등'
elif cnt == 3:
    result = '5등'
else:
    result = '꽝'

return result

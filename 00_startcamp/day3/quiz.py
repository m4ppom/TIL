# name = input('이름을 입력하세요: ')
# print('hi '+name)
# words = input('입력 고고:')
# 입력되는값 = string
# words의 첫글자와 마지막글자를 출력하라.
# word = int(list(words))
# n = len(words)
# print(words[0], words[n-1])
# print(type(words))
# words[-1] 마지막꺼로 넘어감
# 정수n을 입력받고, 1~n까지 출력하라
# n = input('수를 입력하세요: ')
# n = int(n)
# for i in range(n):
#     print(i + 1, end=',')
# string = input()
# number = int(string)
# 짝수 홀수 구분
# number = int(input('숫자를 입력하세요 : '))
# n = number % 2
# if n == 0:
#     print(number , '은 짝수')
# else:
#     print(number , '은 홀수')
# 피즈버즈 1부터 증가 3의 배수에서 fizz나옴 5배수 buzz 15배수 fizz buzz
number = int(input('숫자를 입력하세요 : '))

for i in range(number):
    num = i + 1
    if num % 15 == 0:
        print('fizz buzz')
    elif num % 5 == 0:
        print('buzz')
    elif num % 3 == 0:
        print('fizz')
    else:
        print(num)

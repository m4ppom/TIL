# 190708 startcamp - day1

## 컴퓨터 프로그래밍 언어

### 컴퓨터

컴퓨터 = 계산기

### 프로그래밍

명령어의 집합- 일시키는 것 

### 언어

말, 약속

## Python 기초 문법 3형식

1. 저장
2. 조건
3. 반복



## Python 함수 

파이썬 함수에는 내장 함수와 외장 함수가 있다.

* 내장함수
  * `print()` : 출력하는 함수
  * `range()`  : 범위를 생성하는 함수
  * `list()`: 리스트를 생성하는 함수

* 외장 함수
  * `random` : 랜덤 관련 함수들의 묶음
  * `random.choice` : 리스트에서 1개 무작위 선택
  * `random.sample(p, k)` :모집단에서 k개의 요소를 무작위 비복원 선택

### 로또 번호 추첨 하기

```python
import random

numbers = [0 for a in range(1,46,1)]
for a in range(0,45, 1):
  numbers[a] = a + 1

#numbers 리스트 1-45
#lucky_numbers출력
lucky_numbers = random.sample(numbers,6)
print(lucky_numbers)

numbers2 = []
n = 0
while n < 45:
#  numbers2[n] = n
  numbers2.append(n + 1)
  n += 1
lucky_numbers2 = random.sample(numbers2,6)
print(lucky_numbers2)

numbers3 = []

for i in range(45):
  numbers3.append(i + 1)
lucky_numbers3 = random.sample(numbers3,6)
print(lucky_numbers3)

range(45) #0~44
range(1, 46, 1)

numbers4 = list(range(1, 46))
lucky_numbers4 = random.sample(numbers4, 6)
print(lucky_numbers4)
#비교해서점수
```


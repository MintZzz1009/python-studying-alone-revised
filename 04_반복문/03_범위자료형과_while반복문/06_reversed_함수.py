# reversed( )
# 매개변수: 반복 가능한 것
# 결과: 그것을 뒤집은 것
# 결과 자료형: 이터레이터
# -> list()를 사용해 리스트로 변환해서 결과 보기

# 리스트
print(list(reversed([1, 2, 3, 4, 5])))

# 범위
print(list(reversed(range(0, 10))))

for i in reversed(range(0, 10)):
    print(i)

# 피라미드 만들기
# height = 10
# for i in range(1, heignt + 1):
    # print('*' * i)
    # N개의 별을 가로 방향으로 출력하는 반복문
    # [작성]!

# N개의 별을 가로 방향으로 출력하는 반복문
N = 10
result = ''
for i in range(N):
    # print('*' end='')     '*' 을 가로로 출력하는 방법
    result += '*'
print(result)


# 답
height = 10
for i in range(1, height + 1):
    # N = i
    result = ''
    for j in range(i):
        result += '*'
    print(result)


# 답 - 피라미드2
print('\n피라미드 2-1')
N = 10
    # ' ' * 4 + '*' * 1
    # ' ' * 3 + '*' * 3
    # ' ' * 2 + '*' * 5
    # ' ' * 1 + '*' * 7
answer = ''

list_n =list(reversed(range(N + 1)))
for i in (range(N)):
    answer = ' ' * list_n[i] + '*' * (2*i -1)
    print(answer)
    
print('\n피라미드 2-2') 
answer = ''
N = 10
for k in range(N):
    for i in range(k, N):
        answer += ' '
    for j in range(2*k + 1):
        answer += '*'
    answer += '\n'    
print(answer)

## 분석하기
height = 10
print('  *')    # 띄어쓰기: 2 + 별 1개
print(' ***')   # 띄어쓰기: 1 + 별 3개
print('*****')  # 띄어쓰기: 0 + 별 5개

for i in range(1, height + 1):
    answer = ''
    # print('띄어쓰기:', height + 1)
    answer += ' ' * (height - i)
    # print('별:', 2 * i + 1)
    answer += '*' * (2 * i - 1)
    print(answer)    
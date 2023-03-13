# 함수는 변수에 저장할 수 있다.
# 매개변수로 전달되는 함수
def call_10_times(콜백함수):
    for i in range(10):
        콜백함수(i)


def print_hello(매개변수):
    print('안녕하세요', 매개변수)


# 매개변수를 함수로 입력해서 전달
call_10_times(print_hello)


# 콜백함수 활용 예(1): map, filter
# 이터레이터 = map(함수, 리스트)
# 리스트의 각각의 요소에 함수를 적용해서 
# 새로운 이터레이터를 리턴한다

def power(숫자):
    return 숫자 ** 2

A = [1, 2, 3, 4, 5]
이터레이터 = map(power, A)
print(list(이터레이터))


# 리스트 내포로 구현 가능
print([
    숫자 ** 2 # 표현식
    for 숫자 in range(1, 5 + 1) # 반복문
    # 조건문
])


# filter(함수, 리스트)
# 리스트의 요소를 함수에 전달했을 때
# 결과로 True가 나오는 녀석을 모아서
# 새로운 이터레이터를 만듦

def 홀수인가요(숫자):
    if 숫자 % 2 == 1:
        return True
    else:
        return False
    
A = [1, 2, 3, 4, 5]
이터레이터 = filter(홀수인가요, A)
print(list(이터레이터)) # [1, 3, 5]
print(이터레이터)   # <filter object at 0x0000017984EFB8B0>
print([
    # 표현식
    숫자
    # 반복문
    for 숫자 in A
    # 조건문
    if 숫자 % 2 == 1
])
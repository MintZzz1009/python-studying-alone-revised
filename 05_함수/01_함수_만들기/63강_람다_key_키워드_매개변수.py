# 람다: 간단한 함수를 간단하게 해주는 문법
def power(숫자):
    return 숫자 ** 2

def power(숫자): return 숫자 ** 2

# lambda 매개변수: 리턴값
power = lambda 매개변수: 매개변수 ** 2 
print(power(10)) # 100


def is_odd(숫자):
    return 숫자 % 2 == 1

def is_odd(숫자): return 숫자 % 2 == 1

is_odd = lambda 숫자: 숫자 % 2 == 1
print(is_odd(3)) # True


# 람다가 효과를 발휘하는 때 == 함수 호출에 바로 꽂아넣을 때 
A = [1, 2, 3, 4, 5]
이터레이터 = map(lambda 숫자: 숫자 ** 2, A)
# 약간 익명함수처럼 사용되는 것 같다.
print(list(이터레이터))

이터레이터 = filter(lambda 숫자: 숫자 % 2 == 1, A)
print(list(이터레이터))



# key 키워드 매개변수
A = [52, 273, 32, 103, 57]
print(min(A))
print(max(A))

B = [{
    '제목': '혼자 공부하는 파이썬',
    '가격': 18000
}, {
    '제목': '혼자 공부하는 파이썬 + 딥러닝',
    '가격': 26000
}, {
    '제목': '혼자 공부하는 자바스크립트',
    '가격': 24000
}]
# print(min(B)) # 딕셔너리는 비교할 수 없다는 오류코드
# print(max(B))

def 콜백함수(요소):
    return 요소['가격']

print(min(B, key=콜백함수))
print(min(B, key=콜백함수))


def 가격(요소):
    return 요소["가격"]

# min, max 함수가 가지고 있는 key라는 이름의 키워드 매개변수를 사용.
print(min(B, key=가격))
print(min(B, key=가격))
 
print(min(B, key=lambda 책: 책['가격']))
print(min(B, key=lambda 책: 책['가격']))
B.sort(key=lambda 책: 책['가격'])
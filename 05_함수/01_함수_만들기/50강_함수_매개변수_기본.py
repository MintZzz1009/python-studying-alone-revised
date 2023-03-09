# 매개변수: 함수의 괄호 안에 넣는 변수
def print_3_times(문자열, 횟수):
    for i in range(횟수):
        print(문자열)
    
# argument: 함수 호출 때 넣은 값
print_3_times('안녕', 10)
# 매개변수가 2개인데 1개나 3개 등을 입력했을 때 오류:
print_3_times('안녕')
# TypeError: print_3_times() missing 1 required positional argument: '횟수'

# 매개변수의 자료형
print_3_times('안녕', '문자열')
# TypeError: 'str' object cannot be interpreted as an integer

## parameter: 함수 정의 때 넣은 변수
## 함수를 설계하는 사람
## 1. 함수의 설명서 -> 문서(documentation)
## 2. 예외 처리
def print_3_times(문자열, 횟수):
    if type(문자열) != str:
        print('첫 번째 매개변수는 문자열을 입력해야 합니다!')
    if type(횟수) != int:
        print('두 번째 매개변수는 정수를 입력해야 합니다!')
    for i in range(횟수):
        print(문자열)

## argument: 함수 호출 때 넣은 값
## 함수를 사용하는 사람
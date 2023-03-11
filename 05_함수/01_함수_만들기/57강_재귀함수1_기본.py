# 팩토리얼 연산
# - 반복문으로 구현
def factorial(n):
    output = 1
    for i in range(1, range(n + 1)):
        output *= i
    return output


# - 재귀함수로 구현
# 수학의 수열의 점화식
# 이웃한 항의 관계를 통해 수열을 나타내는 것

# 팩토리얼 점화식
def factorial(n):
    # 1! = 1
    if n == 1:
        return 1
    # (n이 2이상의 수일 때) n! = n * (n - 1)!
    if n >= 2:
        return n * factorial(n - 1)
    
print(factorial(2))
print(factorial(3))
print(factorial(4))
print(factorial(5))

# 파이썬 튜터로 흐름을 살펴보자
# 스택과 힙의 작동방식도 어느정도 알 수 있게 된다.

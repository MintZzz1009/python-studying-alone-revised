# 피보나치 수열
def f(n):
# a_1 = 1
    if n == 1:
        return 1
# a_2 = 1
    elif n == 2:
        return 1
# a_n = a_{n-1} + a_{n-2}
    else:
        return f(n - 1) + f(n - 2)
    
print(f(1))
print(f(2))
print(f(3))
print(f(4))
print(f(5))
print(f(35))
# 피보나치 수열을 재귀함수로 구성하면 실행시간이 굉장히 오래 걸린다.
# 한번 계산한 값을 다시 계산해야 하는 상황이 생긴다. 
# 이를 개선하기 위한 코드를 살펴보자

memo = {1: 1, 2: 1}
def f(n):
    if n in memo:
        return memo[n]
    # if n == 1:
    #     return 1
    # elif n == 2:
    #     return 1
    else: 
        temp = f(n - 1) + f(n - 2)
        memo[n] = temp
        return temp
    
print(f(35))
print(f(50))
# 더 큰 수를 구하려고 해도 위의 함수에 비해 값이 순식간에 출력된다.
# 위와 같이 메모를 사용하는 코드를 메모이제이션이라고 부른다.
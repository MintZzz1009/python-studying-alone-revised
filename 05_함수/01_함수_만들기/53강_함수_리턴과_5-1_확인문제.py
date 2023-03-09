# 함수의 기본형태
def sum_all(start, end):
    output = 0
    for i in range(start, end + 1):
        output += i
    return output
    
print(sum_all(1, 10))   # 55
print(sum_all(1, 100))  # 5050
print(sum_all(1, 1000)) # 500500

# 확인문제 1
def f(x):
    return 2 * x + 1
print(f(10))    # 21

def g(x):
    return x ** 2 + 2 * x + 1
print(g(10))    # 121

# 확인문제 2
def mul(*values):
    multiple_result = 1
    for value in values:
        multiple_result *= value
    return multiple_result

print(mul(5, 7, 9, 10))

# 확인문제 3
def function(valueA=10, valueB=20, *values):
    print('valueA: {}, valueB: {}, values: {}'.format(valueA, valueB, values))
function(1, 2, 3, 4, 5)
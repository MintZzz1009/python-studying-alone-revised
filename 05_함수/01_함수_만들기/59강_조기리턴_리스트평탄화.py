memo = {1: 1, 2: 1}
def f(n):
    if n in memo:
        return memo[n]
    else: 
        temp = f(n - 1) + f(n - 2)
        memo[n] = temp
        return temp
    
# 조기(early) 리턴 방식
memo = {1: 1, 2: 1}
def f(n):
    if n in memo:
        return memo[n]
    
    temp = f(n - 1) + f(n - 2)
    memo[n] = temp
    return temp


# 리스트 평탄화하는 재귀함수 만들기
def flatten(data):
    output = []
    for a in data:
        if type(a) == list:
            output.extend(flatten(a))
        else: output.append(a)
    # 코드 작성
    return output

data = [[1, 2, 3], [4, [5, 6]], 7, [8, 9]]
print(flatten(data)) # [1, 2, 3, 4, 5, 6, 7, 8, 9]
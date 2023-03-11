def solution(num):
    if num == 1:
            return 0
    
    cnt = 0
    while num != 1:
        # print(num, end='')
        if cnt == 500:
            return -1
        
        if num % 2 == 0:
            num = num / 2
            # print('->', num, end='')
        else:
            num = num * 3 + 1
            # print('->', num, end='')
        cnt += 1

    return cnt    
    



print(solution(6))
# print(solution(626331))

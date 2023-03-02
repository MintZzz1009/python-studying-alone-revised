# while 반복문
# while True:
    # 복합구문
    # 조건이 참이라면 반복
    # print('.')



# while 반복문 > for 반복문
# break 키워드
i = 0
while i < 10:
    print(f'{i}번째 반복입니다.')
    i += 1

    a = input('> 종료하시겠습니까?(y/n): ')
    if a in ['y', 'Y']:
        print('반복문을 종료합니다.')
        break


# continue 키워드
numbers = [5, 15, 6, 20, 7, 25]

for number in numbers:
    # if number >= 10:
    #     print(number)

    if number < 10:
        continue
    print(number)   
    # continue 키워드를 사용하므로 들여쓰기를 하나 제거할 수 있다는 것이 장점
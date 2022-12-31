# 입출력과 사칙연산

# 1 - 2557
A, B = map(int, input().split())
print(A + B)

# 2 - 1000
A, B = map(int, input().split())
print(A - B)

# 3 - 1001
A, B = map(int, input().split())
print(A * B)

# 4	- 10998
A, B = map(int, input().split())
print(A / B)

# 5	- 1008
A, B = map(int, input().split())
print(A+B)
print(A-B)
print(A*B)
print(A//B) 
print(A%B)

# 6	- 10869
raw_input = input()
print(raw_input + '??!')

# 7	- 10926
buddha_year = int(input())
print(buddha_year - 543)

# 8 -	18108
# 총 16개: 킹 1개, 퀸 1개, 룩 2개, 비숍 2개, 나이트 2개, 폰 8개
king, queen, rooks, bishops, knights, pawns = map(int, input().split()) # 발견한 말의 수
print(1 - king, 1 - queen, 2 - rooks, 2 - bishops, 2 - knights, 8 - pawns)

# 9	- 3003
# 다른 방법
input_pieces = list(map(int, input().split()))
rule = [1, 1, 2, 2, 2, 8]
result = []
for i in range(len(rule)):
  result.append(rule[i] - input_pieces[i])
print(*result)


# 10 - 10430
A, B, C = map(int, input().split())

print((A+B)%C)
print(((A%C) + (B%C))%C)
print((A*B)%C)
print(((A%C) * (B%C))%C)

# 11 - 2588
num1 = int(input())
num2 = input()
print(num1 * int(num2[2]))
print(num1 * int(num2[1]))
print(num1 * int(num2[0]))
print(num1 * int(num2))

# 12 - 10171
print('\\    /\\')
print(' )  ( \')')
print('(  /  )')
print(' \\(__)|')

# 13 - 10172
print('|\\_/|')
print('|q p|   /}')
print('( 0 )\"\"\"\\')
print('|"^"`    |')
print('||_/=\\\\__|')

# 14 - 25083
print('         ,r\'\"7')         
print('r`-_   ,\'  ,/')
print(' \\. \". L_r\'')
print('   `~\\/')
print('      |')
print('      |')
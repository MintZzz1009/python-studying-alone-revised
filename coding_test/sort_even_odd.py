input_number = input()
last_character = input_number[-1]
even_list = [0, 2, 4, 6, 8]
if last_character in even_list: print(f'{input_number} 는 짝수입니다.')
else: print(f'{input_number} 는 홀수입니다.')

if last_character in '02468': print('짝수')
else: print('홀수')

# 문자열 연산보다 숫자 연산이 더 빠르다
input_number = int(input_number)
if input_number % 2 == 0: print('even')
else: print('odd')
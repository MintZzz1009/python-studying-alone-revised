# 숫자를 입력받습니다.
raw_input = input('inch 단위의 숫자를 입력해주세요.\n:')

inch = int(raw_input)
cm = inch * 2.54

print('입력한 inch 단위의 숫자 ',  raw_input, '은 cm 단위의 숫자 ', cm, '으로  변환되었습니다.')
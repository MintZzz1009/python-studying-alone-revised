# 오전 오후 구분하는 프로그램

from pytz import timezone
from datetime import datetime

today = datetime.now(timezone('Asia/Seoul'))


print(f'{today.hour}시입니다!')

if today.hour < 12:
  print("오전입니다!")

if today.hour >= 12:
  print("오후입니다!")

# 계절을 구분하는 프로그램
m = today.month

if 3 <= m <= 5:
  print('봄입니다')

if 6 <= m <= 8:
  print('여름입니다')

if 9 <= m <= 11:
  print('가을입니다')

if (12 <= m) or (1<= m <= 2):
  print('겨울입니다')

# 조건문
if 조건: 복합 문장\

  # 다른 문법의 복합 문장과 비슷

  # 다름 프로그래밍 언어들은 { }, do ~ end 등을 사용해서 복합문장임을 표시한다.
  # but python은 들여쓰기로 구분한다.
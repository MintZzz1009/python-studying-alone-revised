# 날짜/시간 구하는 방법
import datetime
import pytz

pytz.timezone("Asia/Seoul")
now = datetime.datetime.now()


print(
  "{}년 {}월 {}일 {}시 {}분 {}초".format(
  now.year,
  now.month,
  now.day,
  now.hour,
  now.minute,
  now.second,
))
# 3의 배수: 각 자리 숫자의 합이 3의 배수인 경우
raw = input()
sum = 0
for chr in raw:
  sum += int(chr)
if (sum) % 3 == 0: print('3의 배수')

# 4의 배수: 십의 자리까지의 숫자가 4로 나누어 떨어지는 경우
raw = input()
l1, l2 = raw[-1], raw[-2]
if int(raw[-1]) * 10 + (int(raw[-2]) % 4) == 0: print('4의 배수')

# 5의 배수: 마지막 자리 숫자가 0 또는 5로 끝나는 경우
raw = input()
l = raw[-1]
if l == '0' or l == '5': print('5의 배수')

# 6의 배수: 짝수이면서, 각 자리 숫자의 합이 3이 배수인 경우
raw = input()
sum = 0
for n in raw:
  sum += int(n) 
if sum % 3 == 0 or int(raw) % 2 == 0: print('6의 배수')

# 9의 배수: 각 자리 숫자의 합이 9의 배수인 경우
raw = input()
sum = 0
for n in raw:
  sum += int(n)
if sum % 9 == 0: print('9의 배수')

# 10의 배수: 마지막 자리 숫자가 0으로 끝나는 경우
raw = input()
l = raw[-1]
if l == '0': print('10의 배수')



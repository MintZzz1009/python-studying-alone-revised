# 확인문제 1
print(list(range(5)))           # [0, 1, 2, 3, 4]
print(list(range(4, 6)))        # [4, 5]
print(list(range(7, 0, -1)))    # [7, 6, 5, 4, 3, 2, 1]
print(list(range(3, 8)))        # [3, 4, 5, 6, 7]
print(list(range(3, 10, 3)))    # [3, 6, 9]

# 확인문제 2
key_list = ['name', 'hp', 'mp', 'level']
value_list = ['기사', 200, 30, 5]
character = {}

for i in range(4):
    character[key_list[i]] = value_list[i]

print(character)


# 확인문제 3
answer = 0
for num in range(1, 1000000):
    answer += num
    if answer > 10000:
        print(num, answer)
        break

limit = 10000
i = 1
sum_value = 0
while sum_value <= limit:
    sum_value += i
    i += 1
print(i-1, sum_value)


# 확인문제 4
max_value = 0
a = 0
b = 0

for i in range(1, 100):
    j = 100 - i
    if max_value <= i * j:
        max_value = i * j
        a, b = i, j

print(max_value, a, b)        

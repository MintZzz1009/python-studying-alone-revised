
output_a = '{:d}'.format(52)
output_b = '{:5d}'.format(52)
output_c = '{:10d}'.format(52)
output_d = '{:07d}'.format(52)
output_e = '{:-07d}'.format(52)
output_f = '{:07d}'.format(-52)

my_num = 52
output_string1 = '{:d}, {:5d}, {:10d}, {:07d}, {:-07d}, {:07d}'.format(52, 52, 52, 52, 52, -52)
output_string2 = '{:d}, {:5d}, {:10d}, {:07d}, {:-07d}, {:07d}'.format(my_num, my_num, my_num, my_num, my_num, -my_num)
print(output_string1)
print(output_string2)

print(output_a)
print(output_b)
print(output_c)
print(output_d)
print(output_e)
print(output_f)


num_a = 45
num_b = 20.89
num_c = -36

string_nums1 = '숫자1 = {}, 숫자2 = {}, 숫자3 = {}'.format(num_a, num_b, num_c)
string_nums2 = '숫자1 = {:+}, 숫자2 = {:020d}, 숫자3 = {:=+015.0f}'.format(num_a, num_b, num_c)
print(string_nums1)
print(string_nums2)

str_a = "Hello Python Programming"
str_a.lower()
str_a.upper()
"Hello Python Programming".lower()
"Hello Python Programming".upper()

input_a = '''
    안녕하세요  
                문자열의   함수를   알아봅니다    \
'''

input_a.strip()
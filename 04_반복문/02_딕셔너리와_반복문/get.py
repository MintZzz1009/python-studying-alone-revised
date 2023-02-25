# test_dict = {'haru': 1}

# print(test_dict)
# print(test_dict['haru'])

# if 'haru' in list(test_dict.keys()):
#     print(test_dict)
# else:
#     print('없어요')

# if test_dict.get('haru') == None:
#     print('없어요')
# else:
#     print(test_dict)

# if 'haru' in test_dict:
#     print('없어요')
# else:
#     print(test_dict)

# print('haru' in test_dict)

# print(test_dict.get('haru'))

def solution(my_string):
    answer = ''
    for char in my_string:
        if char not in answer:
            answer += char
            print(answer)
    
    return my_string


print(solution('people'))
print(solution('We are the world'))
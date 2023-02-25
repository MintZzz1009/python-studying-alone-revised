# 3가지 키워드로 정리하는 핵심 포인트
# - [ 딕셔너리 ] 는 키를 기반으로 여러 자료를 저장하는 자료형입니다.
# - [ 키 ]는 딕셔너리 내부에서 값에 접근할 때 사용하는 것입니다.
# - [ 값 ]은 딕셔너리 내부에 있는 각각의 내용을 의미합니다.

# 확인문제 1
dict_a = {}
print(dict_a)

dict_a['name'] = '구름'
print(dict_a)

del dict_a['name']
print(dict_a)


# 확인문제 2
pets = [
    {'name': '구름', 'age': 5},
    {'name': '초코', 'age': 3},
    {'name': '아지', 'age': 1},
    {'name': '호랑이', 'age': 1},
]

print('# 우리 동네 애완 동물들')
for pet in pets:
    print(f"{pet['name']} {pet['age']}살")
    print(f"{pet.get('name')} {pet.get('age')}살")


# 확인문제 3
numbers = [1,2,6,8,4,3,2,1,9,5,4,9,7,2,1,3,5,4,8,9,7,2,3]
counter = {}

for number in numbers:
    if counter.get(number) == None:
        counter[number] = 1
    else:
        counter[number] += 1
print(counter)


# 확인문제 4
type("문자열") is str   # 문자열인지 확인
type([]) is list        # 리스트인지 확인
type({}) is dict        # 딕셔너리인지 확인

character = {
    'name': '기사',
    'level': 12,
    'items': {
        'sword': '불꽃의 검',
        'armor': '풀플레이트',
    },
    'skill': ['베기', '세게 베기', '아주 세게 베기']
}

for key in character:
    if type(character[key]) is dict:
        for item in character[key]:
            print(f'{item} : {character[key][item]}')
    elif type(character[key]) is list:
        for skill in character[key]:
            print(f'{key} : {skill}')
    else:
        print(f'{key} : {character[key]}')

# practice
dict = {
    'name': 'haksoo'
}

print(f'dict : {dict}')         # 딕셔너리 자체에 접근하면 키와 값 모두 호출됨
print(f"name : {dict['name']}") # 그냥 키를 통해 접근하면 값이 호출됨

for key in dict:
    print(f'key : {key}')   # 반복문을 통해서 키 자체에 접근 가능
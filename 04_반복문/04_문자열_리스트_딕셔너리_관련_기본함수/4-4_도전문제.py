# 1. 숫자의 종류
# 다음 리스트에서 몇 가지 종류의 숫자가 사용되었는지 구하는 프로그램을 만들어보세요.
# 1, 2, 3, 4가 사용되었으므로 4개가 사용되었다고 출력하면 됩니다.

a = [1, 2, 3, 4, 1, 2, 3, 1, 4, 1, 2, 3]
dict_a = {}
for i in a:
    if dict_a.get(i) == None:   # if i not in dict_a:
        dict_a[i] = 0
    dict_a[i] += 1

print(dict_a)
print(len(dict_a))


# 2. 염기의 개수
# 우리 몸은 DNA라는 설계도에 의해서 만들어집니다. 
# NA는 A(아데닌), T(티민), G(구아닌), C(사이토신)이라는 4가지 요소로 구성되는 리스트라고 볼 수 있습니다.
염기서열 = 'ctacaatgtcagtatacccattgcattagccgg'
# 염기 서열을 입력했을 때 각각의 염기가 몇 개 포함되어 있는지 세는 프로그램을 구현해보세요.

dict_염기서열 = {'a':0, 't':0, 'g':0, 'c':0}

for i in 염기서열:
    dict_염기서열[i] += 1
print(dict_염기서열)

for key, value in dict_염기서열.items():
    print(f'{key}의 개수:', value)


# 3. 염기 코돈 개수
# 이번에는 코돈의 개수를 세는 프로그램을 만들어 보세요. 
# 염기 서열은 일반적으로 3개씩 묶여서 하나의 의미를 나타냅니다. 
# 즉 다음과 같은 염기서열이 있다면
염기서열 = 'ctacaatgtcagtatacccattgcattagccggaa'
# 다음과 같이 3개씩 나뉘어서  의미를 갖는다는 말입니다.
# 이렇게 염기 3개씩 묶여 있는 것을 '코돈'이라고 부릅니다.
'cta', 'caa', 'tgt', 'cag', 'tat', 'acc', 'cat', 'tgc', 'att', 'agc', 'cgg'
dict_코돈 = {}
# 염기서열[0:3] 염기서열[3:6] 염기서열[6:9]

for i in range(0, len(염기서열), 3):

    key = 염기서열[i: i + 3]
    # if len(key) != 3:
    #     continue
    if len(key) == 3:
        print('key:', key, '\tdict_코돈.get(key):', dict_코돈.get(key))

    if dict_코돈.get(key) == None:
        dict_코돈[key] = 0
    dict_코돈[key] += 1

print(dict_코돈)
print(len(dict_코돈))


# 4. 2차원 리스트 평탄화
# 다음과 같이 리스트가 중첩되어 있을 때 중첩을 제거하는 처리를 리스트 평탄화(list flatten)라고 합니다.
# [1, 2, [3, 4], 5, [6, 7], [8, 9]] -> [1, 2, 3, 4, 5, 6, 7, 8, 9]
A = [1, 2, [3, 4], 5, [6, 7], [8, 9]]
result = []
for i in A:
    if type(i) == list:
        result += i
    else: 
        result.append(i)

print(result)
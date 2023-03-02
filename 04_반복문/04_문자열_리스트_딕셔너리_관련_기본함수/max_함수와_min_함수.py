a = [52, 273, 32, 103, 57]

print(max(a))
print(min(a))

print(max(52, 273, 32, 103, 57))
print(max(*a))  # 전개연산자

print(min(52, 273, 32, 103, 57))
print(min(*a))

print(sum(a))


# reversed( ) 함수
# 결과: 한 번만 사용 가능!
a = reversed(range(0, 10))

for i in a:
    print(i)

# a는 한 번만 사용할 수 있다. 아래 코드로 한번 더 실행해도 출력되지 않는다.
# 이런 현상이 발생하는 이유는 이후 iterator에 대해서 배울 때 다시 공부하자.
for i in a:
    print(i)


# enumerate( ) 함수
fruits = ['바나나', '사과', '포도']
a = enumerate(fruits)
print(a)
print(list(a)) # 튜플로 인덱스와 묶인다.
# 1회용이라서 다시 작성해도 출력이 되지 않는다. 
# 그래서 보통 for 반복문과 함께 사용된다.

for i, fruit in enumerate(fruits):
    print(i, fruit)   # print(fruit[0], fruit[1])


# items() 함수
a = {
    '이름': '바나나',
    '가격': 1500,
    '원산지': '말레이시아'
}

for 키, 값 in a.items():
    # print(key, a[key])    => 아래 코드가 더 직관적이다.
    print(키, 값)
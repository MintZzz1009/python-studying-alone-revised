# 기본 매개변수
def test(a = 10):
    print(a)

test() # 10
test(20) # 20
test(a = 30) # 30

# 기본 매개변수
# 여러 개의 매개변수를 입력할 때 왜 써야하는지를 알 수 있다.
def test(a = 10, b = 20):
    print(a)

test()

# b에 30
test(10, 30) 
# 이런식의 입력은 a에도 반드시 값을 입력해줘야 한다.
# 하지만 그렇게 되면 a에 기본값을 입력한 의미가 사라진다.

# 키워드 매개변수
test(b = 30)

# def test(a = 10, b): 
# b의 값을 입력하기 위해서 a에 반드시 값을 대입해야 되기 때문에
# 기본 매개변수는 기본적으로 다른 매개변수들보다 뒤에 와야 한다.
# def test(b, a = 10):  이런식으로

# 키워드 매개변수
# print() 함수의 sep, end 옵션에 대해서 알아보자.
print('안', '녕', '하', '세', '요', sep='::', end='')
print('안', '녕', '하', '세', '요', sep='::', end='')
print('안', '녕', '하', '세', '요', sep='::', end='')
# 기본 매개변수와 가변 매개변수에 대해서 잘 알면 다른 함수들을 더 잘 사용할 수 있게된다.


# 딕셔너리 매개변수
def 함수(*가변, **딕셔너리):
    print(가변, 딕셔너리)

# 딕셔너리 매개변수는 키워드 매개변수로 입력한 것이 딕셔너리 매개변수로 들어가게 된다
함수('안', '녕', '하', a=10, b=20, c=30)
# ('안', '녕', '하') {'a': 10, 'b': 20, 'c': 30}
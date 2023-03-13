# 파일 처리
# 읽기 처리 / 쓰기 처리

# 파일 읽기 처리(r 모드)

# (1) 스트림 연결(stream = 물길)
# w 쓰기 모드, a 추가해서 쓰기 모드, r 읽기 모드 
# open('경로', '모드')
파일 = open('test.txt', 'r')

# (2) 스트림을 통해 데이터를 통신
문자열 = 파일.read()
print(문자열)   # Hello World!

# (3) 스트림 해제
파일.close()

# 사람들이 하도 파일을 잘 안 닫아서 만들어 놓은 새로운 문법
with open('test.txt', 'r') as 파일:
    문자열 = 파일.read()
    print(문자열)
# 위 구문에 진입할 때, 파일을 열게 되고
# 위 구문에서 벗어날 때, 파일을 닫게 된다.


# 쓰기 모드
with open('a.txt', 'w') as 파일:
    # 파일이 없는 경우 파일을 생성하기 때문에 아무런 문제가 없다.
    # 읽기(r) 모드일 경우, 존재하지 않는 파일을 열려고 하면 오류가 뜬다.
    # FileNotFoundError: [Errno 2] No such file or directory: 'text.txt'
    파일.write('안녕하세요')
    # 문자열이 찍혀서 a .txt가 생겨난다
    print(문자열)


# 파일 처리를 배워서 나타나는 효과
# 프로그램을 한번 실행하고 끝나는 것이 아니라 연속성을 가지게 된다.

파일 = open('data.txt', 'r')
데이터 = 파일.read()
if 데이터 != '':
    print(데이터.read().strip().split('\n'))
파일.close

문자열 = input('> 데이터를 입력해주세요: ')
파일 = open('data.txt', 'a')   # append 모드
파일.write(문자열.strip() + '\n')
파일.close()
 
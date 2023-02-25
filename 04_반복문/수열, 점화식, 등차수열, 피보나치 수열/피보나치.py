N = 100
a = [None] * (N + 1)    # 수열인덱스를 일치시키기 위해서 N + 1개를 만든 것.
for n in range(1, N + 1):
    if n == 1 or n == 2:
        a[n] = 1
    else:
        a[n] = a[n-1] + a[n-2]
print(a)

# 구글에 정수열 목록을 입력한 후 만만한 것들을 입력해보자

output = [
    i
for i in range(1, 100 + 1)
if f'{i:b}'.count('0') == 1
]


for i in output:
    # print('{} : {}'.format(i, '{:b}'.format(i)))
    print(i, ':', f'{i:b}')
print('합계:', sum(output))
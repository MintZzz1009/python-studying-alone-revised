product = {
    'name': '7D 건조 망고',
    'type': '당절임'
}
print(product)
# 요소의 값을 변경하는 방법
product['name'] = '8D 건조 망고'
print(product)

# 요소를 추가하는 방법
product['price'] = 4000
print(product)

# 요소를 제거하는 방법
del product['type']
print(product)

# 키의 존재 확인하는 방법
# product['type'] # 오류
# print(product['type'])
print('price' in product) # True of False
if 'price' in product:
    print(product['price'])
else:
    print('아직 가격 요소가 없습니다')

# get() - 딕셔너리 내장 함수
print(product.get('name'))
print(product.get(''))  # 존재하지 않는 키를 호출시 오류가 아니라 None을 출력

print(product)

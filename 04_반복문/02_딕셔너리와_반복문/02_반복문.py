products = [{
    '제품명': '건망고 슬라이스',
    '가격': 4000,
    '분류': '식품',
    10: 20
}, {
    '제품명': '건망고 슬라이스',
    '가격': 4000,
    '분류': '식품',
    10: 20
}]

for product in products:
    for key in product:
        print(key)
        print(product[key])
        print()
    print('-' * 20)
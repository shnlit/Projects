amount = int(input("Введите сумму: "))

b5000 = amount // 5000
amount %= 5000

b2000 = amount // 2000
amount %= 2000

b1000 = amount // 1000
amount %= 1000

b500 = amount // 500
amount %= 500

b200 = amount // 200
amount %= 200

b100 = amount // 100

print(f"5000 руб. - {b5000} шт.")
print(f"2000 руб. - {b2000} шт.")
print(f"1000 руб. - {b1000} шт.")
print(f"500 руб. - {b500} шт.")
print(f"200 руб. - {b200} шт.")
print(f"100 руб. - {b100} шт.")
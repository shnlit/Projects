tax_rate = 0.13

income = float(input("Введите свой годовой доход: "))

income_tax = income * tax_rate
income_no_tax = income - income_tax

print(f"Общая сумма вашего дохода - {income:,.2f} руб.")
print(f"Сумма налога с вашего дохода - {income_tax:,.2f} руб.")
print(f"Сумма получаемая после вычета налога - {income_no_tax:,.2f} руб.")

weight, height = map(float, input("Введите свой вес и рост: ").split())

bmi = weight / (height * height)

print(f'Ваш ИМТ - {bmi:.1f}')
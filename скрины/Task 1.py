import math

seats_per_compartment = 4

place_in_train = int(input("Введите место в купе "))
compartment = math.ceil(place_in_train / seats_per_compartment)
print("Номер вашего купе -", compartment)

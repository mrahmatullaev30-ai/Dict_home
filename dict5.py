import os
os.system("cls")
car_count = {
    "Chevrolet": 120,
    "Toyota": 95,
    "BMW": 60,
    "Kia": 75
}

max = max(car_count.values())
min = min(car_count.values())

for a, b in car_count.items():
    if b == max:
        print("Eng ko'p sotilgan mashina:", a, b)
    if b == min:
        print("Eng kam sotilgan moshina", a, b)
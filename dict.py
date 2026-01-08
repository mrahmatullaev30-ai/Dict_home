import os
os.system("cls")

cars = {
    "Malibu": 35000,
    "Spark": 12000,
    "Cobalt": 18000,
    "Tracker": 28000
}
print("Eng Kimati:", max(cars), max(cars.values()))
print("Eng Kichigi:", min(cars), min(cars.values()))
print("Orta:", sum(cars.values()) / len(cars))

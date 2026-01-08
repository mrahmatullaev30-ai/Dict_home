import os
os.system("cls")

speed = {
    "Tesla": 250,
    "BMW": 240,
    "Mercedes": 260,
    "Audi": 230
}
for car in sorted(speed, key=speed.get, reverse=True):
    print(car, speed[car])
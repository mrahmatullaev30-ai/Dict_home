import os
os.system("cls")

professions = {
    "Bill Gates": "Dasturchi",
    "Cristiano Ronaldo": "Futbolchi",
    "Elon Musk": "Tadbirkor",
    "Messi": "Futbolchi"
}

name = input("Ismni kiriting")

print(professions.get(name, "Ism topilmadi"))
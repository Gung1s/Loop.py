import random

print()
print("-------------------Masyvų uždaviniai-------------")
print()

print()
print("-------------------Pirmas uždavinys-------------")
print()

# Sugeneruokite masyvą iš 30 elementų (indeksai nuo 0 iki 29), kurių reikšmės yra atsitiktiniai skaičiai nuo 5 iki 25.

arr = [random.randint(5,25) for i in range(30)]
print(arr, end=" ")
print()

print()
print("-------------------Antras uždavinys-------------")
print()

counter = 0
for i in arr:
    if i > 10:
        counter += 1
print(f"Reikšmių didesnių nei 10 šiame masyve yra: {counter}")
print("Didžiausia reikšmė šiame masyve yra:", max(arr))
print("Visų reikšmių suma:", sum(arr))
arr_new = [val - i for i, val in enumerate(arr)]
print(f"Naujas masyvas: {arr_new}")
print()
arr_add = (random.randint(5,25) for i in range(10))
arr.extend(arr_add)
print(f"Išplėstas masyvas: {arr}")


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
arr1 = []
arr2 = []
for i, val in enumerate(arr):
    if (i+1) % 2 == 0:
        arr2.append(val)
    else:
        arr1.append(val)
print(f"Neporiniai indeksų reikšmės: {arr1}")
print(f"Poriniai indeksų reikšmės: {arr2}")
print()
arr_zero = []
for i, val in enumerate(arr):
    if (i+1) % 2 == 1:
        arr_zero.append(val)
    else:
        if val > 15:
            arr_zero.append(0)
        else:
            arr_zero.append(val)
print(f"Masyvas, kur poriniai indeksai pakeisti į 0, jei jų reikšmė didesnė nei 15:")
print(arr_zero)

for i, val in enumerate(arr):
    if val > 10:
        break
print(f"Pirmas indeksas, kuris yra didesnis už 10: {i}")




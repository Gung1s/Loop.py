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

print()
print("-------------------Trečias uždavinys-------------")
print()

# Sugeneruokite masyvą, kurio reikšmės atsitiktinės raidės A, B, C ir D, o ilgis 200. Suskaičiuokite kiek yra kiekvienos raidės.

arr_let = [random.choice(["A", "B", "C", "D"]) for i in range(200)]
count_a = 0
count_b = 0
count_c = 0
count_d = 0
for i in arr_let:
    if i == "A":
        count_a += 1
    if i == "B":
        count_b += 1
    if i == "C":
        count_c += 1
    if i == "D":
        count_d += 1
print(arr_let)
print(f"Raidžių A: {count_a}")
print(f"Raidžių B: {count_b}")
print(f"Raidžių C: {count_c}")
print(f"Raidžių D: {count_d}")

print()
print("-------------------Ketvirta uždavinys-------------")
print()

# Išrūšiuokite 3 uždavinio masyvą pagal abecėlę.

print(sorted(arr_let))

print()
print("-------------------Penktas uždavinys-------------")
print()

# Sugeneruokite 3 masyvus pagal 3 uždavinio sąlygą. Sudėkite masyvus, sudėdami atitinkamas reikšmes.
# (turi gautis masyvas, kurio elementai, kaip pvz atrodo taip: “AAB”, “CBC”, “DDA”, 200 reikšmių).
# Paskaičiuokite kiek skirtingų reikšmių kombinacijų gavote.

arr_let1 = [random.choice(["A", "B", "C", "D"]) for i in range(200)]
arr_let2 = [random.choice(["A", "B", "C", "D"]) for i in range(200)]
arr_let3 = [random.choice(["A", "B", "C", "D"]) for i in range(200)]
print(arr_let1)
print(arr_let2)
print(arr_let3)
arr_merged = [arr_let1[i] + arr_let2[i] + arr_let3[i] for i in range(200)]
print(arr_merged)
value_unique = set(arr_merged)
value_unique_count = len(value_unique)
print(value_unique_count)

print()
print("-------------------Šeštas uždavinys-------------")
print()

# Sugeneruokite du masyvus, kurių reikšmės yra atsitiktiniai skaičiai nuo 100 iki 999. Masyvų ilgiai 100.
# Masyvų reikšmės turi būti unikalios savo masyve (t.y. neturi kartotis).

array_1 = random.sample(range(100,999), 100)
array_2 = random.sample(range(100,999), 100)
print(sorted(array_1))
print(sorted(array_2))

print()
print("-------------------Septintas uždavinys-------------")
print()

# Sugeneruokite masyvą, kuris būtų sudarytas iš reikšmių, kurios yra pirmame 6 uždavinio masyve, bet nėra antrame 6 uždavinio masyve.

array_rnd1 = []
for i in array_1:
    if i not in array_2:
        array_rnd1.append(i)
print(sorted(array_rnd1))

print()
print("-------------------Aštuntas uždavinys-------------")
print()

# Sugeneruokite masyvą iš elementų, kurie kartojasi abiejuose 6 uždavinio masyvuose.

array_rnd2 = []
for i in array_1:
    if i in array_2:
        array_rnd2.append(i)
print(sorted(array_rnd2))

print()
print("-------------------Devintas uždavinys-------------")
print()

# Sugeneruokite 10 skaičių masyvą pagal taisyklę: Du pirmi skaičiai- atsitiktiniai nuo 5 iki 25.
# Trečias, pirmo ir antro suma. Ketvirtas- antro ir trečio suma. Penktas trečio ir ketvirto suma ir t.t.

array_10 = [(random.randint(5,25)) for i in range(2)]


# array_10_plus = (array_10[i-1]+array_10[i-2] for i in range(2, 10))
# array_10.extend(array_10_plus)

array_10.extend(array_10[i-1]+array_10[i-2] for i in range(2, 10))

# for i in range(2,10):
#     array_10.append(array_10[i-1]+array_10[i-2])

print(array_10)


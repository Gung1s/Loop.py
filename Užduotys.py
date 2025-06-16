print()
print("-------------------------Lengvesni----------------------------")
print()

print()
print("-------------------------Pirma užduotis----------------------------")
print()

# Sukurkite ciklą kuris atspausdintų 10 kartų žodį “labas”.

for i in range(10):
    print("labas")

print()
print("-------------------------Antra užduotis----------------------------")
print()

# Sukurkite ciklą kuris atspausdintų skaičius nuo 0 iki 9.

for i in range(10):
    print(i)

print()
print("-------------------------Trečia užduotis----------------------------")
print()

# Sukurkite masyvą iš dešimties augalų pavadinimų.

plants = ["rožė", "tulpė", "herbera", "žibutė", "beržas", "ąžuolas", "alksnis", "ieva", "smilga", "lelija"]
print(plants)

print()
print("-------------------------Ketvirta užduotis----------------------------")
print()

# Atspausdinkite kiekvieną 3čio uždavinio augalą atskiroje eilutėje.

for plant in plants:
    print(plant)

print()
print("-------------------------Penkta užduotis----------------------------")
print()

# Atspausdinkite 3čio uždavinio kiekvieną augalą pradedant nuo paskutinio, ir baigiant pirmuoju. (atvirkščias ciklas).


rev = list(reversed(plants))
print(rev)

print()
print("-------------------------Šešta užduotis----------------------------")
print()

# Atspausdinkite kas antrą skaičių nuo 10 iki 50 (porinius);

for i in range(10,51):
    if i % 2 == 0:
        print(i)

print()
print("-------------------------Septinta užduotis----------------------------")
print()

# Atspausdinkite kas antrą skaičių nuo 10 iki 50. (porinius) Jei skaičius dalinasi iš 10 be liekanos jo nespausdinkite.
# ( naudokite continue.) (atspausdinti visus porinus skaičius, išskyrus tuos kurie dalinasi iš 10 be liekanos)

for i in range(10,51):
    if i % 10 == 0:
        continue
    if i % 2 == 0:
        print(i)

print()
print("-------------------------Aštunta užduotis----------------------------")
print()

# Sukurkite ciklą kuris suktųsi nuo 0 iki 20. Suskaičiuokite, kiek kartų kintamasis i turėjo porinę reikšmę;

count = 0
for i in range(20):
    if i > 0 and i % 2 == 0:
        count += 1
print(count)

print()
print("-------------------------Devinta užduotis----------------------------")
print()

# Suskaičiuokite kiek 3čio uždavinio masyve yra žodžių trumpesnių nei 5 simboliai, ir kiek ilgesnių nei 7 simboliai.
# (du skaičiavimai)

plants = ["rožė", "tulpė", "herbera", "žibutė", "beržas", "ąžuolas", "alksnis", "ieva", "smilga", "lelija"]
# print(plants)
count5 = 0
count6 = 0
for plant in plants:
    if len(plant) < 5:
        count5 += 1
    if len(plant) > 6:
        count6 += 1
print("trumpesnių žodžių nei 5:", count5)
print("ilgesnių žodžių nei 6:", count6)

print()
print("-------------------------Dešimta užduotis----------------------------")
print()

# Suskaičiuokite kiek 3čio uždavinio masyve yra žodžių ilgesnių nei 5 simboliai bet trumpesnių  nei 10 simboliai. (tarp 5 ir 10 simbolių ilgio)

plants = ["rožė", "tulpė", "herbera", "žibutė", "beržas", "ąžuolas", "alksnis", "ieva", "smilga", "lelija"]
count = 0
for plant in plants:
    if 5 < len(plant) < 10:
        count += 1
print("žodžių ilgesnių, nei 5 simboliai ir trumpesni nei 10 simboliai yra:", count)

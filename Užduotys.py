print()
print("-------------------------Lengvesni----------------------------")
print()
# Lengvesni
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

for i in range(10,51):
# Atspausdinkite kas antrą skaičių nuo 10 iki 50. (porinius) Jei skaičius dalinasi iš 10 be liekanos jo nespausdinkite.
# ( naudokite continue.) (atspausdinti visus porinus skaičius, išskyrus tuos kurie dalinasi iš 10 be liekanos)
print()
print("-------------------------Aštunta užduotis----------------------------")
print()
# Sukurkite ciklą kuris suktųsi nuo 0 iki 20. Suskaičiuokite, kiek kartų kintamasis i turėjo porinę reikšmę;
print()
print("-------------------------Devinta užduotis----------------------------")
print()
# Suskaičiuokite kiek 3čio uždavinio masyve yra žodžių trumpesnių nei 5 simboliai, ir kiek ilgesnių nei 7 simboliai. (du skaičiavimai)
print()
print("-------------------------Dešimta užduotis----------------------------")
print()
# Suskaičiuokite kiek 3čio uždavinio masyve yra žodžių ilgesnių nei 5 simboliai bet trumpesnių  nei 10 simboliai. (tarp 5 ir 10 simbolių ilgio)

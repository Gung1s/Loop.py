import random

print()
print("-------------------------Sunkesni----------------------------")
print()

print()
print("-------------------------Pirma užduotis----------------------------")
print()

# Sugeneruokite 300 atsitiktinių skaičių nuo 0 iki 300, atspausdinkite juos atskirtus tarpais ir
# suskaičiuokite kiek tarp jų yra didesnių už 150.  Skaičiai didesni nei 275 turi būti atspausdinti skliausteliuose” [ ] “.

numbers = (random.randint(0,300) for i in range(300))
count = 0
for x in numbers:
    if x > 150:
        count += 1
    if x > 275:
        print("[", x, "]", end=" ")
    else:
        print(x, end=" ")
print()
print("Didesnių skaičių, nei 150 yra:", count)

print()
print("-------------------------Antra užduotis----------------------------")
print()

# Vienoje eilutėje atspausdinkite visus skaičius nuo 1 iki 3000, kurie dalijasi iš 77
# be liekanos. Skaičius atskirkite kableliais. Po paskutinio skaičiaus kablelio neturi būti.

arr = [] # sukuriam masyvą
for i in range (1,3000):
    if i % 77 == 0:
        arr.append(i) # append įdedam į masyvą
print(*[i for i in arr], sep = ",")
print()

# kitas sprendimas

print(", ".join(str(i) for i in range(1, 3000) if i % 77 == 0))

print()
print("-------------------------Trečia užduotis----------------------------")
print()

# Nupieškite kvadratą iš “*”, kurio kraštines sudaro 25“*”.
# * * * * * * * * * * *
# * * * * * * * * * * *
# * * * * * * * * * * *
# * * * * * * * * * * *
# * * * * * * * * * * *
# * * * * * * * * * * *
# * * * * * * * * * * *

for i in range (25):
    print("*" * 25)

print()
print("-------------------------Ketvirta užduotis----------------------------")
print()

# Prieš tai nupieštam kvadratui nupieškite istrižaines zaigzdutę pakeisdami kitu simboliu.

for x in range (25):
    for y in range (25):
        if x == y or x + y == 24:
            print("8", end=" ")
        else:
            print("*", end=" ")
    print()

print()
print("-------------------------Penkta užduotis----------------------------")
print()

# Metam monetą. Monetos kritimo rezultatą imituojam random.randint(x,x) funkcija, kur 0 yra herbas, o 1 - skaičius.
# Monetos metimo rezultatus išvedame į ekraną atskiroje eilutėje: “S” jeigu iškrito skaičius ir “H” jeigu herbas.
# Suprogramuokite tris skirtingus scenarijus kai monetos metimą stabdome:
# Iškritus herbui;
# Tris kartus iškritus herbui;
# Tris kartus iš eilės iškritus herbui;

result = random.randint(0,1)
print(result)
if result == 1:
    result = "Skaičius"
else:
    result = "Herbas"
print(result)
print()

while True:
    result = random.randint(0,1)
    if result == 0:
        print("Herbas")
        break
    else:
        print("Skaičius")
print()
print("-------------Tris kartus iškritus herbui---------------")
print()
herbai = 0
while herbai < 3:
    result = random.randint(0,1)
    if result == 0:
        print("Herbas")
        herbai += 1
    else:
        print("Skaičius")
print()

print("-------------Tris kartus iš eilės iškritus herbui---------------")
print()
herbai = 0
while herbai < 3:
    result = random.randint(0,1)
    if result == 0:
        print("Herbas")
        herbai += 1
    else:
        print("Skaičius")
        herbai = 0

print()
print("-------------------------Šešta užduotis----------------------------")
print()

# Kazys ir Petras žaidžia šaškėm. Petras surenka taškų kiekį nuo 10 iki 20, Kazys surenka taškų kiekį nuo 5 iki 25.
# Vienoje eilutėje išvesti žaidėjų vardus su taškų kiekiu ir “Partiją laimėjo: ​laimėtojo vardas​”.
# Taškų kiekį generuokite funkcija ​random.randint(x,x)​. Žaidimą laimi tas, kas greičiau surenka 222 taškus.
# Partijas kartoti tol, kol kažkuris žaidėjas pirmas surenka 222 arba daugiau taškų.

petras_count = 0
kazys_count = 0

while petras_count < 222 and kazys_count < 222:
    petras_points = random.randint(10,20)
    kazys_point = random.randint(5,25)

    petras_count += petras_points
    kazys_count += kazys_point

    print(f"Petras: {petras_points}, Kazys: {kazys_point}")
print()

print(f"Petras: {petras_count}, Kazys: {kazys_count}")
if petras_count >= 222:
    winner = "Petras"
else:
    winner = "Kazys"
if kazys_count >= 222 and petras_count >= 222:
    if kazys_count > petras_count:
        winner = "Kazys"
    elif kazys_count < petras_count:
        winner = "Petras"
    else:
        winner = "Lygiosios"

print()
print("Partiją laimėjo:", winner)
print()

print()
print("-------------------------Septinta užduotis----------------------------")
print()

# Reikia nupaišyti pilnavidurį rombą, taip pat, kaip ir pilnavidurį kvadratą (https://lt.wikipedia.org/wiki/Rombas),
# kurio aukštis 21 eilutė.


for x in range(1, 12):
    for y in range(11 - x):
        print(" ", end = "")
    for z in range((x * 2) - 1):
        print("*", end = "")
    print()
for x in range(12, 22):
    for y in range(x - 11):
        print(" ", end = "")
    for z in range((22 - x) * 2 - 1):
        print("*", end = "")
    print()

print()
print("-------------------------Aštunta užduotis----------------------------")
print()

# Sumodeliuokite vinies kalimą. Įkalimo gylį sumodeliuokite pasinaudodami random.randint(x,x) funkcija.
# Vinies ilgis 8.5cm (pilnai sulenda į lentą).
# “Įkalkite” 5 vinis mažais smūgiais. Vienas smūgis vinį įkala 5-20 mm. Suskaičiuokite kiek reikia smūgių.
# “Įkalkite” 5 vinis dideliais smūgiais. Vienas smūgis vinį įkala 20-30 mm, bet yra 50% tikimybė
# (pasinaudokite random.randint(x,x) funkcija tikimybei sumodeliuoti), kad smūgis nepataikys į vinį.
# Suskaičiuokite kiek reikia smūgių.

counter = 0
for v in range(1,6):
    hit_deep = 0
    hits = 0
    while hit_deep < 85:
        hit = random.randint(5,20)
        hits += 1
        hit_deep += hit
    counter += hits
print()
print(f"Sukalti penkias vinis mažų smūgių reikia: {counter}")
print()

counter = 0
for v in range(1,6):
    hit_deep = 0
    hits = 0
    chance = 0
    while hit_deep < 85:
        hit = random.randint(20,30)
        hits += 1
        chance = random.randint(0,1)
        if chance == 1:
            hit_deep += hit
            print(hit, end=" ")
        else:
            print("miss", end=" ")
    counter += hits
print()
print(f"Sukalti penkias vinis didelių smūgių užteks: {counter}")
print()

print()
print("-------------------------Devinta užduotis----------------------------")
print()

# Sugeneruokite stringą, kurį sudarytų 50 atsitiktinių skaičių nuo 1 iki 200, atskirtų tarpais.
# Skaičiai turi būti unikalūs (t.y. nesikartoti). Sugeneruokite antrą stringą, pasinaudodami pirmu,
# palikdami jame tik pirminius skaičius (t.y tokius, kurie dalinasi be liekanos tik iš 1 ir patys savęs).
# Skaičius stringe sudėliokite didėjimo tvarka, nuo mažiausio iki didžiausio. (reikės split() funkcijos ir masyvų.)

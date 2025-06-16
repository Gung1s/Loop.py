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






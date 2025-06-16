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




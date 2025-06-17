import random

print()
print("-------------------------Trečia paskaita----------------------------")
print()

for i in range(5):  # range(ciklo pasikartojimai)
    print("Labas")
    print("rytas")
print("Ciklo pabaiga")
print()

num = 24
nums = [1, 2, 15, 8, 10] # masyvas (list)

print(nums)
print(nums[0]) # nurodo kelintas skaičius masyve
print(nums[-1]) # minus ženklas rodo, kad imame nuo galo
print()

nums.append(14) # prideda naują narį
print(nums)
nums[1] = 16 # pakeičiam antrą skaitmenį
print(nums)
nums.remove(16) # pašaliną skaičių 16
print(nums)
print()

games = ["zelda", "final fantasy", "gta", "nfs", "top heroes"]
print(games)
print(games[3])
print()

for number in nums:
    print(number)
print()
print(len(games)) # kiek yra elementų masyve
for zaidimas in games:
    print("My favorites game is: " + zaidimas)
print()

count = 0
for i in range(50):
    print(i)
    count += 1
print("prasisuko", count)

for i in range(10):
    if i % 2 == 0:
        continue # sustabdo pagal sąlygą ir grįžta atgal
    print(i)
print()

for i in range(1, 10):
    if i % 4 == 0:
        break # sustabdo pagal sąlygą ir nutraukia ciklą
    print(i)

# loop in loop
# while paskirtis suktis tol kol bus patenkinta sąlyga

print()
print("-------------------------While----------------------------")
print()

counter = 0
while True:
    counter += 1
    if counter >= 5:
        break
    print(counter)
print()

while True:
    rnd = random.randint(1, 6)
    print(rnd)
    if rnd == 1:
        break
print()

is_even = False

while not is_even:
    rnd = random.randint(1, 10)
    if rnd % 2 == 0:
        is_even = True
    print(rnd)

print("--------------Loop loop-------------")

for y in range(1, 11):
    for x in range(1, 11):
        print(y*x, end=" ")
    print() # po END duoda naują eilutę

print("-------------------Masyvai-----------------")

grades = [
    [1,2,2],
    [5,8,9],
    [2,8,9]
]

students = [
    ["Rima", "Beitnorę", 1988, "da"],
    ["Neringa", "Dainauskė", 1988, "da"],
    ["Lukas", "Bukauskas", 1989, "da"],
    ["Tomas", "Strelčiūnas", 1984, "da"],
]

print(students)
print()
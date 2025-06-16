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
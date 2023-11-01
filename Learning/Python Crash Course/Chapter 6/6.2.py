print("\n# 6.5. Rivers")
print("---------------------------------------------")

rivers = {
    'nile': 'egypt',
    'tennessee': 'united states',
    'rhine': 'germany',
}

for key, value in rivers.items():
    print(f"The {key.title()} runs through {value.title()}.")

print()

for key in rivers.keys():
    print(key.title())

print()

for val in rivers.values(): 
    print(val.title())

print("\n# 6.6. Polling")
print("---------------------------------------------")

favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'rust',
    'phil': 'python',
    }

names = {'john', 'jen', 'phil', 'fred'}

for name in names:
    if name not in favorite_languages:
        print(f"{name.title()}, you need to take the poll.")
    if name in favorite_languages:
        print(f"{name.title()}, thanks for taking the poll.")







print()
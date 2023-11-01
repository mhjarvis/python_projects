print("\n# 6.1. Person")
print('---------------------------------------------')
person = {
    'first_name': 'Jim',
    'last_name': 'Smith',
    'age': 22,
    'city': 'Sims',
}

for obj in person:
    print(person[obj])

print("\n# 6.2. Favorite Numbers")
print('---------------------------------------------')

fav_numbers = {
    'joe': 22,
    'ryan': 84,
    'bob': 28,
    'job': 188,
    'eee': 24,
}

for num in fav_numbers:
    print(f"{num}: {fav_numbers[num]}")

for key, value in fav_numbers.items():
    print(f"{key}: {value}")


print("\n# 6.3. Glossary")
print('---------------------------------------------')


print()

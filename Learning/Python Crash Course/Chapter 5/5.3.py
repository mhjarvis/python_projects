print("\n# 5.8 - 5.9. Hello Admin, No Users")
print("-------------------------------------------------------")
usernames = ['admin', 'Tom', 'Brian', 'Jack', 'Jill']

for name in usernames:
    if len(usernames) == 0:
        print('We need to find some users.')
    if name == 'admin':
        print('Hello Admin, would you like to see a status report?')
    else:
        print(f"Hello {name}, thank you for logging in again.")

print("\n# 5.10. Checking Usernames")
print("-------------------------------------------------------")

current_users = ['admin', 'Tom', 'Brian', 'Jack', 'Jill']
new_users = ['admin', 'Jeff', 'Tom', 'Poop']

for user in new_users:
    if user in current_users:
        print(f"'{user}' is already in use, please select another.")
    else:
        print(f"'{user}' is okay to use good Sir.")

print("\n# 5.11. Ordinal Number")
print("-------------------------------------------------------")

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]

for number in numbers:
    if number == 1:
        print('1st')
    elif number == 2:
        print('2nd')
    elif number == 3:
        print('3rd')
    else:
        print(f"{number}th")

print()
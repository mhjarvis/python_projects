inv = ['joe', 'jim']

print(f'come to dinner {inv[0]}')
print(f"{inv[0].title()} can't make it to dinner.")

inv[0] = 'mike'

print(f'Can you come to dinner {inv[0].title()}?')
print('Hey idiots, I found a bigger table!')

inv.insert(0, 'jack')
inv.insert(2, 'jake')
inv.append('don')

print(inv)

print('looks like i am going to have to drop a bunch of you')

inv.pop()
inv.pop()

print(f"{inv[0]} and {inv[1]}, are you guys coming?")

del inv[0]
del inv[0]
del inv[0]

print(inv)

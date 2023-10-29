values = [1, 2, 3, 4, 5, 6, 7, 8, 9]

#4.10
print(f"The first three items are {values[0 : 3]}")
print(f"The items from the middle are {values[3 : 6]}")
print(f"The items at the end are {values[-3 :]}")

#4.11
friend_pizzas = ['Cheese', 'Pepperoni', 'Sausage']
friend_pizzas.append('Veggie')
newPizza = friend_pizzas[:]
newPizza.append('worm')

print(friend_pizzas)
print(newPizza)

# tuples in a list that cannot change
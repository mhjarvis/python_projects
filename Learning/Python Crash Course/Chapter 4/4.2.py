#4.3
for val in range(1, 21):
    print(val)

million = list(range(1, 1000001))
#print(million)

#4.4
print(min(million))
print(max(million))
print(sum(million))

#4.5
x = list(range(1, 20, 2))
for bit in x:
    print(bit)


#4.6
newList = list(range(3, 30, 3))
for val in newList:
    print(val)

#4.8
cubes = [value ** 3 for value in range(1, 11)]
for cube in cubes:
    print(cube)

#4.9
newCubes = [value ** 3 for value in range(1, 11)]
print(newCubes)
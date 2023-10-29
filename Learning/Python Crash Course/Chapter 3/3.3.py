print()
arr = ['Germany', 'London', 'Amerika', 'Antartica', 'Brazil']
print('Unsorted: ', arr)

arr = sorted(arr)
print('Sorted', arr)

arr.reverse()
print('Reversed: ', arr)

arr.reverse()
print('Back to original: ', arr)

arr.sort()
print('Sorted: ', arr)

arr.sort(reverse=True)
print('Reverse Alphabetical: ', arr)

print('Number of countries: ', len(arr))
#Lists

fruits = ["apple", "banana", "cherry", "peach"]

print(fruits)
print(fruits[1])

fruits[1] = "blackberry"

print(fruits)
print(fruits[1])

#adding items to list

print(fruits)
fruits.append("strawberry")
print(fruits)

fruits.insert(1, "grape")
print(fruits)

#remove from list
fruits.remove('apple')
print(fruits)

fruits.sort()
print(fruits)
fruits.sort(reverse=True)
print(fruits)
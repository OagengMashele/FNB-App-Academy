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

#Tuples
# cannot change,no duplicates

my_tuple = (1,5,2,3,4,6)
print(my_tuple)
print(my_tuple[0])
print(my_tuple[4])
print(my_tuple[-1])

#concatination and repetition
tuple1 = (1,2,3)
tuple2 =(4,5,6)

print(tuple1)
print(tuple2)

conc_tuple = tuple1 + tuple2
print(conc_tuple)

rep_tuple = tuple1 * 2
print(rep_tuple)

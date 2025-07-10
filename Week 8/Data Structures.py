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
# cannot change

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

#Sets
#no duplicates

my_set = {1,2,3,4,5,"apple"}
print(my_set)

my_set.add("banana")
print(my_set)
my_set.remove(2)
print(my_set)

set1 = {1,2,3}
set2 = {3,4,5}

print(set1)
print(set2)
#Union
union_set = set1.union(set2)
print(union_set)
#intersection
intersect_set = set1.intersection(set2)
print(intersect_set)
#difference
diff_set = set1.difference(set2)
difff_set = set2.difference(set1)
print(diff_set)
print(difff_set)

#Dictionaries
#collection of jkey value pairs

my_dict = {"apple": 2, "banana": 6, "orange": 9}
print(my_dict)
print(my_dict["apple"])

my_dict["cherry"] = 5
print(my_dict)

my_dict["apple"] = 1
print(my_dict)
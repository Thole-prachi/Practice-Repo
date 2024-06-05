'''list methods: append : adding new value to the list at the end 
sort : sort the list by ascending order if you add reverse=true to it it will sort by descending order
reverse: reverse the original list
index: print the value index value of the item if item comes multiple time it will print 1st occurance of it
count : count the occurance of item in list
copy : copy the original list in another variable whatever you provide and if you make any changes in copy it will not affect the original list
insert: in this user has to provide on which index we have add the specified item in list
extend: if you create new list and wanted to add in old list you can do that using extend method any data type will work in this case be it tuple,set 
dictionary it put value at the end of old list
concatenating 2 list: you can concatenet means add 2 list =  + list2 = list3'''

#Practice of list methods 

fruits = ["apple", "cherry", "blueberry", "Banana"]
all_fruits = ["fig", "appricoat"]

# fruits[0] = "Mango"
# print (fruits)

fruits.append("watermelon")
print(fruits)

fruits.insert(0,"Mango")
print(fruits)

fruits.remove("cherry")
print(fruits)

removed_fruits = fruits.pop(2)
print(fruits)
print (removed_fruits)

# fruits.clear()
# print(fruits)

print(fruits[:4])
print(fruits[1:3])
print(fruits[-3:])

sum_fruits = fruits + all_fruits
print(sum_fruits)

repeated_fruits = fruits * 2
print(repeated_fruits)
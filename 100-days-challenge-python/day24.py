'''Datatype : Tuple: Tupels are ordered collection of data items. they store multiple items in sigle variable.items are seprated by comma and 
enclosed in () Tuples are unchangeble we can not alter them after creation. '''

# countries1 = ('spain', 'Italy', 'India', 'england', 'germany')
# countries2 = ('afganistan', 'srilanka', 'bangladesh', 'pakistan')
# # temp = list(countries)
# # temp.append("russia")
# # temp.pop(3)
# # temp[2] = 'finland'
# # countries = tuple(temp)
# # print(countries)

# southeast = countries1 + countries2
# print(southeast)


#Practice1

lst = (1,3,'test',1.24 , [1,3,5])
# print(lst[1])
# first_three = lst[:3]
# last_two = lst[-2:] 
# print(first_three)
# print(last_two)

# tup2 = lst + (100,200)

# tup3 = lst * 3

# print(tup2)
# print(tup3)

#Check in 
# check_in = 'test' in lst
# check_in_num = 0 in lst

# print(check_in)
# print(check_in_num)

#iterating through tuple

# for i in lst:
#     print(i)

#Unpack Assignment of element to other variable

# a , b, c, *rest = lst
# print(f"a: {a}, b: {b}, c: {c}")
# print(f"rest of tumple element: {rest}")


#Nested tuple 1st calculate complete tuple len then go for 1st element then inside that 2nd value as we have passed 2 index
# nested_tup = (1, (2, 3,4), (4, 5, 6))

# innner_ele = nested_tup[1][2]

# print(innner_ele)


# print (lst)
# print(type(lst))

# lst1 = ()
# print(type(lst1))

# lst2 = (1,)
# print(type(lst2))


# Conversion of list tuple and vice versa
lst_tup = [1, 2, 3, 4]
tup_lst = tuple(lst_tup)
print(type(tup_lst))

tup2 = (1, 2, 3, 4)
lst_tup1 = list(tup2)
print(lst_tup1)
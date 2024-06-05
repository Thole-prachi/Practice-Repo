'''List as a Data type use cases and understanding how it works.
List is a order collection of data items
We can store multiple items in single variable you can add kinds of data in it which means we can add numbers , string , boolean in list
items in list seprated by commans and enclosed in [] bracket.
we can changes values inside list after creation we can call item from list using index value which start from 0 
when someone asked or you mention length of list it will start from  1 I mean if you have 5 items in list 5 is length and index value will end
at 4 index calculation start from 0 and length count start from 1
negative index when try to print it minus in with length of list and get the positive index value and print that positive index value 
no need to do it in actual programming as this is what python do behind the scene.
to find any item in list if it is present or not you can use "in"keyword for it by using this in key word we can find particular alphabet or string present or not
refer "navi" example


'''
#use of in key word
# marks = [3, 5, 7, 8, 2, 12, "navi"]
# if 7 in marks:
#     print("yes")
# else:
#     print("no")

# print (marks[0]) # printing of 0th index value
# # print(len(marks)) # print the length of list
# print(marks[-3]) # print the value of negative index in this case it will print 8 how read above description

# if "navi" in marks:
#     print("Yes")
# if "s" in "navi": #finding keyword inside string item which is present in list
#     print ("a is present")
# else:
#     print("No")

# if you want to print the complete list or from any specific index you can do that like below

# print(marks)
# print(marks[:]) #print complete list
# print(marks[1:]) #print from index one 
# print(marks[:3]) #print items from 0 to 2 index value  
# print(marks[1:-4]) #negative index print
# print(marks[1:4]) # just to get list to understand below concept
# print(marks[1:4:2]) # jump index value by 2 1 start ,4 end , 2 jump by you can jump by any value 2, 3, or any value 

'''list comprehension : where you will create list on the go without passing predefined values to the list
'''

# lst = [i*i for i in range (5)]
# print (lst)

# lst = [i*i for i in range (10) if i % 2 == 0]
# print (lst)

#List practice question : create list and access it using index no.

# list = ["Apple", "Banana", "Mango", "Jackfruit", "Cherry"]

# print(list[0])
# print(list[-1])
# print(list[4])
# print(list[:])
# print(len(list))
# print(list[1:3])
# print(list[:2])

#list comprehestion example

squares = [x**2 for x in range(1,10)]
print(squares)

evens = [x for x in range(1,20) if x%2 == 0 ]
print (evens)
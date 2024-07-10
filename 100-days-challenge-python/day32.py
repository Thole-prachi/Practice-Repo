'''Set methods: In this we will see methods which we can use on set Joining sets:1. method : union :it is combination of 2 sets if any value common in those it get prints only once
update method : in this element of s2 or s21 will get updated like s1 update all values those are present in s2 viceversa duplicate value will ignore it just got printed once
intersection and intersection update : it prints those items which are common in both groups, and in intersection update : only those value will get updated which are 
present in both sets like in our ex. 3,5 , Symmetric differnce : it will print those values which are not common in both sets it means 3,5 will get removed or ignored
differnce and difference update :  it only prints original value of difference set like in our case it ignore duplicate values and the unique values which are present in s2
 differnce update is same like above update it just get those values which are original ignore duplicate and unique value of s2 too
 some in-built methods of set like isdisjoint : it checks if same items present in another set or not if not it prints true if present it prints false
  2nd in-built : issuperset : it checks if all items present in original set (in our case s1 ) check with another set if it is then print true or false   
  3rd in-built: issubset : it checks if all items are present in original set are present in another set if it is presnt then it prints true or false it only give true when all values are same if any extar value in original set it prints false
   add method to add extra values in set , Update : if you want to add more than one item , simply create another set or anyother iterable object like list, tuple , dictionary
 and use the update() method to add values in existing set. remove/ discard : remove the item from set , if you use remove to remove the item which is not part of set it will throw error if you use discard it will not through any error
  pop (): it remove any last item(not compulsary that it will remove last item only) of set as set are unorder collection so we don't have any cotrol on poping item.
   del : it is not method , it is keyword it help you to delete the entire set , clear : if we just want to remove items of set not entire set then we can use clear
  In keyword : if you want to find out if any xyz value is present in set or not you can use in
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      '''

# s1 = {1, 2, 3,5}
# s2 = {4,9,7,8}

s1 = {2,3,5,4,7}
s2 = {4,5,7,3}
# print(s1.union(s2))
# s1.update(s2)
# print(s1)
# s3 = s1.intersection(s2)
# print (s3)
# s1.intersection_update(s2)
# print (s1)

# s4 = s1.symmetric_difference(s2)
# print(s4)
# s1.symmetric_difference_update(s2)
# print(s1)

# s5 = s1.difference(s2)
# print(s5)
# s1.difference_update(s2)
# print(s1)

# print(s1.isdisjoint(s2))

# print(s1.issuperset(s2))

# print(s1.issubset(s2))

# s1.add(10)
# print(s1)

# s1.update(s2)
# print(s1)

# item = s1.pop()
# print(s1)
# print(item)

if 1 in s1:
    print ("1 is present in s1 set")
else:
    print ("1 is not present in s1")







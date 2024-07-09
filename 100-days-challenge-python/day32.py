'''Set methods: In this we will see methods which we can use on set Joining sets:1. method : union :it is combination of 2 sets if any value common in those it get prints only once
  update method : in this element of s2 or s21 will get updated like s1 update all values those are present in s2 viceversa duplicate value will ignore it just got printed once
    intersection and intersection update : it prints those items which are common in both groups, and in intersection update : only those value will get updated which are 
      present in both sets like in our ex. 3,5 , Symmetric differnce : it will print those values which are not common in both sets it means 3,5 will get removed or ignored
         differnce and difference update :  it only prints original value of difference set like in our case it ignore duplicate values and the unique values which are present in s2
         '''

s1 = {1, 2, 3,5}
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
s1.difference_update(s2)
print(s1)





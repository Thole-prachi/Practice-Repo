''' Datatype set : set is unorder collection of data items. They store multiple item is single variable. 
set items are comma seperated and enclosed in {} set are  unchangebel meaning you cannot change items of the set  once created.
sets do not contain duplicate items.'''

s = {2,6,4,2} #in this case it will not print 2 again just print it once.
print(type(s) ,s)


info = {"carla", 19, False, 5.9, 19}
for i in info:
    print(i)


'''In set order of printing is  not maintanied so you can not print them by passing index no. and it won't allow duplicate entry
you canot directly create empty set as representation of set and dictinary is similar using {}  so if you want to create empty set refer below method'''

s1 = set()
print(type(s1), s1)
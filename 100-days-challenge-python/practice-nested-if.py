grade = int(input("enter obtained grade: "))

'''A= 90
B= 70 -80
c = 60 -70
d = 70-50
f =20-30'''

if (grade >= 90):
    print("you are in group A")
elif (grade > 70 and grade <=80):
    print("you are in group B")
elif (grade >60 and grade <=70):
    print ("you are in group C")
elif (grade <70 and grade >=50):
    print("you are in group D")
else:
    print("you are in group F. Repeat exam")


# if (num < 0):
#     print("number is negative")
# elif (num > 0):
#     if (num <= 10):
#         print("number is between 1-10")
#     elif (num > 10 and num <= 20):
#         print("number is in the range of 11-20")
#     else:
#         print("num is greated than 20")
# else:
#     print("number is 0")
#Function practice code
#Instead of tytping gmean logic again and again we can create function and call it.
# def calculategmean(a,b):
#     gmean = (a*b)/(a+b)
#     print(gmean)

# a = 90
# b = 80
# calculategmean(a,b)

# c = 3
# d = 4
# calculategmean(c,d)

# sum of 2 numbers practice function

# def sum(a,b):
#     sums = (a+b)
#     print (sums)


# a = int(input("enter 1st number for addition: "))
# b= int(input("enter 2nd num for addition: "))
# sum(a,b)

# c = 6
# d = 8
# sum(c,d)

# check even and odd

# def iseven (a):
#     if a % 2 == 0:
#         print("number is even")
#     else:
#         print("number is odd")

# a = int(input("enter value to check if even or odd: "))
# iseven(a)

# b = 6
# iseven(b)


#find the maximum of 3 numbers

# def max_of_three(a,b,c):
#     return max(a,b,c)

# print(max_of_three(1,7,9))
# print(max_of_three(-9,-4,-1))

#Write factorial 


# def facto(a):
#     factorial = 1
#     if a > 0:
#         for i in  range(1, a + 1):
#             factorial*= i
#         return factorial
#     else:
#         return 1
#         # print (f"The factorial {a} is : Factorial")
# print (facto(5))

# reversed string

def reverse_string(s):
    return s[::-1]

print (reverse_string("Hello"))
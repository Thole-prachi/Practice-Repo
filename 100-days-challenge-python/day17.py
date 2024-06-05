# colors = ["Red", "Green","blue", "Yellow","orange"]
# for color in colors:
#     print(color)
#     for i in color:
#         print (i)

# for step in range(1,10,2):
#     print(step)
# num = range(1,11)
# for i in num:
#     print (i)

# num = 0
# for i in range(1,101):
#     num += i
#     print(num)

# finding even number (1,21)

# for i in range(1,21):
#     if i %2  ==0:
#         print (i)

# mul = int(input("enter the value for multiplication: "))
# print(f",multiplcation table of (mul):  ")
# for i in range(1,11):
#     print(f"{mul} x {i} = {mul * i}")

# Calculate factorial

# num = int(input("enter no. for factorial calculation: "))

# factorial = 1
# #Chevk if num passed is valid or not
# if num > 0:
#     print ("num is positive and non zero")
#     for i in  range(1, num +1):
#         factorial *= i
#     print (f"The factorial {num} is : Factorial")
# else:
#     print("Please pass valid num value.")

#count no of vowels in given string

# note = "I am in the right place, at the right time, doing the right thing."
# vowels = ('a','e','i','o','u','A','E','I','O','U')

# for char in note:
#     if char in vowels:
#         print(f"'{char}'it is vowel")
#     else:
#         print(f"'{char}'It is constant")

#check the max value in list

# num_list =[1,4,5,8,34,98,100,234,76,500,900,988,1]

# max_num = num_list[0]


# for i in num_list:
#     if i > max_num:
#         max_num = i
# print (f"this is max no. all amongs: {max_num} ")

# Print the pattern in order value

# star = "*"
# for i in range(1,7):
#     print(star * i) # * this is mothing but multiplication don't miss interpret it as a variable *

#sum of even no. using for loop 

# sum_num = 0

# for i in range (0,101):
#      if i % 2 == 0:
#         sum_num += i
# print("The sum of even number in range 1-51 is: ",sum_num)


#Addition of 1 to 100
sum = 0

for i in range(1,100):
    sum +=i
print(sum)








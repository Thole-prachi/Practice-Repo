# break and continue practice with while and for loop 
# print the number which come first and it it divisible by 5 from below list

# numbers = [2, 5, 8, 9, 6, 24, 43, 45, 15, 25]

# for number in numbers:
#     if number % 5 == 0:
#         print("The first number which is divisible by 5 is : ",number)
#         break

#Continue example Print all the numbers from 1-10 except 5


# for i in range(1,11):
#     if i == 5:
#         continue
#     print (i)

# combination of break and continue statement
#Task: Iterate through a list of numbers and print each number. If you encounter a number greater than 10, stop the loop. Skip printing the number 7.


numbers = [2, 5, 8, 9, 6, 7, 10, 24, 43, 45, 15, 25]

for number in numbers:
    if number > 10:
        break
    if number == 7:
        continue
    print(number)
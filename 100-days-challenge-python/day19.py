#What is break and continue : break means once condition got satisfied it break the loops or we can say come  out of loop and for continue
#if continue condition got true it skip that particular part like if you don't want to print vatule 7 then add it in continue statement
#once it reach till 7 it check condition skip printing of 7 print the next number in list program run continue in this state.

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
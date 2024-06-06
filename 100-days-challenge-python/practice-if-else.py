# applePrice = int(input("current apple price: "))
# budget = int(input("my budget is: "))

# if applePrice >= budget:
#     print("don't add apples in cart.")
# else:
#     print("it is in budget adding apples in cart.")


# BMI calculater

# weight = float(input("Enter your weight: "))
# height = float(input("Enter your height in feet: "))

# #bmi calculator 
# bmi = weight / (height ** 2)

# if bmi <18.5:
#     print("underweight")
# elif 18.5 <= bmi < 25:
#     print("normal weight")
# elif 25 <= bmi < 30:
#     print("overweight")
# else:
#     print ("obese")

# Number comparision 

# num1 = int(input("enter num1 value: "))
# num2 = int(input("enter num2 value: "))

# if num1 > num2:
#     print("num1 is greated than num2: ",num1)
# elif num1 < num2:
#     print("num2 is greater than num1: ",num2)
# else:
#     print("selected numbers for comparision is equal: ",num1)

#Advanced number comparision
# Number comparison

# num1 = int(input("Enter num1 value: "))
# num2 = int(input("Enter num2 value: "))

# # Compare numbers
# if num1 > num2:
#     print("num1 is greater than num2:", num1)
# elif num1 < num2:
#     print("num2 is greater than num1:", num2)
# else:
#     print("num1 and num2 are equal:", num1)

# # Absolute difference
# diff = abs(num1 - num2)
# print("Absolute difference between num1 and num2:", diff)

# # Maximum and minimum
# maximum = max(num1, num2)
# minimum = min(num1, num2)
# print("Maximum of num1 and num2:", maximum)
# print("Minimum of num1 and num2:", minimum)

# # Odd/Even check
# if num1 % 2 == 0:
#     print("num1 is even")
# else:
#     print("num1 is odd")

# if num2 % 2 == 0:
#     print("num2 is even")
# else:
#     print("num2 is odd")

# # Positive/Negative/Zero check
# if num1 > 0:
#     print("num1 is positive")
# elif num1 < 0:
#     print("num1 is negative")
# else:
#     print("num1 is zero")

# if num2 > 0:
#     print("num2 is positive")
# elif num2 < 0:
#     print("num2 is negative")
# else:
#     print("num2 is zero")

# # Range check
# if 0 <= num1 <= 100:
#     print("num1 is within the range [0, 100]")
# else:
#     print("num1 is outside the range [0, 100]")

# if 0 <= num2 <= 100:
#     print("num2 is within the range [0, 100]")
# else:
#     print("num2 is outside the range [0, 100]")



# wishing code depend on time
import time
timestamp = time.strftime("%H:%M:%S")
# print (timestamp)
hour = int(time.strftime('%H'))
hour = int(input("Enter time : "))
print (hour)

if (hour>0 and hour<12):
    print("Hello, Good Morning")
elif (hour>12 and hour<16):
    print("Hello, Good Afternoon")
elif (hour>=16 and hour<21):
    print("Hello Good Evening")
else:
    print("Hello Good Night")


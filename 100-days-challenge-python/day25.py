# F-string practice which formats the print output if we put someting in {} by adding "f" in start of print line.examples are below.

# user = input("Enter your name: ")

# greetings= (f"Hello {user},Very Good Morning. Wishing you Fantastic day ahead {user}")

# print(greetings)

num1 = float(input("Enyter value for num1: "))
num2 = float(input("Enter value for num2: "))

sum = f"The sum of {num1} and {num2} is: {num1+num2}"
sub = f"The sub of {num1} and {num2} is: {num1-num2}"
mul = f"The mul of {num1} and {num2} is: {num1*num2}"
div= f"The Div of {num1} and {num2} is {num1/num2:.2f}"  # print the value of division till 2 decimal points meaning it should be written like this ":.2f"

print(sum)
print(sub)
print(mul)
print (div)
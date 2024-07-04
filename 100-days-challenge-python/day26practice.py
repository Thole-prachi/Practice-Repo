#My own practice  for basic

#perform addition of 2 numbers by taking user input

# num1 = int(input("Enter value for num1: "))
# num2 = int(input("Enetr value for num2: "))

# addition = num1 + num2
# print(addition)

#function practice 
# def add (a,b):
#     addition = a + b
#     print(addition)

# add(9,4)
# add(67,7)

#for loop 

# lst = ['docker', 'kubernetes', 'jenkins', 'git', 'ansible', 'Terraform']

# for i in lst:
#     print(i)
#     for j in i:
#         print(j)

#while loop + if else and f string 

user_input = ""

while user_input != "exit":
    user_input = input("Enter your name (or type 'exit' to stop): ")
    user_input_captalize = user_input.capitalize() # so to convert user input 1st alphabet in uppercase u have to create new variable where you call username variable.
    if user_input == 'exit':
        print("Exiting the loop , GoodBye!")
    else:
        print(f"Hello {user_input_captalize}!")


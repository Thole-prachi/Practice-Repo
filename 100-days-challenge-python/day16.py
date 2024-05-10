#Example of match case statement

# day_of_week = input("enter day of the week: ")

# match day_of_week:
#     case "Monday":
#         print("Start of week")
#     case "Tuesday":
#         print("Early in week")
#     case _:
#         print("mid of the week")


#Match case statement for year of month printing

# year_of_month = int(input("enter the value of 1-12 to print the Month: "))

# match year_of_month:
#     case 1:
#         print ("It's Jan")
#     case 2:
#         print("it's Feb")
#     case 3:
#         print("it's mar")
#     case 4:
#         print("it Apr")
#     case 5:
#         print("it May")
#     case 6:
#         print("it Jun")
#     case  7:
#         print("it Jul")
#     case 8:
#         print("it Aug")
#     case 9:
#         print("it sep")
#     case 10:
#         print("it Oct")
#     case 11:
#         print("it Nov")
#     case 12:
#         print("it Dec")
#     case _:
#         print("Print valida number")

#Match case state ment example to print if it is vowel , constant or neither working

# character = input("Please enter any character between A-Z, a-z : ")

# match character.lower():
#     case 'a':
#         print("Vowel")
#     case 'b':
#         print("constant")
#     case 'c':
#         print("constant")
#     case 'd':
#         print("constant")
#     case 'e':
#         print("constant")
#     case 3:
#         print("neither")


#Chantgpt code not working
# character = input("Please enter any character between A-Z, a-z: ")

# match character.lower():
#     case 'a', 'e', 'i', 'o', 'u':
#         print("Vowel")
#     case 'b', 'c', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'm', 'n', 'p', 'q', 'r', 's', 't', 'v', 'w', 'x', 'y', 'z':
#         print("Consonant")
#     case _:
#         print("Neither")
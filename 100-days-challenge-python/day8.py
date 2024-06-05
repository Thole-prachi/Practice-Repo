nm = "        !!Prachi!!!!! !!!!!  !kiran   !!!navish!!  navish  kiran prachi"
print (nm[-4:-2])
print (len(nm))
print (nm.upper())
print(nm.lower())
#Replacing prachi with kiran
print(nm.replace("Prachi","Kiran"))
#removing last strip of ! from prachi it only remove end strip not from start of string
print(nm.strip("!"))
#Conversion of nm variable data which include space into list form
print(nm.split (" "))

# for conversting 1st character of start of line convert into uppercase
blogheading= "introduction to python\ni love chocolates\nnavish is a coolest baby "
print(blogheading.capitalize())

#moving heading line of blog to center

str1 = "Welcometothezoo"
print(len(str1))
print(len(str1.center(50)))
print(str1.center(42))
#print the no. of occurance of particular word in string

print(nm.count("navish"))

#isend()versifying if the mention string ends with some mention value or character or not it also having isstart() which will find start of string data
#we can even check in between part of string for any specific word or character
print(nm.endswith("kiran"))
print(nm.endswith("!", 9, 11))

#finding the 1st occurance of any word/character in string sentence it will print the index value of it
#if it won't be able to find required details it will print -1 as output
print(nm.find("P"))

#index incase of index even it we gave wrong to find it will print error message use case of it is when you want prog. has to failed if it didn't find requested data
print(nm.index("!"))

#isalnum if yout strint includes alphanumeric value (a-z,A-Z,0-9) it will print true if not it will print false if space is present in string it will print false for true output you have to remove space
print(nm.isalnum( ))
print(str1.isalnum())
#isalpha if a-z and A-Z are present in string it will print true or false
print(nm.isalpha())
print(str1.isalpha())

#islower if all character of string is in lower case or not true and false output format also having isupper which work same like this
print(nm.islower())
#isprintable means there is no presence of \n or \t or anything which is not print on scree if it found o/p will be false vice versa
print(nm.isprintable())

#isspace if we apply space between character using space bar it will return true or false it reads only blank space if it is present in string or we can say complete blank string 
print(nm.isspace())
str2 = "    "
print(str2.isspace())

#istitle it is more useful when you are blogging or doing some documenation kind of thing o/p is true and false format
print(str1.istitle())
print(nm.istitle())

#swapcase convert lowercase to uppercase and viseversa
print(nm.swapcase())

#title convert capitalized 1st character of each word in string
print(nm.title())


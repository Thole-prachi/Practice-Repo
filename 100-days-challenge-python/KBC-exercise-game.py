'''KBC Game program'''
import time

gamer = input("Enter your Name: ")

print ("Hello",gamer)

age = int(input("Enter your age: "))

print("Your age is:",age)

print ("Welcome to KBC game",gamer)

questions = ["Which animal is known as the 'Ship of the Desert'?","How many days are there in a week?","How many hours are there in a day?","How many letters are there in the English alphabet?","Rainbow consist of how many colours?","How many days are there in a year?","How many minutes are there in an hour?","How many seconds are there in a minute?","How many seconds make one hour?","How many consonants are there in the English alphabet?"]

answer = ["Question no.1 Answer is : Camel","Question no.2 Answer is : 7 Days","Question no.3 Answer is : 24 Hours","Question no.4 Answer is : 26 Alphabet","Question no.5 Answer is : 7 colors","Question no.6 Answer is : 365Days","Question no.7 Answer is : 60 Minute","Question no.8 Answer is :60 Seconds","Question no.9 Answer is : 3600 Seconds","Question no.10 Answer is : 21 Constants"]
print(len(answer))
print (len(questions))

# Printing each question and ask user to enter answer
for index,question in enumerate(questions,start=1):
    print(f"{index}.{question}")
    time.sleep(1)
    for question in answer
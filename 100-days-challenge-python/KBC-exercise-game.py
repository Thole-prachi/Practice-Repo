'''KBC Game program'''
import time

gamer = input("Enter your Name: ")

print ("Hello",gamer)

age = int(input("Enter your age: "))

print("Your age is:",age)

print ("Welcome to KBC game",gamer)

questions = ["Which animal is known as the 'Ship of the Desert'?","How many days are there in a week?","How many hours are there in a day?","How many letters are there in the English alphabet?","Rainbow consist of how many colours?","How many days are there in a year?(Exclude leap year)","How many minutes are there in an hour?","How many seconds are there in a minute?","How many seconds make one hour?","How many consonants are there in the English alphabet?"]

answer = ["Camel","7","24","26","7","365","60","60","3600","21"]

score = 0
winning_score = 7

# print(len(answer))
# print (len(questions))

# Printing each question and ask user to enter answer
for index,question in enumerate(questions,start=1):
    print(f"{index}.{question}")
    # time.sleep(2)
    attempt = 2
    while attempt > 0:
        participant_answer = (input(f"Please enter answer for question {index}:  "))
        time.sleep(3)
        if participant_answer == answer[index - 1]:
            print("answer is correct")
            score += 5
            break
        else:
            attempt -= 1
            score -= 1
            if attempt > 0:
                print(f"anwer is incorrect. try again you have {attempt} {'attempt' if attempt > 1 else 'attempt'} left.")
            else:
                print (f"answer is incorrect. you have no attempt left. The correct answer is : {answer[index -1]}")
if score >= winning_score * 5:
    print (f"congratulation {gamer}! you win the game with score {score}.")
else:
    print(f"you lose the game with {score}. Better luck next time!")



    

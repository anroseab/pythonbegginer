import random

score=20
randomNumber=random.randint(0,10)

while True:
    userInput=int(input("ENter an number"))
    
    if userInput == randomNumber:
           print("Congrats u guessed right your score is" +str(score))
           break
    else:
           print("Better luck next time")
           score-=1
           if userInput>randomNumber:
                print("too high")
           elif userInput<randomNumber:
                 print("too  low")

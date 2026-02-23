import random

target=random.randint(1,10)

while True :
    guess=int(input("Guess Number btw 1-100"))
    if(guess<0 and guess>100):
        print("valif range is 1 to 100 only")
        continue
    
    elif(guess==target):
        print("you guess it right")
        break
    else:
        print('Try again buddy ')


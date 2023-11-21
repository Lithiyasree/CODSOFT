import random
r=1
tie=0
your_score=0
computer_score=0
while True:
    print("ROUND:",r)
    you=input("Enter your choice (rock,paper,scissors):").lower()
    computer=random.choice(["rock","paper","scissors"])
    print("your choice:",you)
    print("computer choice:",computer)
    if(you==computer):
        print("It's a TIE....")
        tie+=1
        r+=1
    elif((you=="rock" and computer=="scissors")or(you=="scissors" and computer=="paper")or(you=="paper" and computer=="rock")):
        print("You WIN...")
        your_score+=1
        r+=1
    elif((you=="scissors" and computer=="rock")or(you=="paper" and computer=="scissors")or(you=="rock" and computer=="paper")):
        print("Computer WINS....")
        computer_score+=1
        r+=1
    else:
        print("invalid input")
    again_play=input("Do you want to play again (y/n):").lower()
    if(again_play!="y"):
        break
print("YOUR SCORE IS:",your_score)
print("COMPUTER SCORE:",computer_score)
print(tie,"rounds tie")

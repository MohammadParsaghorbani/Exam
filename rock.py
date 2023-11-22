import random
random_option="notdefind"
winner="notdefind"
rnd_score=0
player_score=0
rnd=random.randint(0,2)
print("**********rock,paper,scissor**********")
player=input("enter your option: ")
if rnd==0:
    random_option="rock"
elif rnd==1:
    random_option="paper"
else:
    random_option="scissor"
if random_option=="rock" and player=="rock":
    print("robot said:",random_option)
    print("nobody win!")
elif random_option=="rock" and player=="paper":
    print("robot said:",random_option)
    print("player win!")
    player_score=player_score+1
elif random_option=="rock" and player=="scissor":
    print("robot said:",random_option)
    print("robot win!")
    rnd_score=rnd_score+1
elif random_option=="paper" and player=="rock":
    print("robot said:",random_option)
    print("robot win!")
    rnd_score=rnd_score+1
elif random_option=="paper" and player=="paper":
    print("robot said:",random_option)
    print("nobody win!")
elif random_option=="paper" and player=="scissor":
    print("robot said:",random_option)
    print("player win!")
    player_score=player_score+1
elif random_option=="scissor" and player=="rock":
    print("robot said:",random_option)
    print("player win!")
    player_score=player_score+1
elif random_option=="scissor" and player=="paper":
    print("robot said:",random_option)
    print("player win!")
    rnd_score=rnd_score+1
elif random_option=="scissor" and player=="scissor":
    print("robot said:",random_option)
    print("nobody win!")
if rnd_score>player_score:
    winner="robot"
else:
    winner="player"
print(f"************so,{winner} is the winner!************")
again=input("do you want to play again?y/n: ")
while again=="y":
    print("**********rock,paper,scissor**********")
    player=input("enter your option: ")
    if rnd==0:
        random_option="rock"
    elif rnd==1:
        random_option="paper"
    else:
        random_option="scissor"
    if random_option=="rock" and player=="rock":
        print("robot said:",random_option)
        print("nobody win!")
    elif random_option=="rock" and player=="paper":
        print("robot said:",random_option)
        print("player win!")
        player_score=player_score+1
    elif random_option=="rock" and player=="scissor":
        print("robot said:",random_option)
        print("robot win!")
        rnd_score=rnd_score+1
    elif random_option=="paper" and player=="rock":
        print("robot said:",random_option)
        print("robot win!")
        rnd_score=rnd_score+1
    elif random_option=="paper" and player=="paper":
        print("robot said:",random_option)
        print("nobody win!")
    elif random_option=="paper" and player=="scissor":
        print("robot said:",random_option)
        print("player win!")
        player_score=player_score+1
    elif random_option=="scissor" and player=="rock":
        print("robot said:",random_option)
        print("player win!")
        player_score=player_score+1
    elif random_option=="scissor" and player=="paper":
        print("robot said:",random_option)
        print("player win!")
        rnd_score=rnd_score+1
    elif random_option=="scissor" and player=="scissor":
        print("robot said:",random_option)
        print("nobody win!")
    if rnd_score>player_score:
        winner="robot"
    else:
        winner="player"
    print(f"************so,{winner} is the winner!************")
    again=input("do you want to play again?y/n: ")
#gool/pooch
import random
player=input("plz enter your hand:left/right: ")
p_score=0
rnd_score=0
winer="notdefind"
p_hand="notdefind"
random_hand="notdefind"
if player=="left":
    p_hand="left"
elif player=="right":
    p_hand="right"
ran=random.randint(0,1)
if ran==0:
    random_hand="left"
else:
    random_hand="right"
if p_hand==random_hand:
    rnd_score=rnd_score+1
    winer="ran"
    print("robot win the game!")
    while winer=="ran":
        ran=random.randint(0,1)
        if ran==0:
            random_hand="left"
        else:
            random_hand="right"
        player=input("enter hand that you want to serch:l/r: ")
        if player=="l":
            p_hand="left"
        elif p_hand=="r":
            p_hand="right"
        if p_hand==random_hand:
            winer="player"
            p_score=p_score+1
            winer="player"
            print("player win the game!")
            while winer=="player":
                ran=random.randint(0,1)
                if ran==0:
                    random_hand="left"
                else:
                    random_hand="right"
                player=input("enter hand that you want to put paper in:l/r: ")
                if player=="l":
                    p_hand="left"
                elif p_hand=="r":
                    p_hand="right"
                if p_hand==random_hand:
                    winer="ran"
                    rnd_score=rnd_score+1
                else:
                    print("robot answer is wrong!")
                    p_score_score=p_score+1
                stop=input("do you want to play more?y/n: ")
                if stop=="n":
                    break
        if stop=="n":
            break
        else:
            print("your answer is wrong!")
            rnd_score=rnd_score+1
        stop=input("do you want to play more?y/n: ")
        if stop=="n":
            break
else:
    p_score_score=p_score+1
    winer="player"
    print("player win the game!")
    while winer=="player":
        ran=random.randint(0,1)
        if ran==0:
            random_hand="left"
        else:
            random_hand="right"
        player=input("enter hand that you want to put paper in:l/r: ")
        if player=="l":
            p_hand="left"
        elif p_hand=="r":
            p_hand="right"
        if p_hand==random_hand:
            winer="ran"
            rnd_score=rnd_score+1
        else:
            print("robot answer is wrong!")
            p_score_score=p_score+1
        stop=input("do you want to play more?y/n: ")
        if stop=="n":
            break
final_winer="notdefind"
if p_score>rnd_score:
    final_winer="player"
else:
    final_winer="robot"
print(f"{final_winer} is final winer!")
#exame
s=lambda score1,score2,score3,score4,score5:score1+score2+score3+score4+score5
wrong=0
l="nothing"
name=input("enter your name: ")
name2=input("f/m: ")
lastName=input("enter your last name: ")
chairnumber=input("enter your chair number:")
age=int(input("enter your age: "))
if age in list(age):
    print(f"dear{name},thay are the quistion: ")
    print("first qustion:")
    print("which one is the best time for sleap in your age?")
    q_1=input("a.9:00 PM    b.11:00 PM    c.12:00 PM     d.1:00 AM          your answer: ")
    if q_1=="a":
        score1 =4
    elif q_1!="a":
        score1=0
        wrong=wrong+1
    print("qustion2: 2+2*3+(4+6/2)")
    q_2=input("a.12     b.14     c.15       d.19        your answer: ")
    if q_2=="c":
        score2=4
    elif q_2!="c":
        score2=0
        wrong=wrong+1
    print("qustion 3 : we make new paper with: ")
    q_3=input("a.tree     b.recicle paper     c.the old paper     d. b and c      your answer: ")
    if q_3 =="d":
        score3=4
    elif q_3!="d":
        score3=0
        wrong=wrong+1
    print("qustion 4 : How many layers does the earth have?")
    q_4=input("a.4      b.3      c.2     d.5   your answer: ")
    if q_4=="b":
        score4=4
    elif q_4!="b":
        score4=0
        wrong=wrong+1
    print("qustion 5: who hc daryosh ?")
    q_5=input("a.father of khashazar     b.son of korosh    c.builder of takht jamshid      d.all of them   your answer: ")
    if q_5=="d":
        score5=4
    elif q_5!="d":
        score5=0
        wrong=wrong+1
    add=score1+score2+score3+score4+score5
    print("======================================")
    print(f"your score {add} the correct answer: ")
    print("1.a      2.c     3.d     4.b     5.d")
    print(f"you have {wrong} misteke")
elif age not in list(age):
    wrong=0
    if name2=="f":
        l="Mrs"
    else:
        l="mr"
    print(f"{l}.{name},they are your qustion: ")
    print("==============================")
    print("what are the Social harm?")
    q_1=input("a.aggression     b.aggression . quarrel . addiction    c.quarrel and addiction     d.aggression and addiction      your answer: ")
    if q_1=="a":
        score1=4
    elif q_1!="a":
        score1=0
        wrong=wrong+1
    print("qustion 2: In the sieve of numbers 1 to 100. The number 100 is the number that is underlined?")
    q_2=input("a.the last   b.100th     c.50th      d.20th      your answer: ")
    if q_2=="c":
        score2=4
    elif q_2!="c":
        score2=0
        wrong=wrong+1
    print("qustion3:In a simple electric circuit, how many ohms is the resistance if the battery is 24 volts and the ammeter is 0.03?")
    q_3=input("a.400    b.2400    c.200     d.800     ypur answer: ")
    if q_3=="d":
        score3=4
    elif q_3!="d":
        score3=0
        wrong=wrong+1
    print("qustion4:what is the best time for sleaping in your age: ")
    q_4=input("a.12:00PM    b.10:00PM   c.11:30PM   d.3:00AM    your answer: ")
    if q_4=="b":
        score4=4
    elif q_4!="b":
        score4=0
        wrong=wrong+1
    print("qustion5: At what age did the Prophet reach his mission?")
    q_5=input("a.30     b.35     c.40     d.20      your answer: ")
    if q_5=="c":
        score5=4
    elif q_5!="c":
        score5=0
        wrong=wrong+1
    add=(s(score1,score2,score3,score4,score5))
    print("======================================")
    print(f"your score {add} . the correct answer: ")
    print("1.a      2.c     3.d     4.b     5.c")
    print(f"you have {wrong} misteke")
#################################################################

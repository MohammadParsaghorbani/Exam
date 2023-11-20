#odd and even
a=[]
c=[]
b=int(input("enter number: "))
if b%2!=0:
    c.append(b)
elif b%2==0:
    a.append(b)
d=str(input("do you want to add new number?y/n: "))
while d=="y":
    b=int(input("enter number: "))
    if b%2!=0:
        c.append(b)
    elif b%2==0:
        a.append(b)
    d=str(input("do you want to add new number?y/n: "))
print(f"odd number={c} and even number= {a}")
######################################************************************########################################
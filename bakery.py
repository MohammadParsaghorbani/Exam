#welcome to parsa shop
a=0
b=0
c=0
d=0
e=0
f=0
g=0
h=0
i=0
j=0
k=0
l=0
m=0
n=0
o=0
p=0
q=0
r=0
s=0
t=0
u=0
tipe=["grains","cereal","dairy","protein","unhelthy food"]
grains=["cotyledons","lentils","Beans"]
cotyledons=lambda cotyledons:cotyledons*13000
lentils=lambda lentils:lentils*15000
Beans=lambda Beans:Beans*12500
cereal=["atmosphere","Rice","wheat","corn"]
atmosphere=lambda atmosphere:atmosphere*17000
Rice=lambda Rice:Rice*26500
wheat=lambda wheat:wheat*22750
corn=lambda corn:corn*20000
dairy=["yogurt","milk","Cheese"]
milk=lambda milk:milk*15000
Cheese=lambda Cheese:Cheese*17000
yogurt=["500g","1000g","1500g"]
yogurt_500g=lambda yogurt_500g:yogurt_500g*15000
yogurt_1000g=lambda yogurt_1000g:yogurt_1000g*20000
yogurt_1500g=lambda yogurt_1500g:yogurt_1500g*25000
protein=["Meat","fish"]
Meat=["veal","lamb"]
Meat_Veal=lambda Meat_Veal:Meat_Veal*350000
Meat_Lamb=lambda Meat_Lamb:Meat_Lamb*330000
fish=["gheselala","sefid","osonbron","kapor"]
fish_ghesel=lambda fish_ghesel:fish_ghesel*150000
fish_sefid=lambda fish_sefid:fish_sefid*140000
fish_osonbron=lambda osonbron:osonbron*13500000
fish_kapor=lambda fish_kapor:fish_kapor*170000
unhelthy=["sauce","hamburger","Sandwich"]
unhelthy_sauce=lambda unhelthy_sauce:unhelthy_sauce*35000
unhelthy_hamburger=lambda unhelthy_hamburger:unhelthy_hamburger*200000
unhelthy_Sandwich=lambda unhelthy_Sandwich:unhelthy_Sandwich*175000
print("==========Welcome to Parsa shop!==========")
customer_name=input("dear customer,what is your name? ")
print(f"{customer_name}!such a graet name!")
print("hear,we have a meno for you . the meno from the tipe of food!")
again="nothing"
stop=""
while again!="no":
    print("*****************************")
    print("*          grains           *")
    print("*          cereal           *")
    print("*          dairy            *")
    print("*          protein          *")
    print("*       unhelthy food       *")
    print("*****************************")
    customer_chois=input("which one do you chose? ")
    while customer_chois not in (tipe):
        customer_chois=input("please enter existing item: ")
    if customer_chois=="grains":
        print("for grains,we have this item:")
        print("*********************")
        print("*  cotyledons=13000 *")
        print("*  lentils=15000    *")
        print("*  Beans=12500      *")
        print("*********************")
        customer_chois=input("which one do you want? ")
        while customer_chois not in (grains):
            customer_chois=input("please enter existing item: ")
        if customer_chois=="cotyledons":
            how_many=int(input("how many: "))
            a=cotyledons(how_many)
            print("==========================")
            print(f"until now,you must pay{a+b+c+d+e+f+g+h+i+j+k+l+m+n+o+p+q+r+s+t+u}")
        elif customer_chois=="lentils":
            how_many=int(input("how many: "))
            b=lentils(how_many)
            print(f"until now,you must pay{a+b+c+d+e+f+g+h+i+j+k+l+m+n+o+p+q+r+s+t+u}")
        elif customer_chois=="Beans":
            how_many=int(input("how many: "))
            c=Beans(how_many)
            print(f"until now,you must pay{a+b+c+d+e+f+g+h+i+j+k+l+m+n+o+p+q+r+s+t+u}")
    elif customer_chois=="cereal":
        print("for cereal,we have this items:")
        print("*********************")
        print("*  atmosphere=17000 *")
        print("*  Rice=26500       *")
        print("*  wheat=22750      *")
        print("*  corn=20000       *")
        print("*********************")
        customer_chois=input("please enter existing item: ")
        while customer_chois not in (cereal):
            customer_chois=input("please enter existing item: ")
        if customer_chois=="atmosphere":
            how_many=int(input("how many: "))
            d=atmosphere(how_many)
            print("==========================")
            print(f"until now,you must pay{a+b+c+d+e+f+g+h+i+j+k+l+m+n+o+p+q+r+s+t+u}")
        elif customer_chois=="Rice":
            how_many=int(input("how many: "))
            e=Rice(how_many)
            print(f"until now,you must pay{a+b+c+d+e+f+g+h+i+j+k+l+m+n+o+p+q+r+s+t+u}")
        elif customer_chois=="wheat":
            how_many=int(input("how many: "))
            f=wheat(how_many)
        elif customer_chois=="corn":
            how_many=int(input("how many: "))
            g=corn(how_many)
            print(f"until now,you must pay{a+b+c+d+e+f+g+h+i+j+k+l+m+n+o+p+q+r+s+t+u}")
    elif  customer_chois=="dairy":
        print("for grains,we have this item:")
        print("*********************")
        print("*  milk=15000       *")
        print("*  Cheese=17000     *")
        print("*  yogurt           *")
        print("*********************")
        customer_chois=input("which one do you want? ")
        while customer_chois not in (dairy):
            customer_chois=input("please enter existing item: ")
        if customer_chois=="milk":
            how_many=int(input("how many: "))
            h=milk(how_many)
            print("==========================")
            print(f"until now,you must pay{a+b+c+d+e+f+g+h+i+j+k+l+m+n+o+p+q+r+s+t+u}")
        elif customer_chois=="Cheese":
            how_many=int(input("how many: "))
            i=Cheese(how_many)
            print(f"until now,you must pay{a+b+c+d+e+f+g+h+i+j+k+l+m+n+o+p+q+r+s+t+u}")
        elif customer_chois=="yogurt":
            print("which one?")
            print("*********************")
            print("*       500g        *")
            print("*       1000g       *")
            print("*       1500g       *")
            print("*********************")
            customer_chois=input("whish one do you want? ")
            while customer_chois not in (yogurt):
                customer_chois=input("please enter existing item: ")
            if customer_chois=="500g":
                how_many=int(input("how many: "))
                j=yogurt_500g(how_many)
                print(f"until now,you must pay{a+b+c+d+e+f+g+h+i+j+k+l+m+n+o+p+q+r+s+t+u}")
            elif customer_chois=="1000g":
                how_many=int(input("how many: "))
                k=yogurt_1000g(how_many)
                print(f"until now,you must pay{a+b+c+d+e+f+g+h+i+j+k+l+m+n+o+p+q+r+s+t+u}")
            elif customer_chois=="1500g":
                how_many=int(input("how many: "))
                l=yogurt_1500g(how_many)
                print(f"until now,you must pay{a+b+c+d+e+f+g+h+i+j+k+l+m+n+o+p+q+r+s+t+u}")
    elif customer_chois=="protein":
        print("for grains,we have this item:")
        print("*********************")
        print("*        Meat       *")
        print("*        fish       *")
        print("*********************")
        customer_chois=input("which one do you want? ")
        while customer_chois not in (protein):
            customer_chois=input("please enter existing item: ")
        if customer_chois=="Meat":
            print("we have this tipe of Meat:")
            print("*******************")
            print("*   Veal=350000   *")
            print("*   lamb=330000   *")
            print("*******************")
            customer_chois=input("which one do you want? ")
            while customer_chois not in list(Meat):
                customer_chois=input("please enter existing item: ")
            if customer_chois=="Veal":
                how_many=int(input("how many: "))
                t=Meat_Veal(how_many)
                print(f"until now,you must pay{a+b+c+d+e+f+g+h+i+j+k+l+m+n+o+p+q+r+s+t+u}")
            elif customer_chois=="lamb":
                how_many=int(input("how many: "))
                u=Meat_Lamb(how_many)
                print(f"until now,you must pay{a+b+c+d+e+f+g+h+i+j+k+l+m+n+o+p+q+r+s+t+u}")
        elif customer_chois=="fish":
            print("***************************")
            print("*    gheselala=150000     *")
            print("*    sefid=140000         *")
            print("*    osonbron=13500000    *")
            print("*    kapor=170000         *")
            print("***************************")
            customer_chois=input("which one do you want? ")
            while customer_chois not in (fish):
                customer_chois=input("please enter existing item: ")
            if customer_chois=="gheselala":
                how_many=int(input("how many: "))
                n=fish_ghesel(how_many)
                print(f"until now,you must pay{a+b+c+d+e+f+g+h+i+j+k+l+m+n+o+p+q+r+s+t}")
            elif customer_chois=="sefid":
                how_many=int(input("how many: "))
                o=fish_sefid(how_many)
                print(f"until now,you must pay{a+b+c+d+e+f+g+h+i+j+k+l+m+n+o+p+q+r+s+t+u}")
            elif customer_chois=="osonbron":
                how_many=int(input("how many: "))
                p=fish_osonbron(how_many)
                print(f"until now,you must pay{a+b+c+d+e+f+g+h+i+j+k+l+m+n+o+p+q+r+s+t+u}")
            elif customer_chois=="kapor":
                how_many=int(input("how many: "))
                p=fish_kapor(how_many)
                print(f"until now,you must pay{a+b+c+d+e+f+g+h+i+j+k+l+m+n+o+p+q+r+s+t+u}")
    elif customer_chois=="unhelthy food":
        print("*************************")
        print("*    sauce=35000        *")
        print("*    hamburger=200000   *")
        print("*    Sandwich=175000    *")
        print("*************************")
        customer_chois=input("which one do you want? ")
        while customer_chois not in (unhelthy):
            customer_chois=input("please enter existing item: ")
        if customer_chois=="sauce":
            how_many=int(input("how many: "))
            q=unhelthy_sauce(how_many)
            print(f"until now,you must pay{a+b+c+d+e+f+g+h+i+j+k+l+m+n+o+p+q+r+s+t+u}")
        elif customer_chois=="hamburger":
            how_many=int(input("how many: "))
            r=unhelthy_hamburger(how_many)
            print(f"until now,you must pay{a+b+c+d+e+f+g+h+i+j+k+l+m+n+o+p+q+r+s+t+u}")
        elif customer_chois=="Sandwich":
            how_many=int(input("how many: "))
            s=unhelthy_Sandwich(how_many)
            print(f"until now,you must pay{a+b+c+d+e+f+g+h+i+j+k+l+m+n+o+p+q+r+s+t+u}")
    again=input("do you want to by enything else? ")
print(f"so,you must pay{a+b+c+d+e+f+g+h+i+j+k+l+m+n+o+p+q+r+s+t+u}T")
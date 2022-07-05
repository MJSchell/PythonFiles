m=input("What would you like to order? ([1]Sandwhich, [2]Drink, [3]Fries, [4]Sauce, [5]Icecream, [6]Quit, [7]Mistake)")
t=0
a=9
c=9
b=9
d=9
z=float(0)
x=float(0)
ls=""
pac=0
top=0
it=float(0)
icetop=0
while m!=6:
    m=int(m)
    if m==5:
        c=3
        i=input('What Icecream would you like? ([1]Chocolate, [2]Vanilla, [3]Twist, [4]Strawberry, [5]Mint, [6]Back')
        while c==3:
                i=int(i)
                it=0
                if i==1:
                    print("You Ordered Chocolate")
                    flav="Chocolate"
                    it=it+.5
                    icetop=input("What Topping Would You Like?([1]M&M, [2]Cookie Dough, [3]Sprinkles, [4]Peanuts, [5]Gummy Worms")
                    icetop=int(icetop)
                    if icetop==1:
                        print('you ordered M&Ms')
                        top=' w/ M&Ms'
                        it+.25
                    if icetop==2:
                        print('you ordered Cookie Dough')
                        top=' w/ Cookie Dough'
                        it+.75
                    if icetop==3:
                        print('you ordered Sprinkles')
                        top=' w/ Sprinkles'
                        it+.50
                    if icetop==4:
                        print('you ordered Peanuts')
                        top=' w/ Peanuts'
                        it+.50
                    if icetop==5:
                        print('you ordered Gummy Worms')
                        top=' w/ Gummy Worms'
                        it+1
                    t=t+it
                    ls+=f'''
                    {flav} {top}            +${it}'''
                    i=input('What Icecream would you like? ([1]Chocolate, [2]Vanilla, [3]Twist, [4]Strawberry, [5]Mint, [6]Back')
                    i=int(i)
                if i==2:
                    print("You Ordered Vanilla")
                    flav="Vanilla"
                    it=it+.5
                    icetop=input("What Topping Would You Like?([1]M&M, [2]Cookie Dough, [3]Sprinkles, [4]Peanuts, [5]Gummy Worms")
                    icetop=int(icetop)
                    if icetop==1:
                        print('you ordered M&Ms')
                        top=' w/ M&Ms'
                        it+.25
                    if icetop==2:
                        print('you ordered Cookie Dough')
                        top=' w/ Cookie Dough'
                        it+.75
                    if icetop==3:
                        print('you ordered Sprinkles')
                        top=' w/ Sprinkles'
                        it+.50
                    if icetop==4:
                        print('you ordered Peanuts')
                        top=' w/ Peanuts'
                        it+.50
                    if icetop==5:
                        print('you ordered Gummy Worms')
                        top=' w/ Gummy Worms'
                        it+1
                    t=t+it
                    ls+=f'''
                    {flav} {top}            +${it}'''
                    i=input('What Icecream would you like? ([1]Chocolate, [2]Vanilla, [3]Twist, [4]Strawberry, [5]Mint, [6]Back')
                    i=int(b)
                if i==3:
                    print(1,"You Ordered Twist")
                    flav="Twist"
                    it=it+.75
                    icetop=input("What Topping Would You Like?([1]M&M, [2]Cookie Dough, [3]Sprinkles, [4]Peanuts, [5]Gummy Worms")
                    icetop=int(icetop)
                    if icetop==1:
                        print('you ordered M&Ms')
                        top=' w/ M&Ms'
                        it+.25
                    if icetop==2:
                        print('you ordered Cookie Dough')
                        top=' w/ Cookie Dough'
                        it+.75
                    if icetop==3:
                        print('you ordered Sprinkles')
                        top=' w/ Sprinkles'
                        it+.50
                    if icetop==4:
                        print('you ordered Peanuts')
                        top=' w/ Peanuts'
                        it+.50
                    if icetop==5:
                        print('you ordered Gummy Worms')
                        top=' w/ Gummy Worms'
                        it+1
                    t=t+it
                    ls+=f'''
                    {flav} {top}            +${it}'''
                    i=input('What Icecream would you like? ([1]Chocolate, [2]Vanilla, [3]Twist, [4]Strawberry, [5]Mint, [6]Back')
                    i=int(i)
                if i==4:
                    print(1,"You Ordered Strawberry")
                    flav="Strawbery"
                    it=it+1.00
                    icetop=input("What Topping Would You Like?([1]M&M, [2]Cookie Dough, [3]Sprinkles, [4]Peanuts, [5]Gummy Worms")
                    icetop=int(icetop)
                    if icetop==1:
                        print('you ordered M&Ms')
                        top=' w/ M&Ms'
                        it+.25
                    if icetop==2:
                        print('you ordered Cookie Dough')
                        top=' w/ Cookie Dough'
                        it+.75
                    if icetop==3:
                        print('you ordered Sprinkles')
                        top=' w/ Sprinkles'
                        it+.50
                    if icetop==4:
                        print('you ordered Peanuts')
                        top=' w/ Peanuts'
                        it+.50
                    if icetop==5:
                        print('you ordered Gummy Worms')
                        top=' w/ Gummy Worms'
                        it+1
                    t=t+it
                    ls+=f'''
                    {flav} {top}            +${it}'''
                    i=input('What Icecream would you like? ([1]Chocolate, [2]Vanilla, [3]Twist, [4]Strawberry, [5]Mint, [6]Back')
                    i=int(i)
                if i==5:
                    print(1,"You Ordered Mint")
                    flav="Mint"
                    it=it+1.00
                    icetop=input("What Topping Would You Like?([1]M&M, [2]Cookie Dough, [3]Sprinkles, [4]Peanuts, [5]Gummy Worms")
                    icetop=int(icetop)
                    if icetop==1:
                        print('you ordered M&Ms')
                        top=' w/ M&Ms'
                        it+.25
                    if icetop==2:
                        print('you ordered Cookie Dough')
                        top=' w/ Cookie Dough'
                        it+.75
                    if icetop==3:
                        print('you ordered Sprinkles')
                        top=' w/ Sprinkles'
                        it+.50
                    if icetop==4:
                        print('you ordered Peanuts')
                        top=' w/ Peanuts'
                        it+.50
                    if icetop==5:
                        print('you ordered Gummy Worms')
                        top=' w/ Gummy Worms'
                        it+1
                    t=t+it
                    ls+=f'''
                    {flav} {top}            +${it}'''
                    i=input('What Icecream would you like? ([1]Chocolate, [2]Vanilla, [3]Twist, [4]Strawberry, [5]Mint, [6]Back')
                    i=int(i)
                elif i==6:
                    m=input("What would you like to order? ([1]Sandwhich, [2]Drink, [3]Fries, [4]Sauce, [5]Icecream, [6]Quit, [7]Mistake)")
                    m=int(m)
                    c=9
                else:
                    print('Sorry, Please Try Again!')
                    i=input('What Icecream would you like? ([1]Chocolate, [2]Vanilla, [3]Twist, [4]Strawberry, [5]Mint')
                    i=int(i)
    if m==2:
            c=1
            b=input("What size drink do you want?([1]S, [2]M, [3]L, [4]Back)")
            while c==1:
                b=int(b)
                if b==1:
                    print("You Ordered a Small Drink for $1.00")
                    t=t+1.00
                    b=input("What size drink do you want?([1]S, [2]M, [3]L, [4]Back)")
                    b=int(b)
                    ls=ls+f"""
                    Small drink     +$1.00"""
                if b==2:
                    print("You Ordered a Medium Drink for $1.75")
                    t=t+1.75
                    b=input("What size drink do you want?([1]S, [2]M, [3]L, [4]Back)")
                    b=int(b)
                    ls=ls+f"""
                    Medium drink    +$1.75"""
                if b==3:
                    print(1,"You Ordered a Large Drink for $2.00")
                    t=t+2.00
                    b=input("What size drink do you want?([1]S, [2]M, [3]L, [4]Back)")
                    b=int(b)
                    ls=ls+f""" 
                    Large drink     +$2.00"""
                elif b==4:
                    m=input("What would you like to order? ([1]Sandwhich, [2]Drink, [3]Fries, [4]Sauce, [5]Icecream, [6]Quit, [7]Mistake)")
                    m=int(m)
                    c=9
                else:
                    print('Sorry, Please Try Again!')
                    b=input("What size drink do you want?([1]S, [2]M, [3]L, [4]Back)")
                    b=int(b)
    elif m==1:
            c=0
            a=input("What type of sandwich ([1]chicken $5.25, [2]beef $6.25, [3]tofu $5.75, [4]Back)")
            while c==0:
                a=int(a)
                if a==1:
                    print('You chose the Number 1, chicken $5.25')
                    t=t+5.25
                    a=input("What type of sandwich ([1]chicken $5.25, [2]beef $6.25, [3]tofu $5.75, [4]Back)")
                    a=int(a)
                    ls=ls+f"""
                    Chicken         +$5.25"""
                elif a==2:
                    print('You chose the Number 2, beef $6.25')
                    t=t+6.25
                    a=input("What type of sandwich ([1]chicken $5.25, [2]beef $6.25, [3]tofu $5.75, [4]Back)")
                    a=int(a)
                    ls=ls+f"""
                    Beef            +$6.25"""
                elif a==3:
                    print('You chose the Number 3, tofu $5.75')
                    t=t+5.75
                    a=input("What type of sandwich ([1]chicken $5.25, [2]beef $6.25, [3]tofu $5.75, [4]Back)")
                    a=int(a)
                    ls=ls+f"""
                    Tofu            +$5.75"""
                elif a==4:
                    c=9
                    m=input("What would you like to order? ([1]Sandwhich, [2]Drink, [3]Fries, [4]Sauce, [5]Icecream, [6]Quit, [7]Mistake)")
                    m=int(m)
                else:
                    print('Sorry, Please Try Again!')
                    a=input("What type of sandwich ([1]chicken $5.25, [2]beef $6.25, [3]tofu $5.75, [4]Back")
                    a=int(a)

    elif m==3:
            c=2
            d=input("What size fries do you want?([1]S, [2]M, [3]L, [4]Back)")
            while c==2:
                d=int(d)
                if d==1:
                    print("You Ordered a Small Fry for $0.75")
                    t=t+0.75    
                    d=input("What size fries do you want?([1]S, [2]M, [3]L, [4]Back)")
                    d=int(d)
                    ls=ls+f"""
                    Small Fry       +$0.75"""
                elif d==2:
                    print("You Ordered a Medium Fry for $1.50")
                    t=t+1.50
                    d=input("What size fries do you want?([1]S, [2]M, [3]L, [4]Back)")
                    d=int(d)
                    ls=ls+f"""
                    Medium Fry      +$1.50"""
                elif d==3:
                    print("You Ordered a Large Fry for $2.00")
                    t=t+2.00
                    d=input("What size fries do you want?([1]S, [2]M, [3]L, [4]Back)")
                    ls=ls+f"""
                    Large Fry       +$2.00"""
                    d=int(d)
                elif d==4:
                    m=input("What would you like to order? ([1]Sandwhich, [2]Drink, [3]Fries, [4]Sauce, [5]Icecream, [6]Quit, [7]Mistake)")
                    m=int(m)
                    c=9
                else:
                    print('Sorry, Please Try Again!')
                    d=input("What size fries do you want?([1]S, [2]M, [3]L, [4]Back)")
                    d=int(d)
    elif m==4:
        sau=input("What Sauce Would you like?")
        pac=input("How many Packets do you want?(numbers only)")
        pac=int(pac)
        pacnum=pac*.75
        t=t+pacnum
        pac=str(pac)
        sau=str(sau)
        pacnum=str(pacnum)
        print("You ordered "+pac+" "+sau+" for $"+pacnum)
        ls=ls+f"""
                    {pac} {sau}           +${pacnum}"""
        m=input("What would you like to order? ([1]Sandwhich, [2]Drink, [3]Fries, [4]Sauce, [5]Icecream, [6]Quit, [7]Mistake)")
        m=int(m)
    elif m==7:
        print('Sorry To Hear That!, Please Try Again!')
        t=float(0.00)
        ls=""
        m=input("What would you like to order? ([1]Sandwhich, [2]Drink, [3]Fries, [4]Sauce, [5]Icecream, [6]Quit, [7]Mistake)")
    else:
        print('Sorry, Please Try Again!')
        m=input("What would you like to order? ([1]Sandwhich, [2]Drink, [3]Fries, [4]Sauce, [5]Icecream, [6]Quit, [7]Mistake)")
        m=int(m)
t=float(t)
z=t*0.07
x=z+t
dis=0
t=round(t,2)
x=round(x,2)
z=round(z,2)
z=str(z)
x=str(x)
t=str(t)
'''
while dis!="N"or"n":
    dis=input("Do you have a discount code? (Y, N)")
    if dis=="Y"or"y":
        ban=input("What is the discount code?")
        if ban=="Bander" or "bander":
            x=0
            dis="N"
            print(f"""
            Your subtotal is:    ${t}
                      Tax is:    ${z}
               Your total is:    ${x}
            """)
        else:
            print("Wrong Discount Code")
            dis="N"
            print(f"""
            Your subtotal is:    ${t}
                      Tax is:    ${z}
               Your total is:    ${x}
            """)
    else:
        print(f"""
            Your subtotal is:    ${t}
                    Tax is:      ${z}
            Your total is:       ${x}
            """)
'''
print(f"""  
            Thank You For Visiting Good Burger!
            -----------------------------------
            {ls}
            -----------------------------------
            Your subtotal is:       ${t}
              (IN 7%) Tax is:       ${z}
            -----------------------------------
               Your total is:       ${x}
            """)

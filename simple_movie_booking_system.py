import sys
import random

print("*WELCOME TO THE OFFICIAL WEBSITE OF <insert name> CINEMAS*")
print("Note that all information asked for booking seats are necessary and also that we stick with our privacy policy and terms of conditions")
print("Also note that all tickets will be sold only online in this website and the ticket(s) will only be an e-ticket(s) and thus make sure to bring it with you for entering")
name = input("Enter your name: ")
print("(Note that your e-ticket(s) will be sent to your mobile as a message so kindly double check)")
mob = input("Enter your mobile number: ")
while len(mob) != 10:
    print("INVALID NUMBER!!")
    mob = input("Enter your mobile number: ")
email = input("Enter your email:")
print("(Note that your e-ticket(s) will be sent to your email so kindly double check)")
age = int(input("Enter your age: "))
if age < 15:
    print("**YOU ARE NOT ELIGIBLE TO BOOK TICKETS**")
    sys.exit()
print('''MOVIES :
1 - <movie name 1>
2 - <movie name 2>
3 - <movie name 3>
4 - <movie name 4>''')
mov = int(input("Enter your choice of movie(1-4) : "))
while mov > 4 or mov < 1:
    print("INVALID OPTION")
    mov = int(input("Enter your choice of movie(1-4) : "))
m = ""
if mov == 1:
    m = "<movie name 1>"
elif mov == 2:
    m = "<movie name 2>"
elif mov == 3:
    m = "<movie name 3>"
else:
    m = "<movie name 4>"
if mov == 1:
    print("You have chosen the movie <movie name 1>.")
    date = input("Enter the date you will like to watch the movie(dd/mm/yyyy) : ")
    seats = int(input("Enter the number of tickets you want : "))
    tc = 0
    tc = 125 * seats
    print('''The timings available are :
1 - 9:00am to 12:00pm
2 - 12:20pm to 3:20pm
3 - 3:40pm to 6:40pm
4 - 7:00pm to 10:00pm''')
    t = int(input("Enter you choice of timings(1-4) : "))
    while t > 4 or t < 1:
        print("INVALID OPTION")
        t = int(input("Enter you choice of timings(1-4) : "))
    if t == 1:
        print("Movie : <movie name 1>")
        print("Date : ", date)
        print("Timings : 9:00")
        print("Number of Tickets : ", seats)
        print("Total Cost for the Tickets : ", tc)
    elif t == 2:
        print("Movie : <movie name 1>")
        print("Date : ", date)
        print("Timings : 12:20")
        print("Number of Tickets : ", seats)
        print("Total Cost for the Tickets : ", tc)
    elif t == 3:
        print("Movie : <movie name 1>")
        print("Date : ", date)
        print("Timings : 3:40")
        print("Number of Tickets : ", seats)
        print("Total Cost for the Tickets : ", tc)
    else:
        print("Movie : <movie name 1>")
        print("Date : ", date)
        print("Timings : 7:00")
        print("Number of Tickets : ", seats)
        print("Total Cost for the Tickets : ", tc)
elif mov == 2:
    print("You have chosen the movie <movie name 2>.")
    date = input("Enter the date you will like to watch the movie(dd/mm/yyyy) : ")
    seats = int(input("Enter the number of tickets you want : "))
    tc = 0
    tc = 125 * seats
    print('''The timings available are :
1 - 8:45am to 11:45am
2 - 12:05pm to 3:05pm
3 - 3:25pm to 6:25pm
4 - 6:45pm to 9:45pm''')
    t = int(input("Enter you choice of timings(1-4) : "))
    while t > 4 or t < 1:
        print("INVALID OPTION")
        t2 = int(input("Enter you choice of timings(1-4) : "))
    if t == 1:
        print("Movie : <movie name 2>")
        print("Date : ", date)
        print("Timings : 8:45")
        print("Number of Tickets : ", seats)
        print("Total Cost for the Tickets : ", tc)
    elif t == 2:
        print("Movie : <movie name 2>")
        print("Date : ", date)
        print("Timings : 12:05")
        print("Number of Tickets : ", seats)
        print("Total Cost for the Tickets : ", tc)
    elif t == 3:
        print("Movie -:<movie name 2>")
        print("Date : ", date)
        print("Timings : 3:25")
        print("Number of Tickets : ", seats)
        print("Total Cost for the Tickets : ", tc)
    else:
        print("Movie : <movie name 2>")
        print("Date : ", date)
        print("Timings : 6:45")
        print("Number of Tickets : ", seats)
        print("Total Cost for the Tickets : ", tc)
elif mov == 3:
    print("You have chosen the movie <movie name 3>.")
    date = input("Enter the date you will like to watch the movie(dd/mm/yyyy) : ")
    seats = int(input("Enter the number of tickets you want : "))
    tc = 0
    tc = 125 * seats
    print('''The timings available are :
1 - 9:15am to 12:15pm
2 - 12:35pm to 3:35pm
3 - 3:55pm to 6:55pm
4 - 7:15pm to 10:15pm''')
    t = int(input("Enter you choice of timings(1-4) : "))
    while t > 4 or t < 1:
        print("INVALID OPTION")
        t = int(input("Enter you choice of timings(1-4) : "))
    if t == 1:
        print("Movie : <movie name 3>")
        print("Date : ", date)
        print("Timings : 9:15")
        print("Number of Tickets : ", seats)
        print("Total Cost for the Tickets : ", tc)
    elif t == 2:
        print("Movie : <movie name 3>")
        print("Date : ", date)
        print("Timings : 12:35")
        print("Number of Tickets : ", seats)
        print("Total Cost for the Tickets : ", tc)
    elif t == 3:
        print("Movie : <movie name 3>")
        print("Date : ", date)
        print("Timings : 3:55")
        print("Number of Tickets : ", seats)
        print("Total Cost for the Tickets : ", tc)
    else:
        print("Movie : <movie name 3>")
        print("Date : ", date)
        print("Timings : 7:15")
        print("Number of Tickets : ", seats)
        print("Total Cost for the Tickets : ", tc)
else:
    print("You have chosen the movie <movie name 4>.")
    date = input("Enter the date you will like to watch the movie(dd/mm/yyyy) : ")
    seats = int(input("Enter the number of tickets you want : "))
    tc = 0
    tc = 125 * seats
    print('''The timings available are :
1 - 9:00am to 12:00pm
2 - 12:20pm to 3:20pm
3 - 3:40pm to 6:40pm
4 - 7:00pm to 10:00pm''')
    t = int(input("Enter you choice of timings(1-4) : "))
    while t > 4 or t < 1:
        print("INVALID OPTION")
        t = int(input("Enter you choice of timings(1-4) : "))
    if t == 1:
        print("Movie : <movie name 4>")
        print("Date : ", date)
        print("Timings : 9:00")
        print("Number of Tickets : ", seats)
        print("Total Cost for the Tickets : ", tc)
    elif t == 2:
        print("Movie : <movie name 4>")
        print("Date : ", date)
        print("Timings : 12:20")
        print("Number of Tickets : ", seats)
        print("Total Cost for the Tickets : ", tc)
    elif t == 3:
        print("Movie : <movie name 4>")
        print("Date : ", date)
        print("Timings : 3:40")
        print("Number of Tickets : ", seats)
        print("Total Cost for the Tickets : ", tc)
    else:
        print("Movie : <movie name 4>")
        print("Date : ", date)
        print("Timings : 7:00")
        print("Number of Tickets : ", seats)
        print("Total Cost for the Tickets : ", tc)

v = input("Do you want to buy food?(Yes/No) ")
if v == "Yes":
    Snacks = ['Popcorn', 'Nachos', 'Fries', 'Sandwich', 'Puffs', 'Salad']
    Drinks = ['Water', 'Coffee', 'Cold Coffee', 'Hot Chocolate', 'Tea', 'Coke', 'Pepsi', 'Sprite', 'Mountain Dew']
    Desserts = ['Ice cream', 'Cake', 'Donut', 'Waffles', 'Croissants']
    Food = [Snacks, Drinks, Desserts]
    choice = int(input('''Choose from the following :
1)Snacks
2)Beverages
3)Desserts
What is your choice? '''))
    while choice > 4 or choice < 1:
        print("INVALID CHOICE")
        choice = int(input('''Choose from the following :
1)Snacks
2)Beverages
3)Desserts
What is your choice?(1-3) '''))
    if choice == 1:
        print("These are the available Snacks : ", Snacks)
        a = input('''Now tell us what you want?
I want ''')
        f1 = []
        f1.append(a)
        ab = input("Do you want to buy anything else?(Yes/No) ")
        while ab == "Yes":
            print("These are the available Snacks : ", Snacks)
            b = input('''Now tell you what you want?
I want ''')
            f1.append(b)
            ab = input("Do you want to buy anything else?(Yes/No) ")
        total = len(f1)
        fc = total * 75
        print("Your Order :", f1)
        print("Total cost for Food : ", fc)
    elif choice == 2:
        print("These are the available Beverages : ", Drinks)
        a = input('''Now tell us what you want?
I want ''')
        f1 = []
        f1.append(a)
        ab = input("Do you want to buy anything else?(Yes/No) ")
        while ab == "Yes":
            print("These are the available Beverages : ", Drinks)
            b = input('''Now tell you what you want?
I want ''')
            f1.append(b)
            ab = input("Do you want to buy anything else?(Yes/No) ")
        print("Your Order :", f1)
        total = len(f1)
        fc = total * 25
        print("Total cost for Food : ", fc)
    else:
        print("These are the available Desserts : ", Desserts)
        a = input('''Now tell us what you want?
I want ''')
        f1 = []
        f1.append(a)
        ab = input("Do you want to buy anything else?(Yes/No) ")
        while ab == "Yes":
            print("These are the available Desserts : ", Desserts)
            b = input('''Now tell you what you want?
I want ''')
            f1.append(b)
            ab = input("Do you want to buy anything else?(Yes/No) ")
        print("Your Order :", f1)
        total = len(f1)
        fc = total * 85
        print("Total cost for Food : ", fc)
    cost = tc + fc
    print("NAME : ", name)
    print("MOBILE NUMBER : ", mob)
    print("EMAIL ADDRESS : ", email)
    print("MOVIE : ", m)
    print("NUMBBER OF TICKETS : ", seats)
    print("DATE : ", date)
    print("TIMINGS : ", t)
    print("COST FOR THE TICKETS : ₹", tc)
    print("FOOD ORDERED : ", f1)
    print("COST FOR THE FOOD : ₹", fc)
    print("TOTAL COST TO BE PAYED : ₹", cost)
    print("The amount is to be payed in person at PVS Cinemas before going inside the theatre ")
    file = open("Info.txt", "a")
    info = "Name : " + name + "\n" + "Mobile Number : " + str(
        mob) + "\n" + "Email Address : " + email + "\n" + "Movie you have chosen : " + m + "\n" + "Number of tickets : " + str(
        seats) + "\n" + "Date : " + str(date) + "\n" + "Timings : " + str(t) + "\n"
    file.writelines(info)
    file.close()
else:
    print("NAME : ", name)
    print("MOBILE NUMBER : ", mob)
    print("EMAIL ADDRESS : ", email)
    print("MOVIE : ", m)
    print("NUMBBER OF TICKETS : ", seats)
    print("DATE : ", date)
    print("TIMINGS : ", t)
    print("COST FOR THE TICKETS : ₹", tc)
    print("TOTAL COST TO BE PAYED : ₹", tc)
    print("The amount is to be payed in person at PVS Cinemas before going inside the theatre ")
    file = open("Info.txt", "w")
    info = "Name : " + name + "\n" + "Mobile Number : " + str(
        mob) + "\n" + "Email Address : " + email + "\n" + "Movie you have chosen : " + m + "\n" + "Number of tickets : " + str(
        seats) + "\n" + "Date : " + str(date) + "\n" + "Timings : " + str(t) + "\n"
    file.writelines(info)
    file.close()
food = ['Popcorn', 'Nachos', 'Fries', 'Sandwich', 'Puffs', 'Salad', 'Water', 'Coffee', 'Cold Coffee', 'Hot Chocolate',
        'Tea', 'Coke', 'Pepsi', 'Sprite', 'Mountain Dew', 'Ice cream', 'Cake', 'Donut', 'Waffles', 'Croissants']
print("We have a special offer of playing a game and winning a food item.")
import random

print('''Winning rules of the Rock Paper Scissors game as follow :
Rock vs Paper->PAPER WINS!!
Scissor vs Rock->ROCK WINS!! 
Paper vs Scissor->SCISSOR WINS!!
You are all ready to play the game.
LETS GOOOOO!!''')
o1 = int(input('''1)Rock
2)Paper
3)Scissor
Enter your choice :(1-3) '''))
while o1 > 3 or o1 < 1:
    print("INVALID OPTION")
    o1 = int(input('''1)Rock
2)Paper
3)Scissor
Enter your choice : '''))
if o1 == 1:
    ou = "Rock"
elif o1 == 2:
    ou = "Paper"
else:
    ou = "Scissor"
o2 = random.randint(1, 3)
while o1 == o2:
    o2 = random.randint(1, 3)
if o2 == 1:
    oc = "Rock"
elif o2 == 2:
    oc = "Paper"
else:
    oc = "Scissor"
print("Computer's choice :", oc)
print("Now it is ", ou, "vs", oc)
if ((o1 == 1 and o2 == 2) or (o2 == 1 and o1 == 2)):
    print("PAPER WINS!!")
    result = "Paper"
elif ((o1 == 1 and o2 == 3) or (o2 == 1 and o1 == 3)):
    print("ROCK WINS!!")
    result = "Rock"
else:
    print("SCISSOR WINS!!")
    result = "Scissor"
if result == ou:
    print("USER WINS")
    print("YOU GET A FREE FOOD")
    food = ['Popcorn', 'Nachos', 'Fries', 'Sandwich', 'Puffs', 'Salad', 'Water', 'Coffee', 'Cold Coffee',
            'Hot Chocolate', 'Tea', 'Coke', 'Pepsi', 'Sprite', 'Mountain Dew', 'Ice cream', 'Cake', 'Donut', 'Waffles',
            'Croissants']
    print("These are available food items : ", food)
    order = input("What do you want? ")
    print("So you get a free ", order)
else:
    print("BETTER LUCK NEXT TIME!")
print("THANK YOU FOR BOOKING IN <enter name> CINEMAS!!")
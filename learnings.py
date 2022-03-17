# Lets play a guess game
x = int(input("Please enter an integer:"))
y = int(input("Please enter another integer:"))
z = int(input("Please enter a third integer:"))
# Here is our initial guess
maxNum = x
if y > maxNum: # Fix our guess if needed
    maxNum = y
if z > maxNum: # Fix our guess again if needed
    maxNum = z
print(maxNum,"is greatest.")
print("Done.")




# determine if it's a perfect triangle
sideone = int(input("What's the first length?:"))
sidetwo = int(input("What's the second length?:"))
sidethree = int(input("What's the third length?:"))

sum = sideone**2 + sidetwo**2 + sidethree**2

if sum%2 != 0:
	print('It is not a perfect triangle')
else:
	print('It is lit!')
print('Done!')




# Mathematical operations on set of numbers
x = float(input("Please enter a number:"))
y = float(input("Please enter another number:"))

print("1) Add the two numbers")
print("2) Subtract the two numbers")
print("3) Multiply the two numbers")
print("4) Divide the two numbers")

choice = int(input("Select an option:"))

print("The answer is:", end=" ")

if choice == 1:
    print(x + y)
elif choice == 2:
    print(abs(x - y))
elif choice == 3:
    print(x * y)
elif choice == 4:
    print(x/y)
else:
    print("Your choice is not clear. Try again!")
    




#Open a file in directory in python.

catfile = open(input(), 'r')   # can be r, w, a = read, write, append
for line in catfile:
    print(line.rstrip())    # rstrip() removes extra line after each line
catfile.close()




# The first can also be
file = input("Please add name of the file:")
catfile = open(file, 'r')
for line in catfile:
    print(line.rstrip())
catfile.close()




# create a file and write to it
filename = input("Please name your file:")
yourname = input("What is your name?:")
age = int(input("How old are you?:"))
outfile = open(filename, "w")
outfile.write("Hello " + yourname + ". How are you doing today?\n")
outfile.write("Next year you are going to be " + str(age+1) + "years old")
outfile.close()





# turtle diagram
import turtle

t = turtle.Turtle()
screen = t.getscreen()
t.forward(25)
t.left(90)
t.forward(25)
t.left(90)
t.forward(25)
t.left(90)
t.forward(25)
screen.exitonclick()





# pentagon in python
from turtle import *

ff = float(input("Enter the number of forward movement: "))
lt = float(input("Enter the number of leftward movement: "))

t = Turtle()
screen = t.getscreen()
t.forward(ff)
t.left(lt)
t.forward(ff)
t.left(lt)
t.forward(ff)
t.left(lt)
t.forward(ff)
t.left(lt)
t.forward(ff)
screen.exitonclick()




#Explode some xters
def explode(s):
    lst = []
    for c in s:
        lst.append(c)
    return lst
print(explode('antimonophotogeographicationalism'))





def implode(lst):
    s = ' '
    for e in lst:
        s = s+e
    return s
print(implode(['a', 'n', 't', 'i', 'm', 'o', 'n', 'o', 'p', 'h', 'o', 't', 'o', 'g', 'e', 'o', 'g', 'r', 'a', 'p', 'h', 'i', 'c', 'a', 't', 'i', 'o', 'n', 'a', 'l', 'i', 's', 'm']))





### The following ar courtesy of 'The Python Workbook by Ben Stephenson'
## Introduction to Python Exercises 
# ask user to input name
name = input("What is your name amigos?:")
print ("Hello", name, ", Welcome to your PC")




# calculate area of a room
length = float(input("Enter the length of the room (in metres): "))
width = float(input("Enter the width of the room (in meters): "))
print("The room is", length, "metres long", "and", width, "metres wide")
Area = length * width 
Area = round(Area, 2)
print("Area of the room is", Area, "sq. metres")




# The area of a farm in acres
length = float(input("What is the length of the farm (in feet): "))
width = float(input("What is the widthth of the farm (in feet): "))
area = length*width
acre = round((43560/area), 2)  # 1acre is 43560sq.ft
print("Your farm is", acre, "acres of land")




# calculate the amount of refund to give container returners
con = int(input("How many drink containers do you have?: "))
litres = float(input("How many litres are they each?: "))

if litres <= 1.0:
    refund = round((con*0.10), 2)
    print("You will receive a refund of ", "$" + str(refund))
elif litres > 1.0:
    refund = round((con*0.25), 2)
    print("You will receive a refund of", "$" + str(refund))
print("Do have a wonderful day ahead")





# situation where some containers are a mixture of <1L and >1L
lone = int(input("How many containers are 1L or less?: "))
mone = int(input("How many containers are more than 1L?: "))

refund1 = round((lone*0.10), 2)
refund2 = round((mone*0.25), 2)
total_refund = refund1 + refund2 

print("You will receive a total refund of", "$" + str(total_refund))

print("Do have a wonderful day ahead")





# Calculate the tax and tip in a hotel situation 
meal = float(input("Please enter the cost of your meal: "))
tax = (7.5/100)*meal 
tip = (18/100)*meal 
print("Your meal cost =", "$" + str(meal))
print("The tax amount =", "$" + str(tax))
print("The tip amount =", "$" + str(tip))
print("The grand total for the meal = $%.2f." % (meal + tax + tip))

# Alternate formatting for the print statement
# total = meal + tax + tip
# print("The meal is %.2f with a tax of %.2f and the tip %.2f, making the total %.2f" % \
# (meal, tax, tip, total)
# the \ at the end of the line is called the continuation xter. It tells Python that the statement
# continues on the next line. Do not add any spaces or tab after the \character.






# Change height from ft.in to cm
# 1ft = 12 inches
# 1inch = 2.54 cm

ft = int(input("Please add your height in feet: "))
inches = int(input("Please add your height in inches: "))

ft_in = ft*12
n_in = inches + ft_in

ht_cm = n_in * 2.54

print("Your height %.2f feet and %.2f inches is equivalent to %.2f centimeters" % (ft, inches, ht_cm))





# Calc area of a circle
from math import *
radius = float(input("Add the radius of the circle: "))
area = pi * radius**2
print(area)





#Calculate BMI in kg and metres
weight = float(input("Add your weight (in kg): "))
height = float(input("Add your height (in metres): "))

BMI = weight / height**2 

print("Your BMI is %d" %BMI)






#Calculate BMI in pounds and inches
weight = float(input("Add your weight (in pounds): "))
height = float(input("Add your height (in inches): "))

BMI = (weight / height**2) * 703

print("Your BMI is %d" %BMI)






## If statement Exercises begin

# Check if a number is even or odd
oya = int(input("Do add a number: "))
if oya%2 == 0:
    print(oya, "is an even number")
else:
    print(oya, "is an odd number")






# Converting from human years to dog years
human = 10.5
human1 = 4
age = float(input("How old are you?: "))

if age <= 2:
    print("You are", human*age, "dog years")

elif age > 2:
    age1 = age - 2
    new_age = age1 * 4 + human * 2
    print("You are", new_age, "dog years old")
print("That was quite fun!")






# Indicate whether a letter is a Vowel or Consonant
vowels = ['a', 'e', 'i', 'o', 'u']
alphabet = str(input("Enter an alphabet: "))
alphabet = alphabet.lower()

if alphabet in vowels:
    print(alphabet, "is a vowel")
elif alphabet == "y":
    print(alphabet, "is a consonant but can sometimes be a vowel")
else:
    print(alphabet, "is a consonant")






# Determine the name of a shape from the number of sides
sides = int(input("How many sides has the shape?: "))
if sides < 3:
    print("Sorry, that is an invalid shape")
elif sides == 3:
    print("The shape is a Triangle")
elif sides == 4:
    print("The shape is a Quadilateral")
elif sides == 5:
    print("The shape is a Pentagon")
elif sides == 6:
    print("The shape is a Hexagon")
elif sides == 7:
    print("The shape is a Heptagon")
elif sides == 8:
    print("The shape is a Octagon")
elif sides == 9:
    print("The shape is a Nonagon")
elif sides == 10:
    print("The shape is a Decagon")
else:
    print("The shape is out of range")






# Doing the shape above using Guess and Check pattern

sides = int(input("Enter the number of sides: "))

# Set an empty string value for the name variable

name = " "
if sides == 3:
    name = "Triangle"
elif sides == 4:
    name = "Quadilateral"
... until 10.

#Display an error for values not within the above (3 to 10)

if name == " ":
    print("That number of sides is not supported by this program")
else:
    print("That's a", name)







# Read the name of a month and display the number of days in it
first = ["April", "June", "September", "November"]
second = ["January", "March", "May", "July", "August", "October", "December"]
month = str(input("Enter the name of the month: ")).capitalize()
year = int(input("What year is that?: "))

if month in first:
    print(f"There are 30 days in {month} of {year}")
elif month == "February" and year%4 != 0:
    print("In the year", year, "there are 28 days in", month)
elif month == "February" and year%4 == 0:
    print("In the year", year, "there are 29 days in", month)
elif month in second:
    print(f"There are 31 days in {month} of {year}")
else:
    print("Please check your inputs and try again!")


## modify this later to start the sequence again after displaying results. That is using a while loop.







# Who is on the face of Nigerian currency?
denom = int(input("Enter the denomination in Naira (0 for 50kobo): "))

zero = "Corn Cob"
one = "Herbert Macaulay"
two = "National Assembly"
five = "Tafawa Balewa"
ten = "Alvan Ikoku"
twenty = "Murtala Muhhamed"
fifty = "WAZOBIA"
hundred = "Obafemi Awolowo"
two_hundred = "Ahmadu Bello"
five_hundred = "Nnamdi Azikiwe"
one_thousand = "Aliyu Mai-Borno & Clement Isong"

individual = " "

if denom == 0:
    individual = zero
elif denom == 1:
        individual = one
elif denom == 2:
        individual = two
elif denom == 5:
        individual = five
elif denom == 10:
        individual = ten
elif denom == 20:
        individual = twenty
elif denom == 50:
        individual = fifty
elif denom == 100:
        individual = hundred
elif denom == 200:
        individual = two_hundred
elif denom == 500:
        individual = five_hundred
elif denom == 1000:
        individual = one_thousand
else:
    individual = " "

if individual == " ":
    print("No such denomination")
else:
    print("The individual that appears on", "₦" + str(denom), "is", individual)






# National holidays in Canada
month = str(input("Enter the month: ").capitalize())
day = int(input("Enter the day: "))

date = " "
if day == 1:
    date = "1st"
elif day == 2:
    date = "2nd"
elif day == 3:
    date = "3rd"
else:
    date = day + "th"

holiday = " "
if month == "January" and day == 1:
    holiday = "New Year's day"
elif month == "July" and day == 1:
    holiday = "Canada Day"
elif month == "December" and day == 25:
    holiday = "Christmas Day"

if holiday == " ":
    print("Sorry! There is no fixed holiday for", date, "of", month)
else:
    print("On this day the", date, "of", month + ",", "Canada is observing", holiday)







# What colour is a square on a board game?
print("This algo draws from bottom up and left to right.")
card = input("Enter position (e.g. C4): ")
letter = card[0].upper()
num = int(card[-1])

if num%2 == 0:
    print("The row begins with a white square")
else:
    print("The row begins with a black square")

black = ["A", "C", "E", "G"]
if letter in black:
    print("The column starts with a black square")
else:
    print("The column begins with a white square")
    
if letter in black and num%2 != 0:
    print("The square in this position is black")
else:
    print("The square in this position is white")

## To-Do: Add validation line so letters (A-H) and num(1-8)









# Tell the season of the year by the month and day

spring = ["March", "April", "May", "June"]
summer = ["June", "July", "August", "September"]
fall = ["September", "October", "November", "December"]
winter = ["December", "January", "February", "March"]

month = str(input("Enter the month you wish to check: ")).capitalize()
day = int(input("What day is it?: "))

if month in spring:
    if month == "March" and day > 19:
        print("The day", day, month, "is Spring")
    elif month == "June" and day < 19 and day != 0:
        print("The day", day, month, "is Spring")
    elif month == "May" or month == "April": 
        print("The day", day, month, "is Spring")
        
if month in summer:
    if month == "June" and day > 20:
        print("The day", day, month, "is Summer")
    elif month == "September" and day < 22 and day != 0:
        print("The day", day, month, "is Summer")
    elif month == "July" or month == "August": 
        print("The day", day, month, "is Summer")
        
if month in fall:
    if month == "September" and day > 21:
        print("The day", day, month, "is Fall")
    elif month == "December" and day < 21 and day != 0:
        print("The day", day, month, "is Fall")
    elif month == "October" or month == "November": 
        print("The day", day, month, "is Fall")
        
if month in winter:
    if month == "December" and day > 20:
        print("The day", day, month, "is Winter")
    elif month == "March" and day < 20 and day != 0:
        print("The day", day, month, "is Winter")
    elif month == "January" or month == "February": 
        print("The day", day, month, "is Winter")
print("Tres bien Mon Ami")


# modify above
if month == "December" and day > 20:
    season = "Winter"
    
# At the end
print("The day", day, month, "is, season)







# Horoscope

taurus = "About you: My Queen and my Mother, before Your throne of mercy, \
I come for help and intercession. I beg for mercy and healing touch upon me \
and those that are sick, especially those that are terminally ill. \
Mother of mercy present all those that are sick before your Son; our lord Jesus Christ, \
who is the greatest physician; for miraculous cure and wholeness. \
Uproot every infirmity in our lives and grant us divine healing."

pisces = "Properties: My Queen and my Mother, before Your throne of mercy, \
I come for help and intercession. I beg for mercy and healing touch upon me \
and those that are sick, especially those that are terminally ill. \
Mother of mercy present all those that are sick before your Son; our lord Jesus Christ, \
who is the greatest physician; for miraculous cure and wholeness. \
Uproot every infirmity in our lives and grant us divine healing."

month = str(input("Enter your month of birth: ")).capitalize()
day = int(input("Enter your day of birth: "))

if month == "December" and day >= 22:
    sign = "Capricon"
    about = pisces
elif month == "January"and day < 20:
    sign = "Capricon"
    about = pisces
elif month == "January" and day >= 20:
    sign = "Aquarius"
    about = pisces
elif month == "February"and day < 19:
    sign = "Aquarius"
    about = pisces
elif month == "February" and day > 18:
    sign = "Pisces"
    about = pisces
elif month == "March"and day <= 20:
    sign = "Pisces"
    about = pisces
elif month == "March" and day > 20:
    sign = "Aries"
    about = pisces
elif month == "April"and day < 20:
    sign = "Aries"
    about = pisces
elif month == "April" and day >= 20:
    sign = "Taurus"
    about = taurus
elif month == "May" and day < 21:
    sign = "Taurus"
    about = taurus
elif month == "May" and day >= 21:
    sign = "Gemini"
    about = pisces
elif month == "June"and day < 21:
    sign = "Gemini"
    about = pisces
elif month == "June" and day >= 21:
    sign = "Cancer"
    about = pisces
elif month == "July"and day < 23:
    sign = "Cancer"
    about = pisces
elif month == "July" and day >= 23:
    sign = "Loe"
    about = pisces
elif month == "August"and day < 23:
    sign = "Leo"
    about = pisces
elif month == "August" and day >= 23:
    sign = "Virgo"
    about = pisces
elif month == "September"and day < 23:
    sign = "Virgo"
    about = pisces
elif month == "September" and day >= 23:
    sign = "Libra"
    about = pisces
elif month == "October"and day < 23:
    sign = "Libra"
    about = pisces
elif month == "October" and day >= 23:
    sign = "Scorpio"
    about = pisces
elif month == "November"and day < 22:
    sign = "Scorpio"
    about = pisces
elif month == "November" and day >= 22:
    sign = "Capricon"
    about = pisces
elif month == "December"and day < 22:
    sign = "Capricon"
    about = pisces
else:
    print("Check your input")
print("")
print("You were born on", day, month, "and your Zodiac sign is", sign)
print("")
print(about)









# Earthquake magnitude ranges on the Richter scale and their descriptions

mag = float(input("Enter the magnitude: "))

if mag < 2.0:
    desc = "Micro"
elif mag == 2.0 and mag < 3.0:
    desc = "Very minor"
elif mag == 3.0 and mag < 4.0:
    desc = "Minor"
elif mag == 4.0 and mag < 5.0:
    desc = "Light"
elif mag == 5.0 and mag < 6.0:
    desc = "Moderate"
elif mag == 6.0 and mag < 7.0:
    desc = "Strong"
elif mag == 7.0 and mag < 8.0:
    desc = "Major"
elif mag == 8.0 and mag < 10.0:
    desc = "Great"
else:
    desc = "Meteoric"

print("The earthquake of magnitude", mag, "is a", desc, "Earthquake")







# Assessing employers for salary raise

rating = float(input("What is your rating?: "))
r = 2400
amount = r * rating 

if rating == 0.0:
    meaning = "Unacceptable"
elif rating == 0.4:
    meaning = "Acceptable"
else:
    meaning = "Meritorous"
print("Your overall rating is", rating, "which is", meaning, "Your raise is", "$" + str(amount))







# Cell phone bill with cost for additional plan
num_mins = float(input("Enter the number of minutes for the month: "))
num_txt = int(input("Enter the number of text messages for the month: "))

additional_cc = (num_mins - 50) * 0.25
additional_txt = (num_txt - 50) * 0.15
call_center = 0.44

base_charge = "Your base charge: $15.00"   #"$15 for 50 minutes of airtime and 50 text messages per month"
#add_cc = "Additional call charges", "$" + str(additional_cc)
#add_sms = "Additional SMS charges", "$" + str(additional_txt)

if num_mins <= 50 and num_txt <= 50:
    total_cost = 15 + call_center
    print(base_charge)

elif num_mins <= 50 and num_txt > 50:
    total_cost = 15 + additional_txt + call_center
    print(base_charge)
    print("Additional SMS charges: $%.2f" %additional_txt)

elif num_mins > 50 and num_txt <= 50:
    total_cost = 15 + additional_cc + call_center
    print(base_charge)
    print("Additional call charges: $%.2f" %additional_cc)
    
else:
    total_cost = 15 + additional_cc + additional_txt + call_center
    print(base_charge)
    print("Additional call charges: $%.2f" %additional_cc)
    print("Additional SMS charges: $%.2f" %additional_txt)

tax = 0.05 * total_cost
grand_total = total_cost + tax

print("Charge for 911 calls: $0.44")
print("Tax to be paid: $%.2f" %tax)
print("This month's bill is $%.2f inclusive of tax" %grand_total)








## Now Let's loop like a native


count = 0
print("Starting...")
while count < 10:
    print(count, " ", end=" ")
    count += 1
print()
print("Done")






# Performing the above using for loop
count = 0     # a) not a must in for loop
print("Starting...")
for i in range(0, 10):
    print(count, " ", end=" ")    # if a) above is true, count becomes i (where i is the starting point)
    count += 1
print()
print("Done")







#typically for loop of the above. Conscise and clear.
print('Print out values in a range')
for i in range(0, 10):
    print(i, ' ', end='')
print()
print('Done')






# The anonymous loop variable
for _ in range(0, 10):
    print(".", end=" ")
print()
# What the _ above does is to ignore the starting point.
# The loop then prints the xter (.) ten times.



print('Only print code if all iterations completed')
num = int(input('Enter a number to check for: '))
for i in range(0, 6):
    if i == num:
        break
    print(i, ' ', end='')
print('Done')






# Dice rolling
import random
MIN = 1
MAX = 6
roll_again = 'y'
while roll_again == 'y':
    print('Rolling the dices...')
    print('The values are....')
    dice1 = random.randint(MIN, MAX)
    print(dice1)
    dice2 = random.randint(MIN, MAX)
    print(dice2)
    roll_again = input('Roll the dices again? (y / n): ')







# The shorthand if statement (if expression)

age = int(input("Enter your age: "))

status = ('teenager' if age > 12 and age < 20 else 'not teenager')
print(status)


# The above is a shorthand for the below code

age = int(input("Enter your age: "))

status = None

if (age > 12) and age < 20:
    status = 'teenager'
else:
    status = 'not teenager'
print(status)






# The guess game 

import random 

print('Welcome to the number guess game')

# Initialise the number to be guessed
number_to_guess = random.randint(1,10)

# Initialise the number of tries the player has made
count_number_of_tries = 1

# Obtain their initial guess
guess = int(input('Please guess a number between 1 and 10: '))
while number_to_guess != guess:
    print('Sorry wrong number')
    # Check to see they have not exceeded the maximum
    # number of attempts if so break out of loop otherwise
    # give the user come feedback
    if count_number_of_tries == 4:
        break
    elif guess < number_to_guess:
        print('Your guess was lower than the number')
    else:
        print('Your guess was higher than the number')
    
    # Obtain their next guess and increment number of attempts
    guess = int(input('Please guess again: '))
    count_number_of_tries += 1
    
# Check to see if they did guess the correct number
if number_to_guess == guess:
    print('Well done you won!')
    print('You took', count_number_of_tries , 'guess to complete the game')
else:
    print("Sorry - you loose")
    print('The number you needed to guess was', number_to_guess)

# Allow them continue playing (haven't worked out yet)
loose = input("Do you want to play again? (y/n): ") 

if loose == y:
    guess = int(input('Please guess a number between 1 and 10: '))
else:
    print('Game Over')


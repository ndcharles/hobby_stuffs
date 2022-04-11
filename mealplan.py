#Complete this meal plan
#Reference: https://www.ag.ndsu.edu/publications/food-nutrition/myplate-plans-for-adults

print("Let's help you plan your meals so you can live healthy")
gender = input("What is your gender(MALE or FEMALE): ").lower() #reduce gender input to lowercase
get_age = int(input("How old are you?: ")) #Age should be rounded to nearest ten(10, 20, 30, 40, 50, 60, 70, 80)
age = round(get_age, -1) #Round age to the nearest tens on input.

#Keep activity level between 1 and 60
activity_level = 0
while activity_level <= 0 or activity_level > 60:
	try:
		activity_level = int(input("What's your activity level in minutes(maximum is 60): "))
		if activity_level not in range(1, 61):
			raise ValueError		
	
	except ValueError:
		print("Check your inputs again")
		print("Activity Level is between 0 to 60 minutes")

#Given that the age is to the nearest ten.
#On input, round age to the nearest 10

'''
#filter out underage
get_age = []

for age in range(1, 81):
	age = int(input("How old are you?: "))
	if age < 15:
		print("Sorry! Age range not considered. Try again when you are older!")
	else:
		#age.round()
		get_age.append(i)
print("get_age") #test the output.


#Assume age has to be validated
#This validation code is now deprecated.

if age < 18:
	print("Sorry! Age range not considered. Try again when you are older!")

for age in range (18, 26):
	if gender == male:
		if activity_level < 30:
			grain = 9 ounces
			vege = 3.5 cups
			fruits = 2 cups
			dairy = 3 cups 
			protein = 6.5 ounces
			
		elif activity_level > 30 and activity_level < 60:
			grain = 10 ounces
			vege = 3.5 cups
			fruits = 2.5 cups
			dairy = 3 cups 
			protein = 7 ounces
	
		else:
			print("Check your inputs again")
			print("Activity Level is between 0 to 60 minutes")

	elif gender == female:
		if activity_level < 30:
			grain = 6 ounces
			vege = 2.5 cups
			fruits = 2 cups
			dairy = 3 cups 
			protein = 5.5 ounces
			
		elif activity_level > 30 and activity_level < 60:
			grain = 7 ounces
			vege = 3 cups
			fruits = 2 cups
			dairy = 3 cups 
			protein = 6 ounces
		
		else:
			print("Check your inputs again")
			print("Activity Level is between 0 to 60 minutes")
'''


# For age 20
if gender == 'male' and age == 20:
	if activity_level < 30:
		grain = '9 ounces'
		vege = '3.5 cups'
		fruits = '2 cups'
		dairy = '3 cups' 
		protein = '6.5 ounces'
		
	elif activity_level > 30 and activity_level <= 60:
		grain = '10 ounces'
		vege = '3.5 cups'
		fruits = '2.5 cups'
		dairy = '3 cups' 
		protein = '7 ounces'


elif gender == 'female' and age == 20:
	if activity_level < 30:
		grain = '6 ounces'
		vege = '2.5 cups'
		fruits = '2 cups'
		dairy = '3 cups' 
		protein = '5.5 ounces'
		
	elif activity_level > 30 and activity_level <= 60:
		grain = '7 ounces'
		vege = '3 cups'
		fruits = '2 cups'
		dairy = '3 cups' 
		protein = '6 ounces'


# For age 30
elif gender == 'male' and age == 30:
	if activity_level < 30:
		grain = '8 ounces'
		vege = '3 cups'
		fruits = '2 cups'
		dairy = '3 cups' 
		protein = '6.5 ounces'
		
	elif activity_level > 30 and activity_level <= 60:
		grain = '10 ounces'
		vege = '3.5 cups'
		fruits = '2.5 cups'
		dairy = '3 cups' 
		protein = '7 ounces'
	

elif gender == 'female' and age == 30:
	if activity_level < 30:
		grain = '6 ounces'
		vege = '2.5 cups'
		fruits = '1.5 cups'
		dairy = '3 cups' 
		protein = '5 ounces'
		
	elif activity_level > 30 and activity_level <= 60:
		grain = '6 ounces'
		vege = '2.5 cups'
		fruits = '2 cups'
		dairy = '3 cups' 
		protein = '5.5 ounces'
	


#for age 40
elif gender == 'male' and age == 40:
	if activity_level < 30:
		grain = '8 ounces'
		vege = '3 cups'
		fruits = '2 cups'
		dairy = '3 cups' 
		protein = '6.5 ounces'
		
	elif activity_level > 30 and activity_level <= 60:
		grain = '9 ounces'
		vege = '3.5 cups'
		fruits = '2 cups'
		dairy = '3 cups' 
		protein = '6.5 ounces'
	


elif gender == 'female' and age == 40:
	if activity_level < 30:
		grain = '6 ounces'
		vege = '2.5 cups'
		fruits = '1.5 cups'
		dairy = '3 cups' 
		protein = '5 ounces'
		
	elif activity_level > 30 and activity_level <= 60:
		grain = '6 ounces'
		vege = '2.5 cups'
		fruits = '2 cups'
		dairy = '3 cups' 
		protein = '5.5 ounces'


#for age 50
elif gender == 'male' and age == 50:
	if activity_level < 30:
		grain = '7 ounces'
		vege = '3 cups'
		fruits = '2 cups'
		dairy = '3 cups' 
		protein = '6 ounces'
		
	elif activity_level > 30 and activity_level <= 60:
		grain = '9 ounces'
		vege = '3.5 cups'
		fruits = '2 cups'
		dairy = '3 cups' 
		protein = '6.5 ounces'
	

elif gender == 'female' and age == 50:
	if activity_level < 30:
		grain = '6 ounces'
		vege = '2.5 cups'
		fruits = '1.5 cups'
		dairy = '3 cups' 
		protein = '5 ounces'
		
	elif activity_level > 30 and activity_level <= 60:
		grain = '6 ounces'
		vege = '2.5 cups'
		fruits = '2 cups'
		dairy = '3 cups' 
		protein = '5.5 ounces'


#for age 60
elif gender == 'male' and age == 60:
	if activity_level < 30:
		grain = '7 ounces'
		vege = '3 cups'
		fruits = '2 cups'
		dairy = '3 cups' 
		protein = '6 ounces'
		
	elif activity_level > 30 and activity_level <= 60:
		grain = '8 ounces'
		vege = '3 cups'
		fruits = '2 cups'
		dairy = '3 cups' 
		protein = '6.5 ounces'
	

elif gender == 'female' and age == 60:
	if activity_level < 30:
		grain = '5 ounces'
		vege = '2 cups'
		fruits = '1.5 cups'
		dairy = '3 cups' 
		protein = '5 ounces'
		
	elif activity_level > 30 and activity_level <= 60:
		grain = '6 ounces'
		vege = '2.5 cups'
		fruits = '1.5 cups'
		dairy = '3 cups' 
		protein = '5 ounces'
	

#for age 70
elif gender == 'male' and age == 70:
	if activity_level < 30:
		grain = '6 ounces'
		vege = '2.5 cups'
		fruits = '2 cups'
		dairy = '3 cups' 
		protein = '5.5 ounces'
		
	elif activity_level > 30 and activity_level <= 60:
		grain = '8 ounces'
		vege = '3 cups'
		fruits = '2 cups'
		dairy = '3 cups' 
		protein = '6.5 ounces'


elif gender == 'female' and age == 70:
	if activity_level < 30:
		grain = '5 ounces'
		vege = '2 cups'
		fruits = '1.5 cups'
		dairy = '3 cups' 
		protein = '5 ounces'
		
	elif activity_level > 30 and activity_level <= 60:
		grain = '6 ounces'
		vege = '2.5 cups'
		fruits = '1.5 cups'
		dairy = '3 cups' 
		protein = '5 ounces'

#for age 80
elif gender == 'male' and age == 80:
	if activity_level < 30:
		grain = '6 ounces'
		vege = '2.5 cups'
		fruits = '2 cups'
		dairy = '3 cups' 
		protein = '5.5 ounces'
		
	elif activity_level > 30 and activity_level <= 60:
		grain = '7 ounces'
		vege = '3 cups'
		fruits = '2 cups'
		dairy = '3 cups' 
		protein = '6 ounces'

elif gender == 'female' and age == 80:
	if activity_level < 30:
		grain = '5 ounces'
		vege = '2 cups'
		fruits = '1.5 cups'
		dairy = '3 cups' 
		protein = '5 ounces'
		
	elif activity_level > 30 and activity_level <= 60:
		grain = '6 ounces'
		vege = '2.5 cups'
		fruits = '1.5 cups'
		dairy = '3 cups' 
		protein = '5 ounces'
	
#filter ages less than 15 and beyond 84
if age < 15:
	print("Sorry! Age range not considered. Try again when you are older!")
	
elif age >= 90:
	print("We really need to celebrate you for attaining this age.")
	print("However, we never expected someone of such age on here.")	
	
else:
	print("As a", gender.upper(), "of", get_age, "years old with an activity level of about",
		  activity_level, "minutes, your meal plan consists of:\n", grain, "of Grain,\n", vege, "of Vegetables,\n", 
		  fruits, "of Fruits,\n", dairy, "of Dairy, and\n", protein, "of Protein.")
# \n is to add a line break. It should come before the ending apostrophe. 
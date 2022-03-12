'''
The idea here is to create a program that generates food for you based on what you have in your refrigerator. 
* input the foods you have; separated by comma.
* the foods should be able to be eaten singly
* example inputs: jollof rice, eba and egusi, eba and vegetable, spaghetti, rice and stew, yam porridge
* the program will give you a randomly generated food option 


import random 
food_available = input("Add the food in your fridge separated by comma: ").lower()
food = food_available.split(",")
rec_food = random.choice(food)
print(f"You won't go wrong with a plate of{rec_food} today.\nDo have a wonderful day ahead.")

'''



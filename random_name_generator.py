# Random name generator for your child
# Still hving little issues packaing it into a function

import random 

# add names from file
female_names = ["Adaobi", "Adaugo", "Adaku", "Chinaza", "Ugonnia", "Obianma", "Obianuju"]
male_names = ["Obinna", "Igbanude", "Emeka", "Ndubuisi", "Ezejiofor"]
unisex_names = ["Somkenechukwu", "Somtoochukwu", "Sochima", "Uche", "Ogochukwu"]

#Gender is either 1, 2 or 3 (male_names, female_names or unisex_names)
select_gender = int(input("Select gender of choice [male, female or unisex] :"))

name_list = []

# Select the gender of your child
if select_gender == 1:
    name = male_names
    gender = "Male"
elif select_gender == 2:
    name = female_names
    gender = "Female"
elif select_gender == 3:
    name = unisex_names
    gender = "dear"
else: 
    print("Please enter:\n1 for male\n2 for female or \n3 for Unisex")

# Convert names to list and append to empty list above
for n in name:
    name_list.append(n.strip())

# Now generate the names
rec_name = random.choice(name_list)
print(f"You won't go wrong with {rec_name} for your {gender} child.\nDo have a wonderful naming.")




#Khamal created the function 
def NameGenerator(f_name = female_names, m_name = male_names, u_name = unisex_names):
  #Gender is either 1, 2 or 3 (male_names, female_names or unisex_names)
  select_gender = int(input("Select gender of choice [male, female or unisex] :"))

  if select_gender == 1:
    name = random.choice(m_name)
    gender = "Male"
  elif select_gender == 2:
    name = random.choice(f_name)
    gender = "Female"
  elif select_gender == 3:
    name = random.choice(u_name)
    gender = "dear"
  else: 
    print("Please enter:\n1 for male\n2 for female or \n3 for Unisex")

  return f"You won't go wrong with {name} for your {gender} child.\nDo have a wonderful naming."





#Putting it all into one compact file.

import random 

# add names from file
female_names = ["Adaobi", "Adaugo", "Adaku", "Chinaza", "Ugonnia", "Obianma", "Obianuju"]
male_names = ["Obinna", "Igbanude", "Emeka", "Ndubuisi", "Ezejiofor"]
unisex_names = ["Somkenechukwu", "Somtoochukwu", "Sochima", "Uche", "Ogochukwu"]

def NameGenerator(f_name = female_names, m_name = male_names, u_name = unisex_names):
  #Gender is either 1, 2 or 3 (male_names, female_names or unisex_names)
  select_gender = int(input("Select gender of choice [male, female or unisex] :"))

  if select_gender == 1:
    name = random.choice(m_name)
    gender = "Male"
  elif select_gender == 2:
    name = random.choice(f_name)
    gender = "Female"
  elif select_gender == 3:
    name = random.choice(u_name)
    gender = "dear"
  else: 
    print("Please enter:\n1 for male\n2 for female or \n3 for Unisex")

  return f"You won't go wrong with {name} for your {gender} child.\nDo have a wonderful naming."
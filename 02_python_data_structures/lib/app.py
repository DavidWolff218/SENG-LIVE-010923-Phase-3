# Sequence Types
    
# Note: use print() to execute the examples. Comment out examples as needed to keep your Terminal
# output clean.

# Creating Lists
# mutable
#1. ✅ Create a list of 10 pet names
pet_names = ['Rose', 'Meow Meow Beans', 'Mr.Legumes', 'Luke', 'Lea', 'Princess Grace', 'Spot', 'Tom', 'Mini', 'Paul']

# Reading Information From Lists
#2. ✅ Return the first pet name
# print(pet_names[0])


#3. ✅ Return all pet names beginning from the 3rd index
# print(pet_names[3:])

#4. ✅ Return all pet names before the 3rd index
# print(pet_names[:3])

#5. ✅ Return all pet names beginning from the 3rd index and up to the 7th
# print(pet_names[3:7])

#6. ✅ Find the index of a given element => .index()
# first one found
# print(pet_names.index('Paul'))

#7. ✅ Reverse the original list => .reverse()
# print(pet_names.reverse())
# print(pet_names)

#8. ✅ Return the frequency of a given element => .count()
# print(pet_names.count("Rose"))

# Updating Lists
#9. ✅ Change the first name to all uppercase letters => .upper()

# pet_names[0] = pet_names[0].upper()
# print(pet_names)

#10. ✅ Append a new name to the list => .append()
# pet_names.append("Bud")
# print(pet_names)

#11. ✅ Add a new name at a specific index => .insert()
# arg1 - > index
# pet_names.insert(1, "Bud")
# print(pet_names)

#12. ✅ Add two lists together => +

# new_pet_list = pet_names + ["Champ", "Bud"]
# print(new_pet_list)

#13. ✅ Remove the final element from the list => .pop()


#14. ✅ Remove element by specific index => .pop()


#15. ✅ Remove a specific element => .remove()


#16. ✅ Remove all pet names from the list => .clear()

#Tuple
# 📚 Review:
    # Mutable, Immutable <=> Changeable, Unchangeable

#17. ✅ Create a Tuple of 10 pet ages => () 


#18. ✅ Print the first pet age => []


# Testing Mutability 
#19. ✅ Attempt to remove an element with ".pop" (should error)


#20. ✅ Attempt to change the first element (should error) => []


# Tuple Methods
#21. ✅ Return the frequency of a given element => .count()


#22. ✅ Return the index of a given element  => .index()


#23. ✅ Create a Range 
# Note:  Ranges are primarily used in loops


# Sets (Stretch Goal)
#24. ✅ Create a set of 3 pet foods
pet_fav_food = {'house plants', 'fish', 'bacon'}

# Dictionaries 
# Creating 
#25. ✅  Create a dictionary of pet information with the keys "name", "age" and "breed"
pet_info_rose = {'name':'Rose', 'age':11, 'breed':'domestic long'}
print(pet_info_rose['name'])

#26. ✅  Use dict to create a dictionary of pet information with the keys "name", "age" and "breed" => dict(...)
pet_info_spot = dict(name='Spot', age=25, breed='boxer')

# Reading
#27. ✅ Print the pet attribute of "name" using bracket notation 
# print(pet_info_rose['temperament'])

#28. ✅ Print the pet attribute of "age" using ".get"

    # Note: ".get" is preferred over bracket notation in most cases 
    # because it will return "None" instead of an error


# Updating 
#29. ✅ Update Rose's age to 12 => []


#30. ✅ Update Spot's age to 26 => .update({...})


# Deleting
#31. ✅ Delete Rose's age using the "del" keyword => []


#32. ✅ Delete Spot's age using ".pop"


#33. ✅ Delete the last item for Rose using "popitem()"


# Loops 
pet_info = [
    {
        'name':'Rose',
        'age':11,
        'breed': 'domestic long-haired',
    }, 
    {
        'name':'Spot',
        'age':25,
        'breed': 'boxer',
    },
    {
        'name':'Meow Meow Beans',
        'age':2,
        'breed': 'domestic long-haired',
    }
]

#34. ✅ Loop through a range of 10 and print every number within the range


#35. ✅ Loop through a range between 50 and 60 that iterates by 2 and print every number


#36. ✅ Loop through the "pet_info" list and print every dictionary 


#37. ✅ Create a function that takes a list a parameter 
    # The function should use a "for" loop to loop through the list and print each item 
    # Invoke the function and pass it "pet_names" as an argument


#38. ✅ Create a function that takes a list as a parameter
    # The function should define a counter and set it to 0
    # Create a "while" loop 
        # The loop will continue as long as the counter is less than the length of the list
        # Every loop should increase the count by 1
    # Return the counter 
    
def demo_while(list):
    counter = 0
    while(counter < len(list) - 1):
         counter += 1
    return counter   

# print(demo_while(pet_names))


#39. ✅ Create a function that updates the age of a given pet
        # The function should take a list of "dictionaries", "name" and "age" as parameters 
        # Create an index variable and set it to 0
        # Create a while loop 
            # The loop will continue so long as the list does not contain a name matching the "name" param 
            # and the index is less then the length of the list
            # Every list will increase the index by 1
        # If the dictionary containing a matching name is found, update the item's age with the new age 
            # Otherwise, return 'Pet not found'
            
def update_pet_age(list, name, age):
    index = 0
    while(list[index]['name'] != name and index < len(list) -1):
        index += 1
        if(list[index][name] == name ):
            list[index]['age'] = age
            return list[index]
        else:
            return 'Pet Not Found'
    
# List comprehensions vs genertor expressions


# map like 
#40. ✅ Use list comprehension to return a list containing every pet name from "pet_info" changed to uppercase
new_pet_list = [pet.get('name').upper() for pet in pet_info]

# print(new_pet_list)

# find like
# returned pet/ loop/ condtional
#41. ✅ Use list comprehension to find a pet named spot
spot = [pet for pet in pet_info if pet.get("name") == "Spot" ]
# print(spot)

# filter like
#42. ✅ Use list comprehension to find all of the pets under 3 years old
young_pets = [pet for pet in pet_info if pet.get("age") < 3]
print(young_pets)

#43. ✅ Create a generator expression matching the filter above
# main benefit, less memory intensive
young_pets = (pet for pet in pet_info if pet.get("age") < 3)

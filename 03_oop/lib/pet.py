# !/usr/bin/env python3
    # Defines the location of the Python interpreter
    # See More => https://stackoverflow.com/a/7670338/8655247

import ipdb



# Classes

# 1. ✅ Create a Pet class

# class Pet:
#     pass

# ipdb.set_trace()
    # Note: Add 'pass' to the Pet class 

# 2. ✅ Instantiate a few Pet instances

    # Compare the Pet instances. Are each of them the same object?
    
# self => the instance at moment of instantiation

# 3. ✅ Demonstrate __init__ 

class Pet:
    def __init__(self, name, age, breed, owner = "No Owner"):
        self.name = name
        self.age = age
        self.breed = breed
        self.owner = owner
        
        
# fido = Pet("Fido", 5, "Boxer")
# spot = Pet("Spot", 1, "Golden", "David")

# ipdb.set_trace()
    # Add arguments to instances  
    
    # Use dot notation to access each Pet instance's attributes 

    # Update attributes with new values

# Instance Methods

#     def say_hello(self):
#         print("Hello")

# ipdb.set_trace()
# 4. ✅ Create a "print_pet_details" function that will print each Pet instance's 
# attributes

    # Review the "self" keyword 
    
    # Invoke "print_pet_details" on an instance 
    
    # Example Terminal Ouput:
        # name: Rose
        # age: 11
        # breed: Domestic Longhair
        # temperament: Sweet
        
    def print_pet_details(self):
        print(f'''
            name:{self.name}
            age:{self.age}
            breed:{self.breed}
        ''')

# ipdb.set_trace()

# Instance/Object Properties => Attributes that are controlled by methods

class Owner:
    def __init__(self, age):
            self.age = age
            
    def get_name(self):
        return self._name
    
    def set_name(self, name):
        print("setting ownders name")
        
        if(isinstance(name, str)):
            self._name = name
        else:
            print("must be a string")
            
    name = property(get_name, set_name)
            
ipdb.set_trace()

    # Create an Owner class with two instance methods:

        # get_name => Retrieve Owner's name
        
        # set_name => Set Owner's name

            # Ensure that Owner's name is a String

            # If not, issue warning of "Name must be a string"

    # Use property() to compile get_name / set_name and invoke them
    # whenever we access an Owner instance's name
"""
CSV Reader
    Pet Adoption center
    -Reads data about various adoptable animals from CSV Files
    - based on user input

    -user input type of animal at command line
    display info about those animals from the appropriate CSV file
        -python open method
        -csv module to parse data
        -handle bad input
            try/except
            throw error if:
                trying to read file that doesnt exist
                print error message "Sorry we don't have any <input> here."
            Make sure file closes when done

            refactor solution using with statement
    DATA STRUCTURE
    name - string 
    breed - string
    age - int
    species - string

    input
"""

import csv

animal_type = input("cats or dogs?\n")

class Dog:
    def __init__(self, name, age, breed, sex, color):
        self._name = name
        self._age = age
        self._breed = breed
        self._sex = sex
        self._color = color
    # ------GETTERS AND SETTERS-------
    @property
    def name(self):
        return self._name
    @name.setter
    def name(self, new_name):
        self._name = new_name

    @property
    def age(self):
        return self._age
    @age.setter
    def age(self, new_age):
        self._age = new_age

    @property
    def breed(self):
        return self._breed
    @breed.setter
    def breed(self, new_breed):
        self._breed = new_breed
    
    @property
    def sex(self):
        return self._sex
    @sex.setter
    def sex(self, new_sex):
        self._sex = new_sex
    
    @property
    def color(self):
        return self._color
    @color.setter
    def color(self, new_color):
        self._color = new_color

    def __str__(self):
        return f"{self.name} is a {self.age} year old {self.sex} {self.breed}. They are {self.color}."
    
class Cat:
    def __init__(self, name, age, breed, sex='Unknown', color=None):
        self._name = name
        self.age = age
        self.breed = breed
        self.sex = sex
        self.color = color
    # ------GETTERS AND SETTERS-------
    @property
    def name(self):
        return self._name
    @name.setter
    def name(self, new_name):
        self._name = new_name

    @property
    def age(self):
        return self._age
    @age.setter
    def age(self, new_age):
        self._age = new_age

    @property
    def breed(self):
        return self._breed
    @breed.setter
    def breed(self, new_breed):
        self._breed = new_breed
    
    @property
    def sex(self):
        return self._sex
    @sex.setter
    def sex(self, new_sex):
        self._sex = new_sex
    
    @property
    def color(self):
        return self._color
    @color.setter
    def color(self, new_color):
        self._color = new_color

    def __str__(self):
        return f"{self.name} is a {self.age} year old {self.sex} {self.breed}. They are {self.color}."
    

dog = Dog('Foxtrot', 3, 'Belgian Malinois', 'female', 'mahogany with a black mask')
cat = Cat('George', 8, 'Domestic Shorthair', 'male', 'white and orange')

# try:
with open('./data/dogs.csv', mode='r') as csv_file:
    csv_reader = csv.DictReader(csv_file)
    animals = []
    for row in csv_reader:
        if animal_type == 'dogs':
            new_animal = Dog(row['name'],row['age'],row['breed'],row['sex'],row['color'])
            print(new_animal)
# except:
#     print(f"Sorry, we don't have any {animal_type} here.")
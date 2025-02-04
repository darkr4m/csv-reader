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
        if isinstance(new_name, str):
            self._name = new_name
        else:
            print("Name must be a string.")

    @property
    def age(self):
        return self._age
    @age.setter
    def age(self, new_age):
        if isinstance(new_age, int) and new_age > 0:
            self._age = new_age
        else:
            print("Age must be a positive integer.")
    @property
    def breed(self):
        return self._breed
    @breed.setter
    def breed(self, new_breed):
        if isinstance(new_breed, str):
            self._breed = new_breed
        else:
            print("Breed must be a string.")
    
    @property
    def sex(self):
        return self._sex
    @sex.setter
    def sex(self, new_sex):
        valid_input = ['male', 'female']
        if new_sex in valid_input:
            self._sex = new_sex
        else:
            print("Gender of animal must be either 'male' or 'female'.")
    
    @property
    def color(self):
        return self._color
    @color.setter
    def color(self, new_color):
        if isinstance(new_color, str):
            self._color = new_color
        else:
            print("Color must be a string.")

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
        if isinstance(new_name, str):
            self._name = new_name
        else:
            print("Name must be a string.")

    @property
    def age(self):
        return self._age
    @age.setter
    def age(self, new_age):
        if isinstance(new_age, int) and new_age > 0:
            self._age = new_age
        else:
            print("Age must be a positive integer.")
    @property
    def breed(self):
        return self._breed
    @breed.setter
    def breed(self, new_breed):
        if isinstance(new_breed, str):
            self._breed = new_breed
        else:
            print("Breed must be a string.")
    
    @property
    def sex(self):
        return self._sex
    @sex.setter
    def sex(self, new_sex):
        valid_input = ['male', 'female']
        if new_sex in valid_input:
            self._sex = new_sex
        else:
            print("Gender of animal must be either 'male' or 'female'.")
    
    @property
    def color(self):
        return self._color
    @color.setter
    def color(self, new_color):
        if isinstance(new_color, str):
            self._color = new_color
        else:
            print("Color must be a string.")

    def __str__(self):
        return f"{self.name} is a {self.age} year old {self.sex} {self.breed}. They are {self.color}."
    

dog = Dog('Foxtrot', 3, 'Belgian Malinois', 'female', 'mahogany with a black mask')
cat = Cat('George', 8, 'Domestic Shorthair', 'male', 'white and orange')


try:
    with open(f'./data/{animal_type}.csv', mode='r') as csv_file:
        csv_reader = csv.DictReader(csv_file, delimiter=',')
        animals = []
        for row in csv_reader:
            if animal_type == 'dogs':
                new_animal = Dog(row['name'],row['age'],row['breed'],row['sex'],row['color'])
                print(new_animal)
            if animal_type == 'cats':
                new_animal = Dog(row['name'],row['age'],row['breed'],row['sex'],row['color'])
                print(new_animal)

            animals.append(new_animal)
except:
    print(f"Sorry, we don't have any {animal_type} here.")
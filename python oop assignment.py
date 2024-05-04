class Person:
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender
    
    def introduce(self):
        print(f"Hi, my name is {self.name}, {self.age} years old {self.gender}.")

#  instance of the Person class
person = Person("Kanye", 28, "male")

person.introduce()

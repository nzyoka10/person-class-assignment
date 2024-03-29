
class Person:
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender

    def introduce(self):
        print(f"Hello there, my name is {self.name}. I am {self.age} years old and I am {self.gender}.")

# Creating an instance of the Person class
person1 = Person("NZYOKA", 12, "Male")
person2 = Person("Kioko", 35, "Male")
person3 = Person("Joy", 21, "Female")

# Calling the introduce method to display the person's information
person1.introduce()
person2.introduce()
person3.introduce()




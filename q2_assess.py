# **Ancestral Stories:** In many African cultures, the art of storytelling is passed
# down from generation to generation. Imagine you're creating an application that
# records these oral stories and translates them into different languages. The
# stories vary by length, moral lessons, and the age group they are intended for.
# Think about how you would model `Story`, `StoryTeller`, and `Translator`
# objects, and how inheritance might come into play if there are different types of
# stories or storytellers.


class Story:
    def __init__(self, title, content, age_group):
        self.title = title
        self.content = content
        self.age_group = age_group


class StoryTeller:
    def __init__(self, name):
        self.name = name
        self.stories = []

    def add_story(self, story):
        self.stories.append(story)

    def tell_story(self, title):
        story = next((s for s in self.stories if s.title == title), None)
        if story:
            print(f"Story: {story.title}")
            print(f"Content: {story.content}")
            print(f"Age Group: {story.age_group}")
        else:
            print("Story not found.")


class Translator:
    def __init__(self, language):
        self.language = language

    def translate(self, story, target_language):


class FolkTale(Story):
    def __init__(self, title, content, age_group, moral_lesson):
        super().__init__(title, content, age_group)
        self.moral_lesson = moral_lesson


# **African Cuisine:** You're creating a recipe app specifically for African cuisine.
# The app needs to handle recipes from different African countries, each with its
# unique ingredients, preparation time, cooking method, and nutritional
# information. Consider creating a `Recipe` class, and think about how you might
# create subclasses for different types of recipes (e.g., `MoroccanRecipe`,
# `EthiopianRecipe`, `NigerianRecipe`), each with their own unique properties and
# methods.




# *Wildlife Preservation:** You're a wildlife conservationist working on a
# // program to track different species in a national park. Each species has its own
# // characteristics and behaviors, such as its diet, typical lifespan, migration
# // patterns, etc. Some species might be predators, others prey. You'll need to

# // create classes to model `Species`, `Predator`, `Prey`, etc., and think about how
# // these classes might relate to each other through inheritance.



class Species:
    def __init__(self, name, diet, lifespan):
        self.name = name
        self.diet = diet
        self.lifespan = lifespan


class Predator(Species):
    def __init__(self, name, diet, lifespan, hunting_strategy):
        super().__init__(name, diet, lifespan)
        self.hunting_strategy = hunting_strategy


class Prey(Species):
    def __init__(self, name, diet, lifespan, habitat):
        super().__init__(name, diet, lifespan)
        self.habitat = habitat

lion = Predator("Lion", "Carnivore", 7, "Group hunting")
zebra = Prey("Zebra", "Herbivore", 10, "Grasslands")

print(lion.name)  
print(lion.hunting_strategy)  

print(zebra.name)  
print(zebra.habitat)  




# **African Music Festival:** You're in charge of organizing a Pan-African music
# festival. Many artists from different countries, each with their own musical style
# and instruments, are scheduled to perform. You need to write a program to
# manage the festival lineup, schedule, and stage arrangements. Think about how
# you might model the `Artist`, `Performance`, and `Stage` classes, and consider
# how you might use inheritance if there are different types of performances or
# stages.


# Create a class called Product with attributes for name, price, and quantity.
# Implement a method to calculate the total value of the product (price * quantity).
# Create multiple objects of the Product class and calculate their total values.

class Product:
    def __init__(self,name,price,quantity):
        self.name=name
        self.price=price
        self.quantity=quantity
    def calculate_total_value(self):
        return self.price * self.quantity


product1=Product("shirt",100,4)
product2 =Product("Shoes", 100, 2)
product3 =Product("Top", 30, 5)


total_value1 = product1.calculate_total_value()
total_value2 = product2.calculate_total_value()
total_value3 = product3.calculate_total_value()

print(total_value1)  
print(total_value2)  
print(total_value3) 


# Implement a class called Student with attributes for name, age, and grades (a
# list of integers). Include methods to calculate the average grade, display the
# student information, and determine if the student has passed (average grade >=
# 60). Create objects for the Student class and demonstrate the usage of these
# methods.

class Student:
    def __init__(self,name,age,grades):
        self.name=name
        self.age=age
        self.grades=grades
    def calculate_average(self):
        sum(self.grades)/2


student1=Student("Marrion",21,77)  
student2=Student("Lewinnie",17,69)  

average1=student1.calculate_average()
average2=student2.calculate_average()

print(average1)
print(average2)



class Student:
    def __init__(self, name, age, grades):
        self.name = name
        self.age = age
        self.grades = grades

    def calculate_average_grade(self):
        if not self.grades:
            return 0
        return sum(self.grades) / len(self.grades)

    def display_information(self):
        print("Student Information:")
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"Grades: {self.grades}")

    def has_passed(self):
        average_grade = self.calculate_average_grade()
        return average_grade >= 60


student1 = Student("John", 18, [75, 80, 90, 65, 70])
student2 = Student("Jane", 17, [80, 85, 95, 55, 60])
student3 = Student("Mark", 19, [70, 75, 80, 85, 90])


student1.display_information()
average_grade1 = student1.calculate_average_grade()
print(f"Average Grade: {average_grade1}")
print(f" {'Passed' if student1.has_passed() else 'Failed'}")

print()

student2.display_information()
average_grade2 = student2.calculate_average_grade()
print(f"Average Grade: {average_grade2}")
print(f" {'Passed' if student2.has_passed() else 'Failed'}")

print()

student3.display_information()
average_grade3 = student3.calculate_average_grade()
print(f"Average Grade: {average_grade3}")
print(f" {'Passed' if student3.has_passed() else 'Failed'}")

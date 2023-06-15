fun main(){


    val lion = Predator("Lion", "Carnivore", 15, "Group hunting")
    val zebra = Prey("Zebra", "Herbivore", 25, "Grasslands")

    println(lion.name)
    println(lion.huntingStrategy)

    println(zebra.name)
    println(zebra.habitat)


    val product1 = Product("Shirt", 100.00, 3)
    val product2 = Product("Shoes", 150.00, 2)
    val product3 = Product("Tops", 180.00, 5)


    val totalValue1 = product1.calculateTotalValue()
    val totalValue2 = product2.calculateTotalValue()
    val totalValue3 = product3.calculateTotalValue()

    println(totalValue1)
    println(totalValue2)
    println(totalValue3)

    val student1 = Student("John", 18, listOf(75, 80, 90, 65, 70))
    val student2 = Student("Jane", 17, listOf(80, 85, 95, 55, 60))
    val student3 = Student("Mark", 19, listOf(70, 75, 80, 85, 90))




}
//**Ancestral Stories:** In many African cultures, the art of storytelling is passed
//down from generation to generation. Imagine you're creating an application that
//records these oral stories and translates them into different languages. The
//stories vary by length, moral lessons, and the age group they are intended for.
//Think about how you would model `Story`, `StoryTeller`, and `Translator`
//objects, and how inheritance might come into play if there are different types of
//stories or storytellers.

data class Story(val title: String, val content: String, val ageGroup: String)


class StoryTeller(val name: String) {
    val stories = mutableListOf<Story>()

    fun addStory(story: Story) {
        stories.add(story)
    }

    fun tellStory(title: String) {
        val story = stories.find { it.title == title }
        if (story != null) {
            println("Story: ${story.title}")
            println("Content: ${story.content}")
            println("Age Group: ${story.ageGroup}")
        } else {
            println("Story not found.")
        }
    }
}


class Translator(val language: String) {
    fun translate(story: Story, targetLanguage: String) {

    }
}


//**African Cuisine:** You're creating a recipe app specifically for African cuisine.
//The app needs to handle recipes from different African countries, each with its
//unique ingredients, preparation time, cooking method, and nutritional
//information. Consider creating a `Recipe` class, and think about how you might
//create subclasses for different types of recipes (e.g., `MoroccanRecipe`,
//`EthiopianRecipe`, `NigerianRecipe`), each with their own unique properties and
//methods.




//*Wildlife Preservation:** You're a wildlife conservationist working on a
//// program to track different species in a national park. Each species has its own
//// characteristics and behaviors, such as its diet, typical lifespan, migration
//// patterns, etc. Some species might be predators, others prey. You'll need to
//
//// create classes to model `Species`, `Predator`, `Prey`, etc., and think about how
//// these classes might relate to each other through inheritance.


open class Species(val name: String, val diet: String, val lifespan: Int)


class Predator(name: String, diet: String, lifespan: Int, val huntingStrategy: String) : Species(name, diet, lifespan)


class Prey(name: String, diet: String, lifespan: Int, val habitat: String) : Species(name, diet, lifespan)




//**African Music Festival:** You're in charge of organizing a Pan-African music
//festival. Many artists from different countries, each with their own musical style
//and instruments, are scheduled to perform. You need to write a program to
//manage the festival lineup, schedule, and stage arrangements. Think about how
//you might model the `Artist`, `Performance`, and `Stage` classes, and consider
//how you might use inheritance if there are different types of performances or
//stages.


//Create a class called Product with attributes for name, price, and quantity.
//Implement a method to calculate the total value of the product (price * quantity).
//Create multiple objects of the Product class and calculate their total values.
class Product(val name: String, val price: Double, val quantity: Int) {
    fun calculateTotalValue(): Double {
        return price * quantity
    }
}


//Implement a class called Student with attributes for name, age, and grades (a
//list of integers). Include methods to calculate the average grade, display the
//student information, and determine if the student has passed (average grade >=
//60). Create objects for the Student class and demonstrate the usage of these
//methods.

class Student(val name: String, val age: Int, val grades: List<Int>) {
    fun calculateAverageGrade(): Double {
        if (grades.isEmpty()) {
            return 0.0
        }
        val sum = grades.sum()
        return sum.toDouble() / grades.size
    }

    fun displayInfo() {
        println("Student Information:")
        println("Name: $name")
        println("Age: $age")
        println("Grades: $grades")
    }

    fun hasPassed(): Boolean {
        val averageGrade = calculateAverageGrade()
        return averageGrade >= 60
    }
}




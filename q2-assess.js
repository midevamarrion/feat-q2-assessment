// **Ancestral Stories:** In many African cultures, the art of storytelling is passed
// down from generation to generation. Imagine you're creating an application that
// records these oral stories and translates them into different languages. The
// stories vary by length, moral lessons, and the age group they are intended for.
// Think about how you would model `Story`, `StoryTeller`, and `Translator`
// objects, and how inheritance might come into play if there are different types of
// stories or storytellers.


class Story {
  constructor(title, content, ageGroup) {
    this.title = title;
    this.content = content;
    this.ageGroup = ageGroup;
  }
}


class StoryTeller {
  constructor(name) {
    this.name = name;
    this.stories = [];
  }

  addStory(story) {
    this.stories.push(story);
  }

  narrateStory(title) {
    const story = this.stories.find(story => story.title === title);
    if (story) {
      console.log(`Story: ${story.title}`);
      console.log(`Content: ${story.content}`);
      console.log(`Age Group: ${story.ageGroup}`);
    } else {
      console.log(`Story not found.`);
    }
  }
}


class Translator {
  constructor(language) {
    this.language = language;
  }

  translate(story, targetLanguage) {
    
  }
}


class FolkTale extends Story {
  constructor(title, content, ageGroup, moralLesson) {
    super(title, content, ageGroup);
    this.moralLesson = moralLesson;
  }
}


// **African Cuisine:** You're creating a recipe app specifically for African cuisine.
// The app needs to handle recipes from different African countries, each with its
// unique ingredients, preparation time, cooking method, and nutritional
// information. Consider creating a `Recipe` class, and think about how you might
// create subclasses for different types of recipes (e.g., `MoroccanRecipe`,
// `EthiopianRecipe`, `NigerianRecipe`), each with their own unique properties and
// methods.








// **Wildlife Preservation:** You're a wildlife conservationist working on a
// program to track different species in a national park. Each species has its own
// characteristics and behaviors, such as its diet, typical lifespan, migration
// patterns, etc. Some species might be predators, others prey. You'll need to

// create classes to model `Species`, `Predator`, `Prey`, etc., and think about how
// these classes might relate to each other through inheritance.



class Species {
    constructor(name, diet, lifespan) {
      this.name = name;
      this.diet = diet;
      this.lifespan = lifespan;
    }
  }
  
  
  class Predator extends Species {
    constructor(name, diet, lifespan, huntingStrategy) {
      super(name, diet, lifespan);
      this.huntingStrategy = huntingStrategy;
    }
  }
  

  class Prey extends Species {
    constructor(name, diet, lifespan, habitat) {
      super(name, diet, lifespan);
      this.habitat = habitat;
    }
  }
  
  
  const lion = new Predator("Lion", "Carnivore", 7, "Group hunting");
  const zebra = new Prey("Zebra", "Herbivore", 10, "Grasslands");
  
  console.log(lion.name);
  console.log(lion.huntingStrategy);  
  
  console.log(zebra.name);  
  console.log(zebra.habitat); 
  



// **African Music Festival:** You're in charge of organizing a Pan-African music
// festival. Many artists from different countries, each with their own musical style
// and instruments, are scheduled to perform. You need to write a program to
// manage the festival lineup, schedule, and stage arrangements. Think about how
// you might model the `Artist`, `Performance`, and `Stage` classes, and consider
// how you might use inheritance if there are different types of performances or
// stages.



// Create a class called Product with attributes for name, price, and quantity.
// Implement a method to calculate the total value of the product (price * quantity).
// Create multiple objects of the Product class and calculate their total values.

class Product {
    constructor(name, price, quantity) {
      this.name = name;
      this.price = price;
      this.quantity = quantity;
    }
  
    calculateTotalValue() {
      return this.price * this.quantity;
    }
  }
  
  
  const product1 = new Product("Shirt", 40, 3);
  const product2 = new Product("Shoes", 100, 2);
  const product3 = new Product("Top", 30, 5);
  
  
  const totalValue1 = product1.calculateTotalValue();
  const totalValue2 = product2.calculateTotalValue();
  const totalValue3 = product3.calculateTotalValue();
  
  console.log(totalValue1); 
  console.log(totalValue2); 
  console.log(totalValue3); 
  
  
//   Implement a class called Student with attributes for name, age, and grades (a
//     list of integers). Include methods to calculate the average grade, display the
//     student information, and determine if the student has passed (average grade >=
//     60). Create objects for the Student class and demonstrate the usage of these
//     methods.

class Student{
    constructor(name,age,grades){
        self.name=name;
        self.age=age;
        self.grades=grades;
    }
    calculateAverage(){
        
    }

}

  
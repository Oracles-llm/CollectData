# Template Method Design Pattern

Last Updated :
13 Sep, 2025

Template Method Design Pattern is a behavioral pattern that defines the skeleton of an algorithm in a base method while allowing subclasses to override specific steps without altering its overall structure. It’s like a recipe: the main steps remain fixed, but details can be customized for variation.

Let's understand this with the help of Diagram:

## Components of Template Method Design Pattern

**Abstract Class/Interface**: Defines the template method (algorithm skeleton) with some steps implemented and others left abstract or as hooks for customization.**Template Method**: Outlines the algorithm’s fixed structure by calling steps in order, often marked *final* to prevent changes.**Abstract/Hook Methods**: Placeholder methods in the abstract class that subclasses implement or optionally override.**Concrete Subclasses**: Provide implementations for abstract methods, customizing specific steps while preserving the overall algorithm.

## How to Implement Template Method Design Pattern?

Let us see how to implement the Template Method Design Pattern in these simple steps:

**Step 1: Create an Abstract Class**: Start by making a base or abstract class that defines the overall structure of the algorithm. This class will have a template method to outline the steps.**Step 2: Define the Template Method**: Inside the abstract class, create a method (the template method) that calls each step of the algorithm in a specific order.**Step 3: Implement Core Steps**: For each step of the algorithm, create individual methods in the abstract class. Some methods can have default implementations, while others can be abstract to allow customization.**Step 4: Create Subclasses**: Now, create subclasses that inherit from the abstract class. In each subclass, override the steps that need specific behavior, leaving the rest as they are.**Step 5: Use the Template Method**: When you run the template method on a subclass instance, it will execute all the steps in the defined order, with customizations in place from the overridden methods.

**Use of the Template Method Design Pattern**

**Common Algorithm with Variations**: When an algorithm has a common structure but differs in some steps or implementations, the Template Method pattern can help subclasses customize specific parts while encapsulating the common phases in a superclass.**Code Reusability**: By specifying the common steps in one place, the Template Method design encourages code reuse when you have similar tasks or processes that must be executed in several contexts.**Enforcing Structure**: It's useful when you want to provide some elements of an algorithm flexibility while maintaining a particular structure or set of steps.**Reducing Duplication**: By centralizing common behavior in the abstract class and avoiding duplication of code in subclasses, the Template Method pattern helps in maintaining a clean and organized codebase.

**When not to use the Template Method Design Pattern?**

**When Algorithms are Highly Variable**: Using the Template Method pattern might not be appropriate if the algorithms you're dealing with have a lot of differences in their steps and structure and little in common. This is because it could result in inappropriate abstraction or excessive complexity.**Tight Coupling Between Steps**: The Template Method pattern might not offer enough flexibility if there is a close coupling between the algorithm's parts, so modifications to one step require modifications to other steps.**Inflexibility with Runtime Changes**: Because the Template Method pattern depends on predetermined structure and behavior, it might not be the best option if you expect frequent changes to the algorithm's stages or structure at runtime.

## Template Method Design Pattern example (with implementation)

**Problem Statement:**

Let's consider a scenario where we have a process for making different types of beverages, such as tea and coffee. While the overall process of making beverages is similar (e.g., boiling water, adding ingredients), the specific steps and ingredients vary for each type of beverage.


**Benefits of using Template Method Design Pattern in this scenario**

- Using the Template Method pattern in this scenario allows us to define a common structure for making beverages in a superclass while allowing subclasses to customize specific steps, such as adding ingredients, without changing the overall process.
- This promotes code reuse, reduces duplication, and provides a flexible way to accommodate variations in beverage preparation.

### Below is the implementation for the above problem statement using Template Design Pattern

Let’s break down into the component wise code:

### 1. **Abstract Class**

C++
// Abstract class defining the template method
#include <iostream>
class BeverageMaker {
public:
// Template method defining the overall process
void makeBeverage() {
boilWater();
brew();
pourInCup();
addCondiments();
}
// Abstract methods to be implemented by subclasses
virtual void brew() = 0;
virtual void addCondiments() = 0;
// Common methods
void boilWater() {
std::cout << "Boiling water" << std::endl;
}
void pourInCup() {
std::cout << "Pouring into cup" << std::endl;
}
};


Java
/* Abstract class defining the template method */
abstract class BeverageMaker {
// Template method defining the overall process
void makeBeverage() {
this.boilWater();
this.brew();
this.pourInCup();
this.addCondiments();
}
// Abstract methods to be implemented by subclasses
abstract void brew();
abstract void addCondiments();
// Common methods
void boilWater() {
System.out.println("Boiling water");
}
void pourInCup() {
System.out.println("Pouring into cup");
}
}


Python
# Abstract class defining the template method
from abc import ABC, abstractmethod
class BeverageMaker(ABC):
# Template method defining the overall process
def make_beverage(self):
self.boil_water()
self.brew()
self.pour_in_cup()
self.add_condiments()
# Abstract methods to be implemented by subclasses
@abstractmethod
def brew(self):
pass
@abstractmethod
def add_condiments(self):
pass
# Common methods
def boil_water(self):
print("Boiling water")
def pour_in_cup(self):
print("Pouring into cup")


JavaScript
// Abstract class defining the template method
class BeverageMaker {
// Template method defining the overall process
makeBeverage() {
this.boilWater();
this.brew();
this.pourInCup();
this.addCondiments();
}
// Abstract methods to be implemented by subclasses
brew() {
throw new Error("Method 'brew()' must be implemented.");
}
addCondiments() {
throw new Error("Method 'addCondiments()' must be implemented.");
}
// Common methods
boilWater() {
console.log("Boiling water");
}
pourInCup() {
console.log("Pouring into cup");
}
}


### 2. **Concrete Class (TeaMaker)**

C++
#include <iostream>
class BeverageMaker {
public:
virtual void brew() = 0;
virtual void addCondiments() = 0;
};
class TeaMaker : public BeverageMaker {
public:
// Implementing abstract methods
void brew() override {
std::cout << "Steeping the tea" << std::endl;
}
void addCondiments() override {
std::cout << "Adding lemon" << std::endl;
}
};


Java
abstract class BeverageMaker {
// Abstract methods to be implemented
abstract void brew();
abstract void addCondiments();
}
class TeaMaker extends BeverageMaker {
// Implementing abstract methods
@Override
void brew() {
System.out.println("Steeping the tea");
}
@Override
void addCondiments() {
System.out.println("Adding lemon");
}
}


Python
class TeaMaker(BeverageMaker):
# Implementing abstract methods
def brew(self):
print("Steeping the tea")
def addCondiments(self):
print("Adding lemon")


JavaScript
class TeaMaker extends BeverageMaker {
// Implementing abstract methods
brew() {
console.log("Steeping the tea");
}
addCondiments() {
console.log("Adding lemon");
}
}


### 3. **Concrete Class (CoffeeMaker)**

C++
// Concrete subclass for making coffee
class CoffeeMaker : public BeverageMaker {
// Implementing abstract methods
void brew() override {
std::cout << "Dripping coffee through filter" << std::endl;
}
void addCondiments() override {
std::cout << "Adding sugar and milk" << std::endl;
}
};


Java
/* Concrete subclass for making coffee */
class CoffeeMaker extends BeverageMaker {
// Implementing abstract methods
@Override
void brew() {
System.out.println("Dripping coffee through filter");
}
@Override
void addCondiments() {
System.out.println("Adding sugar and milk");
}
}


Python
# Concrete subclass for making coffee
class CoffeeMaker(BeverageMaker):
# Implementing abstract methods
def brew(self):
print("Dripping coffee through filter")
def addCondiments(self):
print("Adding sugar and milk")


JavaScript
// Concrete subclass for making coffee
class CoffeeMaker extends BeverageMaker {
// Implementing abstract methods
brew() {
console.log('Dripping coffee through filter');
}
addCondiments() {
console.log('Adding sugar and milk');
}
}


### Complete code for the above example

Below is the complete code for the above example:

C++
// Abstract class defining the template method
abstract class BeverageMaker {
// Template method defining the overall process
public final void makeBeverage() {
boilWater();
brew();
pourInCup();
addCondiments();
}
// Abstract methods to be implemented by subclasses
abstract void brew();
abstract void addCondiments();
// Common methods
void boilWater() {
System.out.println("Boiling water");
}
void pourInCup() {
System.out.println("Pouring into cup");
}
}
// Concrete subclass for making tea
class TeaMaker extends BeverageMaker {
// Implementing abstract methods
@Override
void brew() {
System.out.println("Steeping the tea");
}
@Override
void addCondiments() {
System.out.println("Adding lemon");
}
}
// Concrete subclass for making coffee
class CoffeeMaker extends BeverageMaker {
// Implementing abstract methods
@Override
void brew() {
System.out.println("Dripping coffee through filter");
}
@Override
void addCondiments() {
System.out.println("Adding sugar and milk");
}
}
public class Main {
public static void main(String[] args) {
System.out.println("Making tea:");
BeverageMaker teaMaker = new TeaMaker();
teaMaker.makeBeverage();
System.out.println("\nMaking coffee:");
BeverageMaker coffeeMaker = new CoffeeMaker();
coffeeMaker.makeBeverage();
}
}


Java
// Abstract class defining the template method
abstract class BeverageMaker {
// Template method defining the overall process
public final void makeBeverage() {
boilWater();
brew();
pourInCup();
addCondiments();
}
// Abstract methods to be implemented by subclasses
abstract void brew();
abstract void addCondiments();
// Common methods
void boilWater() {
System.out.println("Boiling water");
}
void pourInCup() {
System.out.println("Pouring into cup");
}
}
// Concrete subclass for making tea
class TeaMaker extends BeverageMaker {
// Implementing abstract methods
@Override
void brew() {
System.out.println("Steeping the tea");
}
@Override
void addCondiments() {
System.out.println("Adding lemon");
}
}
// Concrete subclass for making coffee
class CoffeeMaker extends BeverageMaker {
// Implementing abstract methods
@Override
void brew() {
System.out.println("Dripping coffee through filter");
}
@Override
void addCondiments() {
System.out.println("Adding sugar and milk");
}
}
public class Main {
public static void main(String[] args) {
System.out.println("Making tea:");
BeverageMaker teaMaker = new TeaMaker();
teaMaker.makeBeverage();
System.out.println("\nMaking coffee:");
BeverageMaker coffeeMaker = new CoffeeMaker();
coffeeMaker.makeBeverage();
}
}


Python
# Abstract class defining the template method
from abc import ABC, abstractmethod
class BeverageMaker(ABC):
# Template method defining the overall process
def make_beverage(self):
self.boil_water()
self.brew()
self.pour_in_cup()
self.add_condiments()
# Common methods
def boil_water(self):
print("Boiling water")
def pour_in_cup(self):
print("Pouring into cup")
# Abstract methods to be implemented by subclasses
@abstractmethod
def brew(self):
pass
@abstractmethod
def add_condiments(self):
pass
# Concrete subclass for making tea
class TeaMaker(BeverageMaker):
# Implementing abstract methods
def brew(self):
print("Steeping the tea")
def add_condiments(self):
print("Adding lemon")
# Concrete subclass for making coffee
class CoffeeMaker(BeverageMaker):
# Implementing abstract methods
def brew(self):
print("Dripping coffee through filter")
def add_condiments(self):
print("Adding sugar and milk")
if __name__ == '__main__':
print('Making tea:')
tea_maker = TeaMaker()
tea_maker.make_beverage()
print('\nMaking coffee:')
coffee_maker = CoffeeMaker()
coffee_maker.make_beverage()


JavaScript
// Abstract class defining the template method
class BeverageMaker {
// Template method defining the overall process
makeBeverage() {
this.boilWater();
this.brew();
this.pourInCup();
this.addCondiments();
}
// Common methods
boilWater() {
console.log('Boiling water');
}
pourInCup() {
console.log('Pouring into cup');
}
// Abstract methods to be implemented by subclasses
brew() {
throw new Error('Method brew() must be implemented.');
}
addCondiments() {
throw new Error('Method addCondiments() must be implemented.');
}
}
// Concrete subclass for making tea
class TeaMaker extends BeverageMaker {
// Implementing abstract methods
brew() {
console.log('Steeping the tea');
}
addCondiments() {
console.log('Adding lemon');
}
}
// Concrete subclass for making coffee
class CoffeeMaker extends BeverageMaker {
// Implementing abstract methods
brew() {
console.log('Dripping coffee through filter');
}
addCondiments() {
console.log('Adding sugar and milk');
}
}
console.log('Making tea:');
const teaMaker = new TeaMaker();
teaMaker.makeBeverage();
console.log('\nMaking coffee:');
const coffeeMaker = new CoffeeMaker();
coffeeMaker.makeBeverage();


**Output:**

Output
Making tea:
Boiling water
Steeping the tea
Pouring into cup
Adding lemon
Making coffee:
Boiling water
Dripping coffee through filter
Pouring into cup
Adding sugar and milk


### Communication flow of the above example implementation:

**Client Interaction**: Imagine you're the person who wants to make a hot beverage, so you decide whether you want tea or coffee.**Template Method Execution**: You follow a predefined set of steps to make your chosen beverage. These steps are outlined in a recipe book (abstract class) that you have.**Execution Flow within Template Method**: You start by boiling water, pouring it into a cup, then you add your specific ingredients depending on whether you're making tea or coffee. These steps are part of the recipe (template method).**Subclass Implementation**: You decide to make tea, so you follow the tea recipe (subclass). In this recipe, instead of adding coffee grounds, you steep a tea bag and add lemon.**Method Overrides**: When you add lemon to your tea, you're customizing that step of the recipe. In programming, this is similar to overriding a method, where you provide your own implementation of a step.**Inheritance and Polymorphism**: You can use the same recipe book (abstract class) to make different beverages (concrete subclasses), whether it's tea or coffee. This is because the recipes (methods) are inherited from the abstract class.

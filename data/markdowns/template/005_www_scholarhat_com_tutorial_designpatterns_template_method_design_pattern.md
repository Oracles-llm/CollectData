## Template Method Design Pattern

**Template Method Design Pattern** is a type of **behavioral design pattern** that comes under **Gangs of Four Design Patterns**. Defining the **general framework of an algorithm **in the superclass allows subclasses to override individual stages without affecting the algorithm's overall structure.

In the **Design pattern tutorial**, we will explore about **what is template method design pattern?**, components of template method design pattern, structure of template method design pattern, implementation of template method design pattern, and many more. **Skilled .NET developers with design pattern expertise earn up to $12,000 more annually. Join our Free .NET Design Patterns Course with Certification now!**

## What is the Template method Design Pattern?

**Template Method Design Pattern** defines the structure of an algorithm in a base **class**, allowing subclasses to override specific steps without changing the overall algorithm. It ensures a consistent algorithm while enabling flexibility in its implementation details.

- The
**parent class**maintains the general hierarchy and flow of the**algorithm**. - A template refers to a prepared format, such as an
**HTML**template with a predetermined format. The template method pattern uses a similar preset structure technique called a**template method**, which consists of phases. - These actions might be an
**abstract**procedure that its subclasses carry out. - This is among the simplest to comprehend and implement. This design approach reduces code duplication and is often used in
**framework**development.

Read More: |
Types of Design Patterns |
IoC Container and DI Container: An Easy Guidel |
Different Types of Software Design Principles |

## Components of Template Method Design Pattern

**There are four components in the Template method design pattern that are:**

**Abstract Class (or Interface)****Template Method****Abstract (or Hook) Methods****Concrete Subclasses**

** **

### 1. Abstract Class (or Interface)

- Defines the template method outlining the algorithm's structure.
- Includes abstract methods for steps that vary in different implementations.
- Provides hook methods with default behavior that can be overridden.
- Ensures a consistent sequence of operations across subclasses.
- Promotes code reuse by handling common parts of the algorithm.

### 2. Template Method

- describes the general layout and flow of the algorithm.
- Calls on abstract methods that subclasses have implemented.
- May invoke hook methods with subclasses' ability to override the default behavior.
- Allows for customization of individual phases while ensuring a consistent order of activities.
- Reduces code duplication by
**encapsulating**the algorithm's common phases.

### 3. Abstract (or Hook) Methods

- Represent steps of the algorithm that vary among implementations.
- Declared in the abstract class or interface and must be implemented by subclasses.
- Allow subclasses to define specific behavior for different parts of the algorithm.
- Provide flexibility while maintaining the overall structure defined by the template method.
- It can be overridden to customize or extend the behavior of the algorithm.

### 4. Concrete Subclasses

- Implement the abstract methods defined in the base class or interface.
- Provide specific details or variations for the algorithm steps.
- Adhere to the structure outlined by the template method in the base class.
- Optionally override hook methods to customize default behavior.
- Ensure that the algorithm defined in the base class functions correctly with the provided implementations.

## Structure of Template Method Design Pattern

- Both the actual template method that calls these methods in a certain sequence and the methods that function as stages in an algorithm are declared in the Abstract Class. The steps might have a default implementation or be declared abstract.
- The template method itself cannot be overridden by Concrete Classes, but all of the phases may.

## Implementation of Template Method Design Factory

**The implementation of the Template method design pattern is as follows:**

### 1. Abstract Base Class

- Create an abstract class that defines the template method.
- This template method will outline the steps of the algorithm, some of which will be abstract (to be implemented by subclasses).

### 2. Define Template Method

- The template method is the final method in the abstract class that provides the algorithm's structure.
- It is called abstract methods, some of which are implemented by subclasses, and it may be called hook methods for optional customization.

### 3. Abstract and Hook Methods

- Define abstract methods for steps that need to be customized by subclasses.
- Optionally, provide hook methods with default implementations that subclasses can override if needed.

### 4. Concrete Subclasses

- Create concrete subclasses that extend the abstract class and implement the abstract methods.
- These subclasses define specific behaviors for the algorithm's variable steps while adhering to the template's overall structure.

## Real-world Example of Template Method Design Pattern

### Beverage Preparation (Tea and Coffee)

Both tea and coffee require boiling water, brewing the drink, pouring it into a cup, and optionally adding condiments. The common steps can be handled by the template method, while the variations (like brewing tea vs. coffee) are handled by the subclasses.

#### Steps of the Process:

- Boil Water
- Brew (Tea/Coffee)
- Pour into cup
- Add Condiments (optional)

```
using System;
abstract class Beverage
{
// Template method
public void PrepareRecipe()
{
BoilWater();
Brew();
PourInCup();
AddCondiments();
}
// Common step for all beverages
public void BoilWater()
{
Console.WriteLine("Boiling water");
}
// Common step for all beverages
public void PourInCup()
{
Console.WriteLine("Pouring into cup");
}
// Abstract methods to be implemented by subclasses
protected abstract void Brew();
protected abstract void AddCondiments();
}
class Tea : Beverage
{
protected override void Brew()
{
Console.WriteLine("Steeping the tea");
}
protected override void AddCondiments()
{
Console.WriteLine("Adding lemon");
}
}
class Coffee : Beverage
{
protected override void Brew()
{
Console.WriteLine("Dripping coffee through filter");
}
protected override void AddCondiments()
{
Console.WriteLine("Adding sugar and milk");
}
}
class Program
{
static void Main()
{
Beverage tea = new Tea();
tea.PrepareRecipe();
Beverage coffee = new Coffee();
coffee.PrepareRecipe();
}
}
```


```
from abc import ABC, abstractmethod
class Beverage(ABC):
# Template method
def prepare_recipe(self):
self.boil_water()
self.brew()
self.pour_in_cup()
self.add_condiments()
# Common step for all beverages
def boil_water(self):
print("Boiling water")
# Common step for all beverages
def pour_in_cup(self):
print("Pouring into cup")
@abstractmethod
def brew(self):
pass
@abstractmethod
def add_condiments(self):
pass
class Tea(Beverage):
def brew(self):
print("Steeping the tea")
def add_condiments(self):
print("Adding lemon")
class Coffee(Beverage):
def brew(self):
print("Dripping coffee through filter")
def add_condiments(self):
print("Adding sugar and milk")
if __name__ == "__main__":
tea = Tea()
tea.prepare_recipe()
coffee = Coffee()
coffee.prepare_recipe()
```


```
abstract class Beverage {
// Template method
public final void prepareRecipe() {
boilWater();
brew();
pourInCup();
addCondiments();
}
// Common step for all beverages
public void boilWater() {
System.out.println("Boiling water");
}
// Common step for all beverages
public void pourInCup() {
System.out.println("Pouring into cup");
}
// Abstract methods to be implemented by subclasses
abstract void brew();
abstract void addCondiments();
}
class Tea extends Beverage {
@Override
public void brew() {
System.out.println("Steeping the tea");
}
@Override
public void addCondiments() {
System.out.println("Adding lemon");
}
}
class Coffee extends Beverage {
@Override
public void brew() {
System.out.println("Dripping coffee through filter");
}
@Override
public void addCondiments() {
System.out.println("Adding sugar and milk");
}
}
public class Main {
public static void main(String[] args) {
Beverage tea = new Tea();
tea.prepareRecipe();
Beverage coffee = new Coffee();
coffee.prepareRecipe();
}
}
```


```
abstract class Beverage {
// Template method
public prepareRecipe(): void {
this.boilWater();
this.brew();
this.pourInCup();
this.addCondiments();
}
// Common step for all beverages
private boilWater(): void {
console.log("Boiling water");
}
// Common step for all beverages
private pourInCup(): void {
console.log("Pouring into cup");
}
// Abstract methods to be implemented by subclasses
protected abstract brew(): void;
protected abstract addCondiments(): void;
}
class Tea extends Beverage {
protected brew(): void {
console.log("Steeping the tea");
}
protected addCondiments(): void {
console.log("Adding lemon");
}
}
class Coffee extends Beverage {
protected brew(): void {
console.log("Dripping coffee through filter");
}
protected addCondiments(): void {
console.log("Adding sugar and milk");
}
}
const tea = new Tea();
tea.prepareRecipe();
const coffee = new Coffee();
coffee.prepareRecipe();
```


#### Output

```
Boiling water
Steeping the tea
Pouring into cup
Adding lemon
Boiling water
Dripping coffee through filter
Pouring into cup
Adding sugar and milk
```


#### Explanation

- The
**Beverage class**defines the template method**prepareRecipe()**, which outlines the steps for making a beverage. - The abstract methods
**brew()**and**addCondiments()**are implemented differently by the subclasses**Tea**and**Coffee**. - The common steps (boiling water and pouring into a cup) are handled in the base class, ensuring consistency across beverages.

## When to use Template Method Design Pattern

**Here are the several aspects where you should use this design pattern:**

#### 1. Common Algorithm with Variations

When you have an algorithm with common steps, some steps need to be customized by subclasses. For example, making different beverages (tea and coffee) follows a similar process but differs in some steps.

#### 2. Code Reusability

When you want to avoid code duplication, you can do so by encapsulating the shared steps of an algorithm in a base class and allowing subclasses to implement the specific steps.

#### 3. Consistent Algorithm Structure

When you need to ensure that the overall structure of the algorithm remains consistent across multiple subclasses while allowing variations in specific steps.

#### 4. Frameworks and Libraries

When building a** framework **where the high-level flow (template method) should remain the same, but users can extend and provide their own implementations for certain parts of the process (via abstract methods).

#### 5. Hook Methods for Flexibility

When you want to allow optional customization of some steps by providing default behavior in the base class that can be overridden by subclasses if needed.

## When not to use Template Method Design Pattern

**Here are the several reasons that you should not use this design pattern:**

**1. Algorithm is Simple:**If the algorithm is straightforward and doesn't need variations, using this pattern can add unnecessary complexity.

**2. Few or No Shared Steps:**When there are minimal common steps between subclasses, it’s better to implement them separately without forcing a common structure.

**3. Frequent Changes in Algorithm Structure:**If the overall structure of the algorithm is likely to change frequently, the pattern becomes rigid and hard to maintain.

**4. Prefer Composition Over Inheritance:**When composition (using objects) is a better fit than inheritance, using the Template Method may limit flexibility.

## Comparison with Other Design Patterns

### 1. Template Method vs. Strategy

**Template:**Fixed algorithm structure with customizable steps.**Strategy:**Swappable algorithms, no fixed structure.

### 2. Template Method vs. Factory Method

**Template:**Defines the process flow; subclasses modify steps.**Factory:**Focuses on creating**objects**; subclasses choose the object type.

### 3. Template Method vs. Observer

**Template:**Subclasses customize algorithm steps.**Observer:**Notifies multiple objects about changes, but there are no fixed steps.

### 4. Template Method vs. Decorator

**Template:**Customizes steps within a defined process.**Decorator:**Adds new functionality to objects dynamically.

### 5. Template Method vs. Builder

**Template:**Fixed algorithm with flexible steps.**Builder:**Flexible construction of complex objects step by step.

## Advantages of Template Method Design Pattern

- It provides a common algorithm framework that encourages the reuse of code.
- Subclasses minimize redundancy by customizing just particular stages.
- Increases adaptability by permitting changes to certain techniques.
- Maintains a uniform process between various classes.
- Sticks to the "open for extension, closed for modification" principle.
- Centralizes the algorithm within the basic class, making maintenance easier.

## Disadvantages of Template Method Design Pattern

- Base and subclasses are closely correlated. Therefore, modifications to one class will impact all of the subclasses.
- This might result in increased code complexity as the class hierarchy expands.
- Restricted flexibility due to the predetermined overall structure of the method.
- Makes the base class responsible for both the specific steps and the algorithm flow, which is against the
**Single Responsibility Principle**. - If several variants are required, subclassing may get difficult.

##### Conclusion

In conclusion, the **Template Method Design Pattern** ensures consistent algorithms with customizable steps but may cause tight coupling and complexity in subclasses. It’s best used when the algorithm structure needs to stay fixed with some variations.


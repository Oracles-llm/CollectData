# Template Method Design Pattern in Java

Template Design Pattern or Template Method is the behavioral design pattern that defines the skeleton of an algorithm in the superclass but lets subclasses override specific steps of the algorithm without changing its structure.


This pattern falls under the category of the "behavioral" design patterns as it is concerned with how classes collaborate and communicate with other classes.

Important Topics for Template Method Design Pattern in Java

## Key Component of Template Method Design Pattern

In Java, the Template Method pattern is implemented using abstract classes. Let's see the key elements of the Template Method Pattern:

**Abstract Class**

- Define an abstract class that declares the template method. The template method typically consists of a series of method calls and control flow statements.
- The template method defines the algorithm's structure but leaves some steps to be implemented by concrete subclasses.

**Concrete Classes**

- Create concrete subclasses that extend the abstract class.
- Implement the abstract methods declared in the abstract class to provide specific behavior for each step of the algorithm.

**Template Method Invocation**

- Clients use the template method to execute the algorithm. The template method ensures that the steps are executed in the correct order, and some steps may be overridden by subclasses.

**Hooks**

- Hooks are methods in the superclass that have a default (empty or no-op) implementation but can be optionally overridden by subclasses. They allow subclasses to "hook into" the algorithm at certain points, influencing its behavior.

So this Pattern provides a way to define the skeleton of an algorithm in the superclass while allowing subclasses to provide specific implementations for certain steps. This promotes code reuse and ensures that the overall algorithm structure remains consistent across different implementations.

**Example of Template Method Design Pattern in Java**

**Problem Statement: **

Let's assume we are developing a game that involves different characters (e.g., warriors, mages, archers) that have a common sequence of actions during their turn in a battle. However, each character may have specific behavior for certain actions like attacking, defending, and resting.


**Explanation of the Problem:**

So in this problem, the **'Character'** class is the abstract class that defines the template method **'takeTurn()'**. The concrete subclasses (**'Warrior'** and **'Mage'**) implement the abstract methods (**'startTurn()'**, **'performAction()'**, **'endTurn()'**) according to their specific behaviors. The client code (**'Game'** class) can create instances of different characters and invoke their **'takeTurn()'** method, relying on the template method to ensure a common sequence of actions.

### Overall Code of above problem Statement:

Java
// Abstract class representing the character
abstract class Character {
// Template method that defines the common sequence of actions
public void takeTurn() {
startTurn();
performAction();
endTurn();
}
// Abstract methods to be implemented by subclasses
protected abstract void startTurn();
protected abstract void performAction();
protected abstract void endTurn();
}
// Concrete subclass representing a warrior character
class Warrior extends Character {
@Override
protected void startTurn() {
System.out.println("Warrior is preparing for the turn.");
}
@Override
protected void performAction() {
System.out.println("Warrior is attacking with a sword.");
}
@Override
protected void endTurn() {
System.out.println("Warrior is resting after the turn.");
}
}
// Concrete subclass representing a mage character
class Mage extends Character {
@Override
protected void startTurn() {
System.out.println("Mage is focusing energy for the turn.");
}
@Override
protected void performAction() {
System.out.println("Mage is casting a spell.");
}
@Override
protected void endTurn() {
System.out.println("Mage is recovering after the turn.");
}
}
// Client code
public class Game {
public static void main(String[] args) {
// Creating instances of different characters
Character warrior = new Warrior();
Character mage = new Mage();
// Invoking the template method for each character
System.out.println("Warrior's Turn:");
warrior.takeTurn();
System.out.println("\nMage's Turn:");
mage.takeTurn();
}
}


**Output**Warrior's Turn:
Warrior is preparing for the turn.
Warrior is attacking with a sword.
Warrior is resting after the turn.
Mage's Turn:
Mage is focusing energy for the turn.
Mage is casting a spell.
Ma...

### Diagrammatic Representation of Above Problem

**Abstract Character Class**

Java
abstract class Character {
// Template method that defines the common sequence of actions
public void takeTurn() {
startTurn();
performAction();
endTurn();
}
// Abstract methods to be implemented by subclasses
protected abstract void startTurn();
protected abstract void performAction();
protected abstract void endTurn();
}


**'Character'** is an abstract class representing the common structure of characters in the game.**'takeTurn()' **is the template method that defines the sequence of actions during a character's turn. It consists of three steps: **'startTurn()', 'performAction()', and 'endTurn()'**.- There are three abstract methods (
**'startTurn()', 'performAction()', 'endTurn()'**) that subclasses must implement. These represent the specific actions that can vary for each type of character.

**Concrete Warrior Class**

Java
class Warrior extends Character {
@Override
protected void startTurn() {
System.out.println("Warrior is preparing for the turn.");
}
@Override
protected void performAction() {
System.out.println("Warrior is attacking with a sword.");
}
@Override
protected void endTurn() {
System.out.println("Warrior is resting after the turn.");
}
}


**'Warrior'** is a concrete subclass of **'Character'**.- It overrides the abstract methods (
**'startTurn()', 'performAction()', 'endTurn()'**) with specific implementations for a warrior character.

**Concrete Mage Class**

Java
class Mage extends Character {
@Override
protected void startTurn() {
System.out.println("Mage is focusing energy for the turn.");
}
@Override
protected void performAction() {
System.out.println("Mage is casting a spell.");
}
@Override
protected void endTurn() {
System.out.println("Mage is recovering after the turn.");
}
}


**'Mage'** is another concrete subclass of **'Character'.**- Similar to
**'Warrior',** it provides specific implementations for the abstract methods.

**Client Code (Game Class)**

Java
public class Game {
public static void main(String[] args) {
// Creating instances of different characters
Character warrior = new Warrior();
Character mage = new Mage();
// Invoking the template method for each character
System.out.println("Warrior's Turn:");
warrior.takeTurn();
System.out.println("\nMage's Turn:");
mage.takeTurn();
}
}


- In the
**'Game'** class, instances of** 'Warrior' **and **'Mage' **are created. - The
**'takeTurn()'** method is invoked for each character, demonstrating the template method pattern. The common sequence of actions (**'startTurn()', 'performAction()', 'endTurn()'**) is followed, but the specific implementations for each character are called based on polymorphism.

### Use Cases of Template Method Design Pattern in Java

This pattern is quite useful in scenarios where we have a common algorithm that needs slight variations in its steps based on different contexts. let's see some of the common use cases of the Template Method Pattern:

**Order of Operations**: In the workflow system, we might have a template method that represents the overall process of handling a request. Subclasses can then override specific steps like validation, authorization, and execution while keeping the order of operations intact.**Code Reuse**: In GUI frameworks, we could have a template method that outlines the process of rendering a UI component. Subclasses can then specialize in rendering specific types of components (e.g., buttons, text fields) while inheriting common behavior.**Database Access**: In a database access library, we have the template method that represents the process of connecting to a database, executing a query, and closing the connection. Subclasses can provide specific implementations for different database systems.**Game Development**: In the game development, a template method can define the overall game loop structure. Subclasses can then override specific steps like updating game logic, rendering graphics, and handling user input.**Logging Frameworks**: In a logging framework, we have a template method that defines the process of logging information. Subclasses can provide specific implementations for logging to different destinations (e.g., console, file, database).**Document Generation**: In a document generation system, we can use the template method for creating different types of documents (e.g., PDF, HTML). Subclasses can override steps like content generation and formatting while inheriting common document creation logic.**Web Frameworks**: In a web framework, a template method can define the structure of handling HTTP requests. Subclasses can then provide specific implementations for routing, authentication, and request handling.**Workflow Engines**: In the workflow engine, we might use a template method that represents the overall process of executing a workflow. Subclasses can specialize in implementing the specific activities or tasks within the workflow.

## Advantages of Template Method Design Pattern in Java

Let's see some of the advantages of Template Method Pattern:

**Consistent Algorithm Structure**: The pattern enforces a consistent algorithm structure across multiple subclasses. This ensures that certain steps are followed in a prescribed order, providing a common interface for different implementations.**Code Reusability**: The pattern promotes code reuse by defining a common algorithm structure in the superclass. Subclasses can reuse this structure without duplicating code.**Maintenance and Extensibility**: Changes to the algorithm can be made in the superclass, affecting all subclasses. This makes maintenance easier and allows for the extension of the algorithm without modifying existing code in the subclasses.**Enforcement of Steps**: The Template Method Pattern enforces certain steps in the algorithm by defining them in the superclass. This can be useful in situations where certain steps must always be executed in a particular order.**Flexibility for Subclasses**: Subclasses can provide their own implementations for specific steps of the algorithm without changing the overall structure. This allows for customization and specialization while adhering to a common framework.**Reduced Code Duplication**: Since the common algorithm is defined in the superclass, there is less duplication of code across subclasses. This can lead to a more maintainable and less error-prone codebase.**Support for Hook Methods**: Template methods often include "hook" methods, which are empty or default implementations in the superclass. Subclasses can choose to override these methods to add or modify behavior, providing additional points of customization.**Simplified Client Code**: Clients using the template method interact with the algorithm through a common interface provided by the superclass. This simplifies client code by abstracting away the details of individual implementations in subclasses.

## Disadvantages of Template Method Design Patten in Java

While the Template Method Pattern offers several advantages, it also has some potential disadvantages also:

**Increased Complexity**: As the number of steps and variations in the algorithm increases, the template method can become more complex. This may make it harder to understand and maintain, especially when dealing with a large number of subclasses and potential variations.**Inflexibility in Run-Time Changes**: The template method defines the algorithm structure at compile time, making it less suitable for situations where the algorithm needs to change dynamically at runtime. If the steps of the algorithm need to be reconfigured during program execution, this pattern may not be the best choice.**Difficulty in Understanding the Flow**: In some cases, it might be challenging to understand the flow of control within the template method, especially if there are many subclasses and overridden methods. This can impact code readability.**Overhead of Inheritance**: The pattern relies heavily on inheritance, and using it excessively can lead to the "fragile base class" problem. Changes to the superclass can potentially affect all subclasses, and modifications to the template method might require changes in all derived classes.**Less Support for Code Composition**: The Template Method Pattern is more focused on inheritance and may not be as suitable for scenarios where code composition is preferred over inheritance. This can limit the ability to mix and match behavior dynamically.**Limited Support for Multiple Inheritance**: In languages that do not support multiple inheritance, the Template Method Pattern might be less flexible when it comes to incorporating behavior from multiple sources.**Potential for Violation of Liskov Substitution Principle**: If subclasses override certain steps in a way that violates the Liskov Substitution Principle, it can lead to unexpected behavior and may break the assumptions made by the template method.**Limited Runtime Polymorphism**: Since the structure of the algorithm is defined in the template method at compile time, there is limited support for runtime polymorphism. This may limit the ability to change algorithm behavior dynamically.

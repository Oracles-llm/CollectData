# Factory Method Design Pattern in Java

Last Updated :
12 Jul, 2025

It is a creational design pattern that talks about the creation of an object. The factory design pattern says to define an interface ( A java interface or an abstract class) for creating the object and let the subclasses decide which class to instantiate.

## What is the Factory Method Design Pattern?

Factory Method Design Pattern define an interface for creating an object, but let subclass decide which class to instantiate. Factory Method lets a class defer instantiation to subclass.


Below is the explanation of the above image:

- The factory method in the interface lets a class defer the instantiation to one or more concrete subclasses.
- Since these design patterns talk about the instantiation of an object they come under the category of creational design pattern.
- If we notice the name
**Factory method**, that means there is a method which is a factory, and in general, factories are involved with creational stuff and here with this, an object is being created. - It is one of the best ways to create an object where object creation logic is hidden from the client. Now Let's look at the implementation.

## When to use Factory Method Design Pattern?

Factory method design pattern can be used in java in following cases:

- A class cannot predict the type of objects it needs to create.
- A class wants its subclasses to specify the objects it creates.
- Classes delegate responsibility to one of multiple helper subclasses, and you aim to keep the information about which helper subclass is the delegate within a specific scope or location.

**Key Components of Factory Method Design Pattern**

Below are the main components of Factory Method Design Pattern in Java:

**Product**- It's an abstract class or interface that defines the common operations for the objects that the factory will create.
- Concrete Products are the actual classes that implement the Product interface, each representing a specific type of object to be created.

**Creator**- It's an abstract class or interface that declares the factory method.
- This method is responsible for creating Product objects, but it delegates the actual creation to subclasses.

**Concrete Creators**- These are subclasses of the Creator that implement the factory method.
- They decide which specific Concrete Product to create, often based on input parameters or configuration.

**Factory Method**- It's a method defined in the Creator class that is responsible for creating Product objects.
- It's typically declared as abstract in the Creator and implemented in the Concrete Creators.


## Factory Method Design Pattern Example

Let's understand factory method design pattern using an example. Below is the problem statement to understand it:

You are developing a software system for an e-commerce platform that deals with various types of products. Each product category (e.g., electronics, clothing, books) requires specific handling during creation. However, you want to decouple the client code from the concrete product creation logic to enhance flexibility and maintainability. Additionally, you want to allow for easy extension by adding new product types in the future without modifying existing code.


### 1. Solution using Abstract Class

The above problem can be solved using Factory Method Design Pattern:

Java
// Abstract Product Class
abstract class Product {
public abstract void display();
}
// Concrete Products
class ConcreteProductA extends Product {
@Override
public void display() {
System.out.println("This is Concrete Product A.");
}
}
class ConcreteProductB extends Product {
@Override
public void display() {
System.out.println("This is Concrete Product B.");
}
}
// Creator Abstract Class
abstract class Creator {
public abstract Product factoryMethod();
}
// Concrete Creators
class ConcreteCreatorA extends Creator {
@Override
public Product factoryMethod() {
return new ConcreteProductA();
}
}
class ConcreteCreatorB extends Creator {
@Override
public Product factoryMethod() {
return new ConcreteProductB();
}
}
// Client Code
public class FactoryMethodExample {
public static void main(String[] args) {
Creator creatorA = new ConcreteCreatorA();
Product productA = creatorA.factoryMethod();
productA.display();
Creator creatorB = new ConcreteCreatorB();
Product productB = creatorB.factoryMethod();
productB.display();
}
}


**Output**This is Concrete Product A.
This is Concrete Product B.

### 2. Solution using Interface

The above problem can be solved using Factory Method Design Pattern:

Java
// Product Interface
interface Product {
void display();
}
// Concrete Products
class ConcreteProductA implements Product {
@Override
public void display() {
System.out.println("This is Concrete Product A.");
}
}
class ConcreteProductB implements Product {
@Override
public void display() {
System.out.println("This is Concrete Product B.");
}
}
// Factory Interface
interface Factory {
Product factoryMethod();
}
// Concrete Factories
class ConcreteFactoryA implements Factory {
@Override
public Product factoryMethod() {
return new ConcreteProductA();
}
}
class ConcreteFactoryB implements Factory {
@Override
public Product factoryMethod() {
return new ConcreteProductB();
}
}
// Client Code
public class FactoryMethodExample {
public static void main(String[] args) {
Factory factoryA = new ConcreteFactoryA();
Product productA = factoryA.factoryMethod();
productA.display();
Factory factoryB = new ConcreteFactoryB();
Product productB = factoryB.factoryMethod();
productB.display();
}
}


**Output**This is Concrete Product A.
This is Concrete Product B.

## Use Cases of the Factory Method Design Pattern

Below are the use cases of factory method:

- JDBC uses factories to create connections and statements. Frameworks like Spring and Guice utilize factories for managing beans.
- Swing and JavaFX uses factories to produce UI components such as buttons and text fields, offering flexibility in design.
- Tools like Log4j and Logback employ factories to create loggers with various configurations, allowing for control over logging levels.
- Serialization frameworks use factories to generate objects from serialized data, accommodating different formats and versions.

## Advantages of Factory Method Design Pattern

Below are the main advantages of factory method:

- Separates object creation from client code, enhancing flexibility and maintainability since changes to creation don’t affect clients.
- New product types can be easily added without altering client code by simply creating new Concrete Creator subclasses.
- Simplifies unit testing by allowing mock product creation, enabling tests of various implementations without actual object dependencies.
- The factory method can be reused across different application parts, centralizing and streamlining object creation logic.
- Hides specific product classes from clients, reducing dependencies and improving maintainability.

## Disadvantages of Factory Method Design Pattern

Below are the main advantages of factory method:

- Adds more classes and interfaces, which can complicate understanding and maintenance, especially for newcomers.
- Polymorphism and dynamic binding may slightly affect performance, though this is usually minimal.
- Concrete creators remain closely linked to their products, necessitating changes across both when one is modified.
- Client code must be aware of concrete subclasses to make accurate factory calls.
- The pattern should be applied carefully to avoid unnecessary complexity; simple object creation may not need a factory.
- Testing the factory logic can be more complicated compared to simpler designs.

## Conclusion

So far we learned what is Factory method design pattern and how to implement it. I believe now we have a fair understanding of the advantage of this design mechanism. Factory methods pervade toolkits and frameworks.The preceding document example is a typical use in MacApp and ET++.

Further Read*:*** ****Java Design Patterns Tutorial**

Factory method design pattern in Java

### Explore

## Java Basics

## OOP & Interfaces

## Collections

## Exception Handling

## Java Advanced

## Practice Java
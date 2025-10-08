# Template Design Pattern in Java

Hey everyone 😄

Design patterns play a crucial role in software development, offering proven solutions to common problems. One such pattern is the Template Design Pattern, which enables the creation of flexible algorithms with a defined structure. In this blog post, we will dive deep into the Template Design Pattern, understanding its core concepts and exploring its practical applications.

## Template Design Pattern : Definition

*The Template Design Pattern is a behavioral design pattern that defines the basic structure of an algorithm in a superclass, while allowing subclasses to provide specific implementations of certain steps of the algorithm without modifying its overall structure. It promotes code reuse and enforces a common algorithm structure across multiple subclasses.*

Let’s have a basic example to understand all this . Suppose we want to buy a phone now we can buy it in two ways either we can go to a phone store or we can buy it offline . Now the steps involved in this complete process is selecting a phone , then after this your phone goes for packaging , then after it is being packed you will make payment and at last phone is delievered to you . So you can see that whether you buy phone online or offline the steps involved in buying are same although their implementation can be different . The important point is that the we can’t change the order of execution because we can’t buy a phone before selecting it .So in this case we can create a template method that will use different methods to buy the phone . Here we can provide base implementation for the steps that are same in buying phone , if subclasses want to override this method, they can .

## Implementation of Template Design Pattern

Let’s use our above example for implementation of template design pattern .

So our very first step is we are going to create a template class which is going to be abstract the reason of making it abstract is that it will be going to serve as blueprint for subclasses .

### PhoneOrder Template

`abstract public class PhoneOrderTemp`

{

final void createOrder()

{

//series of method invocation

selectProduct();

packProduct();

makePayment();

deliverProduct();

}

abstract void selectProduct();

abstract void makePayment();

void packProduct() {

System.out.println("paking the product");

}


abstract void deliverProduct();

}

Here we have made `createOrder()`

method as **final **because the order of execution of different methods present in it cannot be changed we cannot makePayment() before selecting the product . Then we have three different functions which are made as abstract as these three steps are same in online and offline shopping but there implementation is different so these are overridden accordingly in their respective subclasses and `packProduct()`

method is same for every subclass so instead of overriding it in subclasses we have declared it here .

Now the next step is to create our subclasses **OnlineStore and OfflineStore** that are going to extend **PhoneOrder template** .

### OnlineOrder Class

`public class OnlineStore extends PhoneOrderTemp`

{

@Override

void selectProduct()

{

System.out.println("selecting the product in online store");

}


@Override

void makePayment() {

System.out.println("making the payment in online store");

}


@Override

void deliverProduct() {

System.out.println("product delivered at home of the client");

}

}

### OfflineOrder Class

`public class OfflineStore extends PhoneOrderTemp`

{

public OfflineStore()

{


}

@Override

void selectProduct()

{

System.out.println("selecting the product in offline store");

}


@Override

void makePayment() {

System.out.println("making the payment in offline store");

}


@Override

void deliverProduct() {

System.out.println("product deliverd in hands in offline store");

}

}

And the last step is to create our Client Class from where our mobile phone is being ordered .

### Main Class

`public class Main {`

public static void main(String[] args) {

PhoneOrderTemp offlineStore = new OfflineStore();

//offlineStore.createOrder();


PhoneOrderTemp onlineStore = new OnlineStore();

onlineStore.createOrder();

}

}

So here we have made two PhoneOrderTemp class object one for OfflineStore and another for OnlineStore and called `createOrder()`

for each one of them .

### Output

So the above implementation clearly shows that how creating a single template for two different types of stores has helped us making our code simple and enhanced it’s reusability .

## Advantages of Template Design Pattern

**Encourages Code Reusability:**The Template Design Pattern promotes code reuse by providing a common template or algorithm structure in the abstract class. Subclasses can inherit this structure and customize specific steps without modifying the overall algorithm. This reduces duplication of code and improves maintainability.**Defines a Consistent Algorithm Structure:**The pattern enforces a consistent algorithm structure across multiple subclasses. The abstract class determines the sequence of steps and their relationships, ensuring that the algorithm follows a predefined pattern. This structure enhances code readability and comprehensibility.**Supports Open-Closed Principle:**The Template Design Pattern adheres to the Open-Closed Principle, which states that software entities should be open for extension but closed for modification. With the pattern, you can introduce new behavior by creating new subclasses that provide specific implementations for certain steps, without modifying the existing code.**Improves Code Maintainability:**The pattern enhances code maintainability by encapsulating the algorithm within the abstract class. Changes or updates to the algorithm can be made in a single place, rather than modifying multiple subclasses. This reduces the chances of introducing bugs and makes the code easier to understand and maintain.

### Real life examples

**Web Frameworks:**Web frameworks often utilize the Template Design Pattern to provide extensibility and customization options for developers. For instance, in a web application framework, the abstract class may define the overall structure of handling HTTP requests. Subclasses can then override specific methods to handle different types of requests, such as GET, POST, or DELETE. This allows developers to customize the behavior for handling specific requests while leveraging the common framework structure.**Automated Testing**: In automated testing frameworks, the Template Design Pattern can be used to define a common structure for different types of test cases. The abstract class would provide a template method that outlines the steps involved in executing a test, such as test setup, execution, and teardown. Subclasses can then override specific methods to implement test-specific logic and assertions. This pattern ensures a consistent testing approach across different test cases while allowing for customization based on specific test requirements.**Document Generation:**In document generation systems, the Template Design Pattern can be employed to create templates for generating different types of documents, such as invoices, reports, or contracts. The abstract class defines the overall structure of the document, including sections, headers, footers, and placeholders for dynamic data. Subclasses can then override specific methods to populate the placeholders with data and customize the appearance of the document. This pattern enables efficient document generation with consistent formatting and structure.**Game Development:**Game development often involves designing different types of game levels or scenarios. The Template Design Pattern can be utilized to create a template for level design. The abstract class would define the common structure and rules of the game level, such as spawning enemies, setting up obstacles, and defining win/lose conditions. Subclasses can then override specific methods to customize the level’s layout, enemy behavior, or unique features. This pattern facilitates the creation of diverse game levels while maintaining a consistent game structure.

## Conclusion

The Template Design Pattern is a powerful tool for creating algorithms with a defined structure while allowing for customization and extensibility. By using abstract classes and method overriding, developers can design flexible systems that can accommodate different requirements without sacrificing code maintainability. Understanding and applying this pattern will enable you to create elegant and reusable solutions to complex problems in software development.
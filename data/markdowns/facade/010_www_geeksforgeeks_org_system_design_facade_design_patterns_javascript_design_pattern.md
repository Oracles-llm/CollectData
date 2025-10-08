# Facade Design Pattern | JavaScript Design Pattern

Facade design pattern is a Structural design pattern that allows users to create a simple interface that hides the complex implementation details of the system making it easier to use. This pattern intends to create a simplified and unified interface for a set of interfaces hiding the implementation details making it less complex to use.



## Important Topics for the Facade Design Pattern in JavaScript Design Patterns

**Components of **the **Facade Design Pattern**

The components of the Facade design pattern include:

**Subsystem**: The Subsystem is a class or group of classes or interfaces that handles the entire complex logic and implementation.**Facade**: The Facade is the class or object that serves as an entry point to the Subsystem's implementation hiding the complex implementation details.**Client**: The Client interacts with the simplified Interface provided by Facade to perform operations without knowing the internal implementation details.

**Implementation of the Facade design pattern using JavaScript**

Let us understand the process of Implementing a Facade design pattern with an example:

**Step 1: Creation of Subsystem**

JavaScript
class SubsystemA {
method() {
console.log('This is a method of Subsystem-A');
}
}
class SubsystemB {
method() {
console.log('This is a method of Subsystem-B');
}
}
class SubsystemC {
method() {
console.log('This is a method of Subsystem-C');
}
}


**Explanation:**

In this step, I have created the Subsystem which contains three different classes namely `**SubsystemA`**, `**SubsystemB` **and` **SubsystemC` **along with the methods which console logs the information about which method they belong to.


**Step 2: Creation of the Facade **

JavaScript
class Facade {
constructor() {
this.subsystemA = new SubsystemA();
this.subsystemB = new SubsystemB();
this.subsystemC = new SubsystemC();
}
commonInterface() {
this.subsystemA.method();
this.subsystemB.method();
this.subsystemC.method();
}
}


**Explanation**:

In this step, I have created a `**Facade` **class that contains a constructor that intialies the objects of the three Substystems i.e. `**SubsystemA`**, `**SubsystemB`**, `**SubsystemC` **respectively. The `**Facade` **class is also responsible for providing a common interface. So, I created a method called `**commonInterface` **which hides the implementation details of subsystem and serves as a entry point.


**Step 3: Usage and the Client code**

JavaScript
const facade = new Facade();
facade.commonInterface();


**Explanation: **

In this step, I have created a `facade` object for the Facade class and calling the `commonInterface` method of the `Facade` class. Now, the actual process starts without need of knowing the implementation details.


**Below is the complete code for the Facade Design Pattern in Javascript:**

JavaScript
class SubsystemA {
method() {
console.log('This is a method of Subsystem-A');
}
}
class SubsystemB {
method() {
console.log('This is a method of Subsystem-B');
}
}
class SubsystemC {
method() {
console.log('This is a method of Subsystem-C');
}
}
class Facade {
constructor() {
this.subsystemA = new SubsystemA();
this.subsystemB = new SubsystemB();
this.subsystemC = new SubsystemC();
}
commonInterface() {
this.subsystemA.method();
this.subsystemB.method();
this.subsystemC.method();
}
}
const facade = new Facade();
facade.commonInterface();



**Output:**



**Below is the Diagrammatic Representation of the Facade Design Pattern:**

Let's visualize the above example using UML components.



**Advantages of the Facade Design Pattern in JavaScript Design Patterns**

**Simplified Interface: **The Facade design pattern uses a simplified interface which helps the client to interact with and perform operations without knowing the implementation details.**Abstraction and Encapsulation: **The Facade design pattern abstracts the internal implementation details and Encapsulates the Subsystem's logic.**Reduced Complexity:** As the Facade design pattern hides the implementation details for the client, there is reduced complexity and cognitive load on the client. so, the client can focus on the system's working rather than the subsystem's implementation.**Improved Maintainability: **As the common interface provided by the Facade class serves as an** **accessing entry point, it also acts as a centralized way to make changes to the subsystem, providing an easier way to maintain the subsystem.**Enhanced Reusability:** The simplified interface provided by the facade makes it easier to reuse the subsystem across multiple parts of the application or in different applications.

**Disadvantages of the Facade Design Pattern in JavaScript Design Patterns**

**Limited Functionality Exposure: **The Facade design pattern may restrict the client from accessing the functionality of certain operation of the subsystem without knowing the actual implementation details.**Potential Performance Overhead: **In some cases, Relying on the facade design pattern may lead** **to Performance overhead due to the additional layer of Abstraction.**Potential Design Misuse:** In some cases,** **taking the advantage of hiding the implementation details developers may hide up the poor implementation or design issues.


**State Design Pattern in C#**

In this article, I will discuss the **State Design Pattern in C#** with Examples. Please read our previous article discussing the **Chain of Responsibility Design Pattern in C# **with Examples. The State Design Pattern falls under the category of **Behavioral Design Pattern**. As part of this article, we will discuss the following pointers.

**What is a State Design Pattern?****Understanding the State Design Pattern with Multiple Real-Time Examples****Example of State Design Pattern in C#: ATM Machine and Vending Machine Implementation****Understanding the Class or UML Diagram of the State Design Pattern.****Advantages of State Design Pattern****When to use the State Design Pattern in Real-Time Applications?**

**What is a State Design Pattern?**

According to Gang of Four Definitions, the **State Design Pattern allows an object to alter its behavior when its internal state changes. **In simple words, we can say that the State Design Pattern allows an object to change its behavior depending on its current internal state. The State Design Pattern encapsulates varying behavior for the same object based on its internal state.

This pattern is useful when an object needs to go through several states, and its behavior differs for each state. Instead of having conditional statements throughout a class to handle state-specific behaviors, the State Design Pattern delegates this responsibility to individual state classes.

**Example to Understand State Design Pattern**

Please look at the following diagram to better understand the State Design Pattern. Here, you can see that on the left-hand side, we have the client; on the right-hand side, we have the Context object, and the context object internally maintains some states (such as State A and State B). As you can see in the diagram below, the Context object’s current state is State A. So, when the client requests the Context object, what the Context object will do is it will perform Operation A.

Let us say the internal state of the context object is changed to State B. Now, when the request is coming from the client, the context object will perform operation B as the current state is State B, as shown in the following diagram.


So, you need to remember that the behavior will be changed based on the current internal state of the context object. If this is not clear now, don’t worry; we will try to understand this with some real-time examples.

**Understanding State Design Pattern With Real-Time Example:**

Let us understand the State Design Pattern in C# with one real-time example. ATM machine behavior is the best example of the State Design Pattern. Please have a look at the following diagram.

Let’s say the ATM machine’s internal state is **Debit Card Not Inserted, **which means the ATM card is not inserted into the slot of the ATM Machine. Then what are all the operations you can do? The operations you can do are as follows.

- You can insert the debit card.
- You cannot eject the debit card as the debit card is not inserted into the ATM Machine.
- Again, you cannot enter the PIN and withdraw money. So, the only allowed operation is he can insert the debit card.

Suppose you inserted the debit card into the machine. So, the state of the ATM (i.e., Context Object) is changed to **Debit Card Inserted**. Then what are all the operations you can do? The operations you can do are as follows.

- You cannot insert the debit card as one is already inserted into the machine.
- It allows you to eject the Debit card.
- You can enter the PIN number and withdraw the money.

So, you must remember that if the state is Debit Card Not Inserted, it will allow you to perform certain operations. Changing the state to Debit Card Inserted will allow you to perform another set of operations. So, based on the internal state of the ATM machine, the behavior will be changed.

**How to Implement the State Design Pattern in C#?**

Here’s an overview of how you can implement the State Design Pattern in C#:

**State Interface:**This defines an interface for encapsulating the behavior associated with a particular context state.**Concrete State Classes:**These classes implement the State interface and provide the actual behavior specific to a state.**Context:**This class maintains an instance of a Concrete State subclass that defines the current state. The context delegates state-specific behavior to the current State object.**Client Code:**Modifies the state of the context.

**Implementation of State Design Pattern in C#:**

Let’s see the step-by-step procedure to implement the above-discussed example, i.e., the behavior of the ATM machine using the State Design Pattern in C#.

**Step1: Creating State Interface**

Create an interface named **IATMState.cs,** then copy and paste the following code. The IATMState interface defines the common methods for all the concrete state classes. It does not matter what the State of the Context object is. The following methods need to be implemented by the Concrete State classes. All the concrete state classes will implement this interface so that they are going to be interchangeable. Here, we created the interface with the required four operations.

namespace StateDesignPattern { // The State Interface declares methods that all Concrete State Classes should implement public interface IATMState { void InsertDebitCard(); void EjectDebitCard(); void EnterPin(); void WithdrawMoney(); } }

**Step2: Creating Concrete States**

These are going to be classes, and they implement the State Interface. Each Concrete State implements various behaviors associated with a State of the Context object. As the ATM has two states, we will create two concrete State Classes by implementing the ATMState interface and providing the implementations for the interface methods.

**DebitCardNotInsertedState:**

Create a class file named **DebitCardNotInsertedState.cs,** then copy and paste the following code. The following code is very straightforward. We implement all the methods of the IATMState interface. The following Concrete State class implements behavior when the ATM Machine, i.e., the context object State is DebitCardNotInsertedState.

using System; namespace StateDesignPattern { // Concrete States implement various behaviors, associated with a state of the Context Object. // The following Concrete State class implement behavior when the ATM State i.e. Context Object State is DebitCardNotInsertedState public class DebitCardNotInsertedState : IATMState { public void InsertDebitCard() { Console.WriteLine("DebitCard Inserted"); } public void EjectDebitCard() { Console.WriteLine("You cannot eject the Debit CardNo, as no Debit Card in ATM Machine slot"); } public void EnterPin() { Console.WriteLine("you cannot enter the pin, as No Debit Card in ATM Machine slot"); } public void WithdrawMoney() { Console.WriteLine("you cannot withdraw money, as No Debit Card in ATM Machine slot"); } } }

**DebitCardInsertedState:**

Next, create another class file named **DebitCardInsertedState.cs** and copy and paste the following code. In the below class, we implement all the methods of the ATMState interface. The following Concrete State class implements the behavior when the ATM State, i.e., the context object state, is DebitCardInsertedState.

using System; namespace StateDesignPattern { // Concrete States implement various behaviors, associated with a state of the Context Object. // The following Concrete State class implement behavior when the ATM State i.e. Context Objec State is DebitCardInsertedState public class DebitCardInsertedState : IATMState { public void InsertDebitCard() { Console.WriteLine("You cannot insert the Debit Card, as the Debit card is already there "); } public void EjectDebitCard() { Console.WriteLine("Debit Card is ejected"); } public void EnterPin() { Console.WriteLine("Pin number has been entered correctly"); } public void WithdrawMoney() { Console.WriteLine("Money has been withdrawn"); } } }

This way, you can create many concrete states per your business requirements. The Concrete States handles requests from the context object. Each concrete state provides its own implementation for a request. This way, when the context object state changes, its behavior will also change.

**Step3: Creating Context Object**

The Context is the class that can have many internal states. So, create a class file named **ATMMachine.cs** and copy and paste the following code. This class also implements the ATMState interface and provides the implementation for all the interface methods. Here, we create one variable to hold the Concrete State object. Then, we initialize that variable through the class constructor. Initially, the State of the ATM Machine is **DebitCardNotInsertedState,** so we initialize the variable with the **DebitCardNotInsertedState** state.

Further, if you notice, when we insert the debit card, we also change the state of the context object to **DebitCardInsertedState,** and again, when we eject the debit card, we also change the state of the context object to **DebitCardNotInsertedState**.

using System; namespace StateDesignPattern { // The Context Class defines the interface which is going to be used by the clients. // It also maintains a reference to an instance of a State subclass, which represents the current state of the Context. public class ATMMachine : IATMState { // A reference to the current state of the Context. public IATMState AtmMachineState = null; public ATMMachine() { //Initially the AtmMachineState will be DebitCardNotInsertedState AtmMachineState = new DebitCardNotInsertedState(); } // The Context Object allows changing the State of the object at runtime. public void InsertDebitCard() { //Inserting Debit card AtmMachineState.InsertDebitCard(); if (AtmMachineState is DebitCardNotInsertedState) { // Debit Card has been inserted so the internal state of the ATM Machine // has been changed to DebitCardInsertedState AtmMachineState = new DebitCardInsertedState(); Console.WriteLine($"ATM Machine internal state has been changed to : {AtmMachineState.GetType().Name}"); } } // The Context Object allows changing the State of the object at runtime. public void EjectDebitCard() { //Ejecting the Debit Card AtmMachineState.EjectDebitCard(); if (AtmMachineState is DebitCardInsertedState) { // Debit Card has been ejected so the internal state of the ATM Machine // has been changed to 'DebitCardNotInsertedState' AtmMachineState = new DebitCardNotInsertedState(); Console.WriteLine($"ATM Machine internal state has been Changed to : {AtmMachineState.GetType().Name}"); } } public void EnterPin() { //No need to Change the State, only perform the Operation AtmMachineState.EnterPin(); } public void WithdrawMoney() { //No need to Change the State, only perform the Operation AtmMachineState.WithdrawMoney(); } } }

**Note:** Internally, we are calling the methods of the respective state objects.

**Step4: Client**

The Main method of the Program class is going to be the Client. So, please modify the Main method of the Program class as shown below. Here, you can observe that the client only uses the context object. The context object performs different operations based on the current internal state.

using System; namespace StateDesignPattern { class Program { static void Main(string[] args) { // Initially ATM Machine in DebitCardNotInsertedState ATMMachine atmMachine = new ATMMachine(); Console.WriteLine("ATM Machine Current state : " + atmMachine.AtmMachineState.GetType().Name); Console.WriteLine(); atmMachine.EnterPin(); atmMachine.WithdrawMoney(); atmMachine.EjectDebitCard(); atmMachine.InsertDebitCard(); Console.WriteLine(); // Debit Card has been inserted so the internal state of the ATM Machine // has been changed to DebitCardInsertedState Console.WriteLine("ATM Machine Current state : " + atmMachine.AtmMachineState.GetType().Name); Console.WriteLine(); atmMachine.EnterPin(); atmMachine.WithdrawMoney(); atmMachine.InsertDebitCard(); atmMachine.EjectDebitCard(); Console.WriteLine(""); // Debit Card has been ejected so the internal state of the ATM Machine // has been changed to DebitCardNotInsertedState Console.WriteLine("ATM Machine Current state : " + atmMachine.AtmMachineState.GetType().Name); Console.Read(); } } }

**Output:**

**Use Cases:**

- When an object’s behavior depends on its state, it must be able to change its behavior at runtime based on internal state changes.
- In scenarios where complex conditional logic based on object state is required. The State Pattern can provide a cleaner solution.

**State Design Pattern UML or Class Diagram:**

Let us understand the Class Diagram or UML Diagram of the State Design Pattern and the components involved. Please have a look at the following image.

As you can see in the above image, the State Design Pattern consists of three components. They are as follows:

**State:**This is going to be an interface that is used by the Context object. This interface defines the behaviors that the child classes will implement in their own way. In our example, it is going to be the IATMState interface.**ConcreteStateA/B/C:**These will be concrete classes that implement the State interface and provide the functionality the Context object will use. Each concrete state class provides behavior that applies to a single state of the Context object. In our example, it is the DebitCardNotInsertedState and DebitCardInsertedState classes.**Context:**This class will hold a concrete state object that provides the behavior according to its current state. This class is going to be used by the client. In our example, it is the ATMMachine class.

**State Design Pattern Real-Time Example: Vending Machine:**

The Vending Machine is one of the best Real-Time Examples of the State Design Pattern. For example, you want to buy one product (Pepsi) from the vending machine. Then what you have to do is, you have to select the product which is nothing but Pepsi, and then you have to insert the money. Once you do that, then the Vending Machine will dispense the product. This is how the Vending Machine works in real time.

Please have a look at the following diagram. Let us assume that the internal state of the Vending machine is **Money Not Inserted** **and Product Not Selected**. Then, what operations can you perform on the Vending Machine? You can select the product and insert the money, but you cannot get the product from the vending machine.

Once you select the product and insert the money, the state of the Vending machine changes from **Money Not Inserted and Product Not Selected** to **Money Inserted and Product Selected **State. Once the state changes to Money Inserted and Product Selected, then what the Vending will do is it will give you the product as well as the balance amount, if any.


This is how the Vending Machine works, and based on the internal state, the behavior of the vending machine will change.

**Implementation of Vending Machine using State Design Pattern in C#:**

Let’s see the step-by-step procedure to implement the above-discussed example, i.e., the behavior of the Vending Machine using the State Design Pattern in C#.

**Step1: Creating the State Interface**

Create an interface with the **IVendingMachineState.cs** and copy and paste the following code. Here, we created the interface with two methods, i.e., SelectProductAndInsertMoney and DispenseProduct. These methods are going to be implemented by the child classes according to the state of the Vending Machine.

namespace StateDesignPatternExample { // The State interface defines the common methods for all the concrete state classes. // The State Interface declares methods that all Concrete State Classes should implement public interface IVendingMachineState { void SelectProductAndInsertMoney(int amount, string productName); void DispenseProduct(); } }

**Step2: Creating the Concrete States**

Concrete States implement various behaviors associated with a state of the Context object. The Vending machine has two internal states, i.e., NoMoneyState and HasMoneyState. So, we need to create two concrete state classes by implementing the **IVendingMachineState** interface and providing the implementations for the interface methods.

**NoMoneyState:**

Create a class file named **NoMoneyState.cs** and copy and paste the following code. The following class is very straightforward. Here, we implement **IVendingMachineState** interface methods. The following Concrete State class implements behavior when the Vending Machine State is NoMoneyState.

using System; namespace StateDesignPatternExample { // Concrete State A // Concrete States implement various behaviors, associated with a state of the Context. // The following Concrete State class implement behavior when the Vending Machine State is NoMoneyState public class NoMoneyState : IVendingMachineState { public void DispenseProduct() { Console.WriteLine("Vending Machine cannot dispense product because money is not inserted and product is not selected"); } public void SelectProductAndInsertMoney(int amount, string productName) { Console.WriteLine(amount + "Rs has been inserted and " + productName + " has been selected"); } } }

**HasMoneyState**

Create a class file named **HasMoneyState.cs** and copy and paste the following code. This class also implements the **IVendingMachineState** interface and provides the implementation for the two methods. The following Concrete State class implements behavior when the Vending Machine State is HasMoneyState.

using System; namespace StateDesignPatternExample { // Concrete State B // Concrete States implement various behaviors, associated with a state of the Context. // The following Concrete State class implement behavior when the Vending Machine State is HasMoneyState public class HasMoneyState : IVendingMachineState { public void DispenseProduct() { Console.WriteLine("Vending Machine Dispensed the Product"); } public void SelectProductAndInsertMoney(int amount, string productName) { Console.WriteLine("Already Vending machine has money and product selected, So wait till it finish the current dispensing process"); } } }

**Note:** This way, we can create many concrete states per our business requirements. The Concrete States handles requests from the context. Each concrete state provides its own implementation for a request. When the context object state changes, its behavior will also change.

**Step3: Creating the Context object**

As we already discussed in our previous article, the Context object can have many internal states. So, create a class file named **VendingMachine.cs** and copy and paste the following code. This class also implements the IVendingMachineState interface and provides the implementation for the two interface methods. Here, we create one variable, i.e., vendingMachineState, to hold the Concrete State object. Then, we initialize that variable, i.e., vendingMachineState, through the constructor. As we know, initially, the State of the Vending Machine is **NoMoneyState,** so we initialize the variable, i.e., vendingMachineState, with the NoMoneyStatestate within the constructor.

Further, if you notice, when we Select Product And Insert Money, we also change the state of the context object, i.e., Vending Machine to **HasMoneyState,** and again when the Vending Machine Dispense Product and return the balance money, if any, we also change the state of the context object, i.e., Vending Machine to **NoMoneyState**. The following example code is self-explained, so please go through the comment lines for a better understanding.

using System; namespace StateDesignPatternExample { // The Context Class defines the interface which is going to be used by the clients. // It also maintains a reference to an instance of a State subclass, which represents the current state of the Context. public class VendingMachine : IVendingMachineState { //Creating a variable to maintain the internal state public IVendingMachineState VendingMachineState { get; set; } //Initially the vending machine has NoMoneyState public VendingMachine() { VendingMachineState = new NoMoneyState(); } // The Context Object allows changing the State of the object at runtime. public void SelectProductAndInsertMoney(int amount, string productName) { VendingMachineState.SelectProductAndInsertMoney(amount, productName); // Money has been inserted so Vending Machine's internal state changed to HasMoneyState if (VendingMachineState is NoMoneyState) { VendingMachineState = new HasMoneyState(); Console.WriteLine($"VendingMachine internal state has been moved to {VendingMachineState.GetType().Name}"); } } // The Context Object allows changing the State of the object at runtime. public void DispenseProduct() { VendingMachineState.DispenseProduct(); // Product has been dispensed so vending Machine changed the internal state to NoMoneyState if (VendingMachineState is HasMoneyState) { VendingMachineState = new NoMoneyState(); Console.WriteLine($"VendingMachine internal state has been moved to : {VendingMachineState.GetType().Name}"); } } } }

**Step4: Client**

The Main Method of the Program class will be the Client in our example. So, please modify the Main method of the Program class as shown below. Here, you can observe that the client only uses the context object.

using System; using System.Collections.Generic; using System.Linq; using System.Text; using System.Threading.Tasks; namespace StateDesignPatternExample { class Program { static void Main(string[] args) { // Initially Vending Machine will be NoMoneyState VendingMachine vendingMachine = new VendingMachine(); Console.WriteLine($"Current VendingMachine State : {vendingMachine.VendingMachineState.GetType().Name}\n"); vendingMachine.DispenseProduct(); vendingMachine.SelectProductAndInsertMoney(50, "Pepsi"); // Money has been inserted so vending Machine internal state changed to HasMoneyState Console.WriteLine($"\nCurrent VendingMachine State : {vendingMachine.VendingMachineState.GetType().Name}\n"); vendingMachine.SelectProductAndInsertMoney(50, "Fanta"); vendingMachine.DispenseProduct(); // Product has been dispensed so vending Machine internal state changed to NoMoneyState Console.WriteLine($"\nCurrent VendingMachine State : {vendingMachine.VendingMachineState.GetType().Name}"); Console.Read(); } } }

**Output:**

**Advantages of State Design Pattern:**

**Encapsulation of State-Based Behavior:**State-specific logic is encapsulated in state classes.**Easy to Add New States:**Introducing new states doesn’t require changing the context or other states.**Eliminates Conditional Statements:**It helps to eliminate conditional statements for behavior changes based on the state.**Maintainability and Flexibility:**The state pattern makes it easier to maintain and extend state-based behavior.**Dynamic Behavior Change:**The context can change its behavior at runtime depending on its state.

**When to Use State Design Pattern in C#?**

The State Design Pattern in C# is particularly useful in scenarios where:

**Object Behavior Depends on Its State:**When the behavior of an object changes depending on its internal state, and you want to avoid large conditional statements (like switch/case or if/else) in your code. The State pattern allows you to encapsulate the behavior associated with each state in separate classes.**Complex State Logic:**In cases where an object’s state has complex logic that involves many different states and transitions between those states. The State pattern helps organize this logic by separating it into distinct classes.**State-Dependent Transitions:**When the rules for transitioning from one state to another are complex and need to be centralized. The State pattern allows each state object to control the transitions to other states.**Maintaining Clean Code:**If you want to maintain clean code by avoiding tight coupling and minimizing the impact of changes in state logic. Each state can be managed and modified independently with the State pattern.**Large Conditional Blocks Handling:**In situations where an object’s behavior includes many conditional blocks that depend on the object’s state. The State pattern allows you to remove these conditionals by encapsulating the behavior within state objects.**Runtime State Change:**If the state of an object needs to change at runtime and you want the object’s behavior to change accordingly without client intervention.**Ease of Extending States and Behaviors:**When you anticipate that new states might be added in the future. The State pattern makes it easier to extend states and behaviors without modifying existing code, adhering to the Open/Closed Principle.

In the next article, I will discuss the **State Design Pattern in Real-time Examples in C#**. In this article, I try to explain the **State Design Pattern in C#** with an example. I hope you enjoy this State Design Pattern in C# with Examples article.
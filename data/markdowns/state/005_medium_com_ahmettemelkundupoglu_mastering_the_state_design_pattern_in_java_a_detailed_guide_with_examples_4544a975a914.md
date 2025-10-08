# Mastering the State Design Pattern in Java: A Detailed Guide with Examples

The **State Design Pattern** is one of the most useful behavioral patterns defined in the **Gang of Four (GoF)** design patterns. It allows an object to alter its behavior when its internal state changes, making the object appear to change its class. This pattern helps in avoiding complex conditional logic that would otherwise be scattered across the code.

In this article, we’ll take a deep dive into the **State Design Pattern**, covering its key concepts, advantages, and real-world Java examples to showcase how it simplifies state-driven logic in your code.

## What is the State Design Pattern?

The **State Pattern** allows an object to change its behavior based on its current state. Instead of using large if-else or switch-case blocks to handle different states, the behavior is encapsulated into **state classes**. The context delegates behavior to the current state object.

## Key Concepts of the State Pattern:

**State Interface:**Defines the common behavior for all states.**Concrete States:**Implement the behavior for each state.**Context:**Maintains a reference to the current state and delegates requests to the current state object.

## When to Use the State Design Pattern:

- When an object’s behavior depends on its state.
- When you have a lot of if-else or switch statements that change behavior based on state.
- When the state-specific behavior changes frequently or needs to be easily extendable.

## Real-Life Example: Traffic Light System

Let’s take a **traffic light system** as an example. A traffic light can be in one of three states:

**Red Light:**Cars must stop.**Green Light:**Cars can go.**Yellow Light:**Cars should prepare to stop.

## Step 1: Define the State Interface

The TrafficLightState interface defines the common behavior for all traffic light states.

`interface TrafficLightState {`

void handleRequest(TrafficLightContext context);

}

## Step 2: Implement Concrete States

### 1. Red Light State

`class RedLightState implements TrafficLightState {`

@Override

public void handleRequest(TrafficLightContext context) {

System.out.println("Red Light: Cars must stop.");

context.setState(new GreenLightState()); // Change to Green after Red

}

}

### 2. Green Light State

`class GreenLightState implements TrafficLightState {`

@Override

public void handleRequest(TrafficLightContext context) {

System.out.println("Green Light: Cars can go.");

context.setState(new YellowLightState()); // Change to Yellow after Green

}

}

## Step 3: Create the Context Class

The TrafficLightContext class holds a reference to the current state and delegates the request to it.

`class TrafficLightContext {`

private TrafficLightState currentState;


public TrafficLightContext() {

currentState = new RedLightState(); // Default initial state

}


public void setState(TrafficLightState state) {

this.currentState = state;

}


public void changeLight() {

currentState.handleRequest(this);

}

}

## Step 4: Client Code

`public class StatePatternDemo {`

public static void main(String[] args) {

TrafficLightContext trafficLight = new TrafficLightContext();


for (int i = 0; i < 6; i++) { // Change the light multiple times

trafficLight.changeLight();

System.out.println();

}

}

}

Output:

`Red Light: Cars must stop.`


Green Light: Cars can go.


Yellow Light: Cars should prepare to stop.


Red Light: Cars must stop.


Green Light: Cars can go.


Yellow Light: Cars should prepare to stop.

In this example, the OrderContext transitions through different states (Placed, Shipped, Delivered, Cancelled). The behavior in each state is encapsulated, ensuring that state transitions and behaviors are easy to maintain and extend.

## 2. Real-World Example: Order State in an E-Commerce System

In an e-commerce system, an order can go through several states: **Placed, Shipped, Delivered, Cancelled**. Each state has specific actions that can be performed.

## Step 1: Define the State Interface

`interface OrderState {`

void next(OrderContext context);

void cancel(OrderContext context);

}

## Step 2: Implement Concrete States

### 1. Order Placed State

`class OrderPlacedState implements OrderState {`

@Override

public void next(OrderContext context) {

System.out.println("Order has been placed. Moving to Shipped state.");

context.setState(new OrderShippedState());

}


@Override

public void cancel(OrderContext context) {

System.out.println("Order has been cancelled.");

context.setState(new OrderCancelledState());

}

}

### 2. Order Shipped State

`class OrderShippedState implements OrderState {`

@Override

public void next(OrderContext context) {

System.out.println("Order has been shipped. Moving to Delivered state.");

context.setState(new OrderDeliveredState());

}


@Override

public void cancel(OrderContext context) {

System.out.println("Cannot cancel. Order has already been shipped.");

}

}

### 3. Order Delivered State

`class OrderDeliveredState implements OrderState {`

@Override

public void next(OrderContext context) {

System.out.println("Order is already delivered.");

}


@Override

public void cancel(OrderContext context) {

System.out.println("Cannot cancel. Order is already delivered.");

}

}

### 4. Order Cancelled State

`class OrderCancelledState implements OrderState {`

@Override

public void next(OrderContext context) {

System.out.println("Cannot proceed. Order is cancelled.");

}


@Override

public void cancel(OrderContext context) {

System.out.println("Order is already cancelled.");

}

}

## Step 3: Create the Context Class

`class OrderContext {`

private OrderState currentState;


public OrderContext() {

currentState = new OrderPlacedState(); // Default state

}


public void setState(OrderState state) {

this.currentState = state;

}


public void proceedToNext() {

currentState.next(this);

}


public void cancelOrder() {

currentState.cancel(this);

}

}

## Step 4: Client Code

`public class ECommerceStatePatternDemo {`

public static void main(String[] args) {

OrderContext order = new OrderContext();


System.out.println("Order Workflow:");

order.proceedToNext(); // Move to Shipped

order.proceedToNext(); // Move to Delivered

order.cancelOrder(); // Try to cancel after delivery


System.out.println("\nNew Order Workflow:");

OrderContext newOrder = new OrderContext();

newOrder.cancelOrder(); // Cancel immediately after placement

}

}

Output:

`Order Workflow:`

Order has been placed. Moving to Shipped state.

Order has been shipped. Moving to Delivered state.

Cannot cancel. Order is already delivered.


New Order Workflow:

Order has been cancelled.

In this example, the OrderContext transitions through different states (Placed, Shipped, Delivered, Cancelled). The behavior in each state is encapsulated, ensuring that state transitions and behaviors are easy to maintain and extend.

## Advantages of the State Design Pattern:

**Improves Code Maintainability:**State-specific behavior is encapsulated in separate classes, making it easy to extend or modify.**Eliminates Complex Conditional Logic:**Avoids long if-else or switch statements for statements for managing state-based behavior.**Follows Open/Closed Principle:**New states can be added without modifying existing code.**Simplifies State Transitions:**State transitions are handled by the state objects themselves.

## Disadvantages of the State Design Pattern:

**Increased Number of Classes:**Each state requires a new class, which can lead to a large number of classes in complex systems.**Memory Overhead:**Since each state is represented as a separate object, there may be some memory overhead.

## Conclusion:

The **State Design Pattern** is a powerful tool for managing complex state-dependent behavior in Java applications. By encapsulating state-specific logic in separate classes, the pattern makes your code cleaner, easier to understand, and more maintainable. Whether you’re implementing a **traffic light system**, **order management system**, or **game character states**, the **State Pattern** helps you create systems that are flexible and adhere to good software design principles.
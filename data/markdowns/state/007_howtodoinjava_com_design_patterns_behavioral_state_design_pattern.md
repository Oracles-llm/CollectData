The **state pattern** is a **behavioral** design pattern. According to GoF definition, a state **allows an object to alter its behavior when its internal state changes**. The object will appear to change its class.

It can be drawn from above definition that there shall be a **separate concrete class per possible state of an object**. Each concrete state object will have logic to accept or reject a state transition request based on it’s present state and context information passed to it as method arguments.

## 1. When to use state pattern

In any application, when we are dealing with **an object which can be in different states during it’s life-cycle** and how it processes incoming requests (or make state transitions) based on it’s present state – we can use the state pattern.

If we do not use the state pattern in such case, we will end up having lots of `if-else`

statements which make the code base ugly, unnecessarily complex and hard to maintain. State pattern allows the objects to behave differently based on the current state, and we can define state-specific behaviors within different classes.

The state pattern solves problems where an object should change its behavior when its internal state changes. Also, adding new states should not affect the behavior of existing states.


## 2. Real world example of state pattern

- To make things simple, let’s visualize a
**TV box**operated with remote controller. We can change the state of TV by pressing buttons on remote. But the state of TV will change or not, it depends on the current state of the TV. If TV is ON, we can switch it OFF, mute or change aspects and source. But if TV is OFF, nothing will happen when we press remote buttons.For a switched OFF TV. only possible next state can be switch ON.

- State patterns are used to implement state machine implementations in complex applications.
- Another example can be of
**Java thread**states. A thread can be one of its five states during it’s life cycle. It’s next state can be determined only after getting it’s current state. e.g. we can not start a stopped thread or we cannot a make a thread wait, until it has started running.

## 3. State Design Pattern Implementation

Define separate (state) objects that encapsulate state-specific behavior for each state. That is, define an interface (state) for performing state-specific behavior, and define classes that implement the interface for each state.

The State pattern does not specify where the state transitions will be defined. The choices are two: the “context” object, or each individual State derived class.

#### 3.1. Architecture

#### 3.2. Design participants

**State**– The interface define operations which each state must handle.**Concrete States**– The classes which contain the state specific behavior.**Context**– Defines an interface to client to interact. It maintains references to concrete state object which may be used to define current state of object. It delegates state-specific behavior to different State objects.

## 4. State Pattern Example

In this example, we are simulating courier delivery system where packages can be in different states during transitions.

public interface PackageState { public void updateState(DeliveryContext ctx); }

public class Acknowledged implements PackageState { //Singleton private static Acknowledged instance = new Acknowledged(); private Acknowledged() {} public static Acknowledged instance() { return instance; } //Business logic and state transition @Override public void updateState(DeliveryContext ctx) { System.out.println("Package is acknowledged !!"); ctx.setCurrentState(Shipped.instance()); } }

public class Shipped implements PackageState { //Singleton private static Shipped instance = new Shipped(); private Shipped() {} public static Shipped instance() { return instance; } //Business logic and state transition @Override public void updateState(DeliveryContext ctx) { System.out.println("Package is shipped !!"); ctx.setCurrentState(InTransition.instance()); } }

public class InTransition implements PackageState { //Singleton private static InTransition instance = new InTransition(); private InTransition() {} public static InTransition instance() { return instance; } //Business logic and state transition @Override public void updateState(DeliveryContext ctx) { System.out.println("Package is in transition !!"); ctx.setCurrentState(OutForDelivery.instance()); } }

public class OutForDelivery implements PackageState { //Singleton private static OutForDelivery instance = new OutForDelivery(); private OutForDelivery() {} public static OutForDelivery instance() { return instance; } //Business logic and state transition @Override public void updateState(DeliveryContext ctx) { System.out.println("Package is out of delivery !!"); ctx.setCurrentState(Delivered.instance()); } }

public class Delivered implements PackageState { //Singleton private static Deliveredinstance = new Delivered(); private Delivered() {} public static Deliveredinstance() { return instance; } //Business logic @Override public void updateState(DeliveryContext ctx) { System.out.println("Package is delivered!!"); } }

**The Context**

public class DeliveryContext { private PackageState currentState; private String packageId; public DeliveryContext(PackageState currentState, String packageId) { super(); this.currentState = currentState; this.packageId = packageId; if(currentState == null) { this.currentState = Acknowledged.instance(); } } public PackageState getCurrentState() { return currentState; } public void setCurrentState(PackageState currentState) { this.currentState = currentState; } public String getPackageId() { return packageId; } public void setPackageId(String packageId) { this.packageId = packageId; } public void update() { currentState.updateState(this); } }

Now test the code.

public class Main { public static void main(String[] args) { DeliveryContext ctx = new DeliveryContext(null, "Test123"); ctx.update(); ctx.update(); ctx.update(); ctx.update(); ctx.update(); } }

Program Output.

Package is acknowledged !! Package is shipped !! Package is in transition !! Package is out of delivery !! Package is delivered !!

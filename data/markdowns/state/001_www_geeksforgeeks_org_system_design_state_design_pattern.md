State Design Pattern is a behavioral design pattern that allows an object to change its behavior when its internal state changes. This pattern is particularly useful when an object's behavior depends on its state, and the state can change during the object's lifecycle.

For example, a vending machine responds differently based on state (item selected, money paid and item dispensed).



Note: This pattern focuses on managing state transitions and coordinating state-specific behaviors.


## Real Life Software Examples

- Media Player behaves differently in each play, pause and stop states. The internal state determines what action happens when a button is pressed. For example, in play state, it responds to pause and stop.
- Document (Google Docs and MS Word) respond differently according to the current status of the document. In Draft: only the author can edit. In Review: reviewers can comment, but not edit and in Published: it becomes read-only.

## Components of State Design Pattern

**Context** – Maintains a reference to the current state, delegates behavior to it, and provides an interface for clients.**State Interface/Base Class** – Defines common methods for all states, allowing Context to work with them without knowing concrete types.**Concrete States** – Implement the State interface, encapsulating behavior for specific states and defining Context’s actions in those states.

## When to use the State Design Pattern

The State design pattern is beneficial when you encounter situations with objects whose behavior changes dynamically based on their internal state. Here are some key indicators:

**Multiple states with distinct behaviors:** If your object exists in several states (e.g., On/Off, Open/Closed, Started/Stopped), and each state dictates unique behaviors, the State pattern can encapsulate this logic effectively.**Complex conditional logic:** When conditional statements (if-else or switch-case) become extensive and complex within your object, the State pattern helps organize and separate state-specific behavior into individual classes, enhancing readability and maintainability.**Frequent state changes:** If your object transitions between states frequently, the State pattern provides a clear mechanism for managing these transitions and their associated actions.**Adding new states easily:** If you anticipate adding new states in the future, the State pattern facilitates this by allowing you to create new state classes without affecting existing ones.

## When not to use the State Design Pattern

While the State pattern offers advantages, it's not always the best solution. Here are some cases where it might be overkill:

**Few states with simple behavior:** If your object has only a few simple states with minimal behavioral differences, the overhead of the State pattern outweighs its benefits. In such cases, simpler conditional logic within the object itself might suffice.**Performance-critical scenarios:** The pattern can introduce additional object creation and method calls, potentially impacting performance. If performance is paramount, a different approach might be more suitable.

## How to implement State Design Pattern?

Below are the steps to implement the State Design Pattern:

**Purpose** – Lets an object change behavior based on its state, avoiding complex conditionals by using separate state classes.**Context** – The object whose behavior varies (e.g., media player: Playing, Paused, Stopped).**State Interface** – Defines common actions all states must implement.**Concrete States** – Implement the interface, each defining behavior for a specific state.**Context Class** – Holds the current state and delegates actions to it, enabling dynamic state switching at runtime.

Let's understand the component with the help of Diagram:

## Communication between the components

In the State design pattern, the communication between the components typically follows these steps:

**Client Interaction** – Client calls methods on the Context.**Delegation** – Context forwards the request to its current State.**State Behavior** – The State executes behavior for that state.**Transition Check** – Logic may trigger a state change.**State Update** – Context updates its reference to the new State.**Repeat** – Client keeps interacting, and behavior adapts per state

This communication flow ensures that the Context and State objects work together seamlessly to achieve dynamic behavior changes based on the internal state of the Context. The Context manages the state and delegates behavior to the current State object, while the State objects encapsulate state-specific behavior and handle transitions between states as necessary.


## Example of State Design Pattern

**Problem Statement:**

Imagine a vending machine that sells various products. The vending machine needs to manage different states such as ready to serve, waiting for product selection, processing payment, and handling out-of-stock situations. Design a system that models the behavior of this vending machine efficiently.


**How State Design Pattern will help while building this system:**

**Modeling States** – Each state (Ready, Product Selected, Payment Pending, Out of Stock) is represented as a separate class, keeping the code organized.**Encapsulation** – Each state class defines its own behavior (e.g., ReadyState handles selection, PaymentPendingState handles payments), simplifying complex logic.**Dynamic Transitions** – The machine moves between states (e.g., Ready → Product Selected → Payment Pending) based on user actions.**Reusability** – State classes can be reused across different vending machine implementations, reducing duplication.**Maintainability & Flexibility** – New states or changes can be added without impacting other parts, making the system easier to extend and maintain.

**User Interaction with the System**

User interactions with the vending machine trigger state transitions. For example, when a user inserts money, the vending machine transitions from the "ReadyState" to the "PaymentPendingState." Similarly, when a product is selected, the vending machine transitions to the "ProductSelectedState." If a product is out of stock, the vending machine transitions to the "OutOfStockState."

### Below is the code of above problem statement using State Design Pattern:

Let’s break down into the component wise code:

**1. Context(VendingMachineContext)**

The context is responsible for maintaining the current state of the vending machine and delegating state-specific behavior to the appropriate state object.

C++
public class VendingMachineContext {
private VendingMachineState state;
public void setState(VendingMachineState state) {
this.state = state;
}
public void request() {
state.handleRequest();
}
}


Java
public class VendingMachineContext {
private VendingMachineState state;
public void setState(VendingMachineState state) {
this.state = state;
}
public void request() {
state.handleRequest();
}
}


Python
class VendingMachineContext:
def __init__(self):
self._state = None
def set_state(self, state):
self._state = state
def request(self):
self._state.handle_request()


JavaScript
class VendingMachineContext {
#private VendingMachineState state;
constructor() {
this.state = null;
}
setState(state) {
this.state = state;
}
request() {
this.state.handleRequest();
}
}


**2. State Interface (VendingMachineState)**

This interface defines the contract that all concrete state classes must implement. It typically contains a method or methods representing the behavior associated with each state of the vending machine.

C++
public interface VendingMachineState {
void handleRequest();
}


Java
/* Public interface VendingMachineState */
public interface VendingMachineState {
void handleRequest();
}


Python
""" Public interface VendingMachineState """
from abc import ABC, abstractmethod
class VendingMachineState(ABC):
@abstractmethod
def handleRequest(self):
pass


JavaScript
/* Public interface VendingMachineState */
class VendingMachineState {
handleRequest() {
// Handle request logic here
}
}


**3. Concrete States (Specific Vending Machine States)**

Concrete state classes represent specific states of the vending machine, such as "ReadyState," "ProductSelectedState," and "OutOfStockState." Each concrete state class implements the behavior associated with its respective state, like allowing product selection, processing payment, or displaying an out-of-stock message.

C++
#include <iostream>
#include <string>
using namespace std;
class VendingMachineState {
public:
virtual void handleRequest() = 0;
};
class ReadyState : public VendingMachineState {
public:
void handleRequest() override {
cout << "Ready state: Please select a product." << endl;
}
};
class ProductSelectedState : public VendingMachineState {
public:
void handleRequest() override {
cout << "Product selected state: Processing payment." << endl;
}
};
class PaymentPendingState : public VendingMachineState {
public:
void handleRequest() override {
cout << "Payment pending state: Dispensing product." << endl;
}
};
class OutOfStockState : public VendingMachineState {
public:
void handleRequest() override {
cout << "Out of stock state: Product unavailable. Please select another product." << endl;
}
};


Java
import java.util.ArrayList;
// VendingMachineState interface
interface VendingMachineState {
void handleRequest();
}
// ReadyState class
class ReadyState implements VendingMachineState {
@Override
public void handleRequest() {
System.out.println("Ready state: Please select a product.");
}
}
// ProductSelectedState class
class ProductSelectedState implements VendingMachineState {
@Override
public void handleRequest() {
System.out.println("Product selected state: Processing payment.");
}
}
// PaymentPendingState class
class PaymentPendingState implements VendingMachineState {
@Override
public void handleRequest() {
System.out.println("Payment pending state: Dispensing product.");
}
}
// OutOfStockState class
class OutOfStockState implements VendingMachineState {
@Override
public void handleRequest() {
System.out.println("Out of stock state: Product unavailable. Please select another product.");
}
}
// VendingMachine class
class VendingMachine {
private VendingMachineState currentState;
public VendingMachine() {
this.currentState = new ReadyState();
}
public void setState(VendingMachineState state) {
this.currentState = state;
}
public void handleRequest() {
currentState.handleRequest();
}
}
// Main class
public class Main {
public static void main(String[] args) {
VendingMachine vendingMachine = new VendingMachine();
vendingMachine.handleRequest();
vendingMachine.setState(new ProductSelectedState());
vendingMachine.handleRequest();
vendingMachine.setState(new PaymentPendingState());
vendingMachine.handleRequest();
vendingMachine.setState(new OutOfStockState());
vendingMachine.handleRequest();
}
}


Python
from abc import ABC, abstractmethod
class VendingMachineState(ABC):
@abstractmethod
def handle_request(self):
pass
class ReadyState(VendingMachineState):
def handle_request(self):
print('Ready state: Please select a product.')
class ProductSelectedState(VendingMachineState):
def handle_request(self):
print('Product selected state: Processing payment.')
class PaymentPendingState(VendingMachineState):
def handle_request(self):
print('Payment pending state: Dispensing product.')
class OutOfStockState(VendingMachineState):
def handle_request(self):
print('Out of stock state: Product unavailable. Please select another product.')


JavaScript
class VendingMachineState {}
class ReadyState extends VendingMachineState {
handleRequest() {
console.log('Ready state: Please select a product.');
}
}
class ProductSelectedState extends VendingMachineState {
handleRequest() {
console.log('Product selected state: Processing payment.');
}
}
class PaymentPendingState extends VendingMachineState {
handleRequest() {
console.log('Payment pending state: Dispensing product.');
}
}
class OutOfStockState extends VendingMachineState {
handleRequest() {
console.log('Out of stock state: Product unavailable. Please select another product.');
}
}


### Complete code for the above example

Below is the complete code for the above example:

C++
interface VendingMachineState {
void handleRequest();
}
class ReadyState implements VendingMachineState {
@Override
public void handleRequest() {
System.out.println("Ready state: Please select a product.");
}
}
class ProductSelectedState implements VendingMachineState {
@Override
public void handleRequest() {
System.out.println("Product selected state: Processing payment.");
}
}
class PaymentPendingState implements VendingMachineState {
@Override
public void handleRequest() {
System.out.println("Payment pending state: Dispensing product.");
}
}
class OutOfStockState implements VendingMachineState {
@Override
public void handleRequest() {
System.out.println("Out of stock state: Product unavailable. Please select another product.");
}
}
class VendingMachineContext {
private VendingMachineState state;
public void setState(VendingMachineState state) {
this.state = state;
}
public void request() {
state.handleRequest();
}
}
public class Main {
public static void main(String[] args) {
// Create context
VendingMachineContext vendingMachine = new VendingMachineContext();
// Set initial state
vendingMachine.setState(new ReadyState());
// Request state change
vendingMachine.request();
// Change state
vendingMachine.setState(new ProductSelectedState());
// Request state change
vendingMachine.request();
// Change state
vendingMachine.setState(new PaymentPendingState());
// Request state change
vendingMachine.request();
// Change state
vendingMachine.setState(new OutOfStockState());
// Request state change
vendingMachine.request();
}
}


Java
interface VendingMachineState {
void handleRequest();
}
class ReadyState implements VendingMachineState {
@Override
public void handleRequest() {
System.out.println("Ready state: Please select a product.");
}
}
class ProductSelectedState implements VendingMachineState {
@Override
public void handleRequest() {
System.out.println("Product selected state: Processing payment.");
}
}
class PaymentPendingState implements VendingMachineState {
@Override
public void handleRequest() {
System.out.println("Payment pending state: Dispensing product.");
}
}
class OutOfStockState implements VendingMachineState {
@Override
public void handleRequest() {
System.out.println("Out of stock state: Product unavailable. Please select another product.");
}
}
class VendingMachineContext {
private VendingMachineState state;
public void setState(VendingMachineState state) {
this.state = state;
}
public void request() {
state.handleRequest();
}
}
public class Main {
public static void main(String[] args) {
// Create context
VendingMachineContext vendingMachine = new VendingMachineContext();
// Set initial state
vendingMachine.setState(new ReadyState());
// Request state change
vendingMachine.request();
// Change state
vendingMachine.setState(new ProductSelectedState());
// Request state change
vendingMachine.request();
// Change state
vendingMachine.setState(new PaymentPendingState());
// Request state change
vendingMachine.request();
// Change state
vendingMachine.setState(new OutOfStockState());
// Request state change
vendingMachine.request();
}
}


Python
from abc import ABC, abstractmethod
class VendingMachineState(ABC):
@abstractmethod
def handle_request(self):
pass
class ReadyState(VendingMachineState):
def handle_request(self):
print("Ready state: Please select a product.")
class ProductSelectedState(VendingMachineState):
def handle_request(self):
print("Product selected state: Processing payment.")
class PaymentPendingState(VendingMachineState):
def handle_request(self):
print("Payment pending state: Dispensing product.")
class OutOfStockState(VendingMachineState):
def handle_request(self):
print("Out of stock state: Product unavailable. Please select another product.")
class VendingMachineContext:
def __init__(self):
self.state = None
def set_state(self, state):
self.state = state
def request(self):
self.state.handle_request()
def main():
# Create context
vending_machine = VendingMachineContext()
# Set initial state
vending_machine.set_state(ReadyState())
# Request state change
vending_machine.request()
# Change state
vending_machine.set_state(ProductSelectedState())
# Request state change
vending_machine.request()
# Change state
vending_machine.set_state(PaymentPendingState())
# Request state change
vending_machine.request()
# Change state
vending_machine.set_state(OutOfStockState())
# Request state change
vending_machine.request()
if __name__ == "__main__":
main()


JavaScript
class VendingMachineState {
handleRequest() {
throw new Error('Method handleRequest must be implemented.');
}
}
class ReadyState extends VendingMachineState {
handleRequest() {
console.log('Ready state: Please select a product.');
}
}
class ProductSelectedState extends VendingMachineState {
handleRequest() {
console.log('Product selected state: Processing payment.');
}
}
class PaymentPendingState extends VendingMachineState {
handleRequest() {
console.log('Payment pending state: Dispensing product.');
}
}
class OutOfStockState extends VendingMachineState {
handleRequest() {
console.log('Out of stock state: Product unavailable. Please select another product.');
}
}
class VendingMachineContext {
constructor() {
this.state = null;
}
setState(state) {
this.state = state;
}
request() {
this.state.handleRequest();
}
}
function main() {
// Create context
const vendingMachine = new VendingMachineContext();
// Set initial state
vendingMachine.setState(new ReadyState());
// Request state change
vendingMachine.request();
// Change state
vendingMachine.setState(new ProductSelectedState());
// Request state change
vendingMachine.request();
// Change state
vendingMachine.setState(new PaymentPendingState());
// Request state change
vendingMachine.request();
// Change state
vendingMachine.setState(new OutOfStockState());
// Request state change
vendingMachine.request();
}
main();


**Output:**

Output
Ready state: Please select a product.
Product selected state: Processing payment.
Payment pending state: Dispensing product.
Out of stock state: Product unavailable. Please select another product.


**Communication between Components** in the above example:

- When a user interacts with the vending machine (Context), such as inserting money or selecting a product, the vending machine delegates the responsibility of handling the interaction to the current state object.
- The current state object (e.g., "ReadyState" or "ProductSelectedState") executes the behavior associated with that state, such as processing the payment or dispensing the selected product.
- Depending on the outcome of the interaction and the logic implemented within the current state object, the vending machine may transition to a different state.
- The process continues as the user interacts further with the vending machine, with behavior delegated to the appropriate state object based on the current state of the vending machine.


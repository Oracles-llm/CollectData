# Template Method Design Pattern | C++ Design Patterns

Template Method Pattern introduces a template in a superclass that defines the steps of an algorithm. These steps may include both common tasks shared among subclasses and specific tasks that need customization. Subclasses then implement or override these steps to modify the algorithm according to their specific needs.


Important Topics for Template Method Design Pattern

**Example for Template Method Design Pattern in C++ **

### Problem Statement:

We have to design a system for building different types of vehicles.


**Key Components of Template Method Design Pattern in C++**

These components help define a common algorithm structure while allowing specific steps to be customized by subclasses. Here are the key components of the Template Method Pattern:

**Template Method: ** The template method is a method in an abstract base class (or interface) that defines the overall algorithm structure. It consists of a series of steps, some of which are implemented in the base class and others that are left abstract or virtual for concrete subclasses to implement.**Abstract Methods (or Hooks): **These are abstract or virtual methods declared in the abstract base class (or interface) that represent steps of the algorithm to be implemented by concrete subclasses.**Concrete Classes:** Concrete classes are derived from the abstract base class and provide concrete implementations for the abstract methods. **Template or Base Class:** The template or base class is an abstract class (or interface) that declares the template method and may include some default implementations of steps.**Client: **The client is the code that uses the template method pattern. It creates instances of concrete classes and invokes the template method to execute the algorithm.

**Implementation of above Problem in C++:**

**VehicleTemplate ):**

**Responsibility: **Defines the overall algorithm structure for building a vehicle. It includes a template method ("buildVehicle") that orchestrates the steps of vehicle construction.

**Abstract Methods:**

**assembleBody: **To be implemented by concrete classes for assembling the body of the vehicle.**installEngine: **To be implemented by concrete classes for installing the engine.**addWheels: **To be implemented by concrete classes for adding wheels to the vehicle.

C++
// Step 1: Template Method (Abstract Class)
class VehicleTemplate {
public:
// Template method defines the algorithm structure
void buildVehicle() {
assembleBody();
installEngine();
addWheels();
std::cout << "Vehicle is ready!\n";
}
// Abstract methods to be implemented by concrete classes
virtual void assembleBody() = 0;
virtual void installEngine() = 0;
virtual void addWheels() = 0;
};


**Car and Motorcycle(Concrete Classes):**

**Responsibility:** Concrete implementations of the abstract class "VehicleTemplate". They provide specific details for building different types of vehicles.

**Implementation of Abstract Methods:**

- "Car" implements "assembleBody", "installEngine", and "addWheels" methods for building a car.
- "Motorcycle" implements similar methods created for building a motorcycle.

C++
class Car : public VehicleTemplate {
public:
void assembleBody() override {
std::cout << "Assembling car body.\n";
}
void installEngine() override {
std::cout << "Installing car engine.\n";
}
void addWheels() override {
std::cout << "Adding 4 wheels to the car.\n";
}
};
class Motorcycle : public VehicleTemplate {
public:
void assembleBody() override {
std::cout << "Assembling motorcycle frame.\n";
}
void installEngine() override {
std::cout << "Installing motorcycle engine.\n";
}
void addWheels() override {
std::cout << "Adding 2 wheels to the motorcycle.\n";
}
};


**Main Function(Client Code): **Demonstrates how to use the template method pattern by creating instances of "Car" and "Motorcycle" and invoking their "buildVehicle" method.** Output:** Shows the result of building a car and a motorcycle, including the specific steps executed in the construction process.

C++
int main() {
std::cout << "Building a Car:\n";
Car car;
car.buildVehicle();
std::cout << "\nBuilding a Motorcycle:\n";
Motorcycle motorcycle;
motorcycle.buildVehicle();
return 0;
}


**Below is the complete combined code of the above example:**

C++
#include <iostream>
// Step 1: Template Method (Abstract Class)
class VehicleTemplate {
public:
// Template method defines the algorithm structure
void buildVehicle() {
assembleBody();
installEngine();
addWheels();
std::cout << "Vehicle is ready!\n";
}
// Abstract methods to be implemented by concrete classes
virtual void assembleBody() = 0;
virtual void installEngine() = 0;
virtual void addWheels() = 0;
};
// Step 2: Concrete Classes
class Car : public VehicleTemplate {
public:
void assembleBody() override {
std::cout << "Assembling car body.\n";
}
void installEngine() override {
std::cout << "Installing car engine.\n";
}
void addWheels() override {
std::cout << "Adding 4 wheels to the car.\n";
}
};
class Motorcycle : public VehicleTemplate {
public:
void assembleBody() override {
std::cout << "Assembling motorcycle frame.\n";
}
void installEngine() override {
std::cout << "Installing motorcycle engine.\n";
}
void addWheels() override {
std::cout << "Adding 2 wheels to the motorcycle.\n";
}
};
// Step 3: Client Code
int main() {
std::cout << "Building a Car:\n";
Car car;
car.buildVehicle();
std::cout << "\nBuilding a Motorcycle:\n";
Motorcycle motorcycle;
motorcycle.buildVehicle();
return 0;
}


**Output: **

Building a Car:

Assembling car body.

Installing car engine.

Adding 4 wheels to the car.

Vehicle is ready!

Building a Motorcycle:

Assembling motorcycle frame.

Installing motorcycle engine.

Adding 2 wheels to the motorcycle.

Vehicle is ready!



**Diagrammatical Representation of Template Method Design Pattern in C++**

**VehicleTemplate (Abstract Class):** Represents the abstract class "VehicleTemplate". Contains abstract methods ("assembleBody", "installEngine", "addWheels") that need to be implemented by concrete subclasses. Defines the template method "buildVehicle", which manages the algorithm's structure.**Car (Concrete Class):** Represents the concrete class "Car" that inherits from "VehicleTemplate". Implements specific details for building a car, providing concrete implementations for the abstract methods (("assembleBody", "installEngine", "addWheels").**Motorcycle (Concrete Class):** Represents the concrete class "Motorcycle" that also inherits from "VehicleTemplate". Implements specific details for building a motorcycle, providing concrete implementations for the abstract methods (("assembleBody", "installEngine", "addWheels").**Arrows (Inheritance Relationships):** The arrows indicate the inheritance relationships between "VehicleTemplate" and its concrete subclasses ("Car" and "Motorcycle") "Car" and "Motorcycle" inherit the template method and abstract methods from "VehicleTemplate".**Method Implementation:** The + assembleBody(), + installEngine(), and + addWheels() within Car and Motorcycle indicate that these methods are implemented in these concrete classes.

**Advantages of the Template Method Design Pattern in C++ **

**Code Reusability:** The Template Method pattern promotes the reuse of the common algorithm structure defined in the template method across multiple subclasses. This reduces code duplication.**Flexibility:** Concrete subclasses have the flexibility to customize specific steps of the algorithm by providing their implementations for abstract methods. This allows for variations in behavior without altering the overall algorithm structure.**Consistent Structure: **The template method defines a clear and consistent structure for the algorithm, ensuring that certain steps are executed in a specific sequence. This consistency improves code structure and readability.**Encapsulation: **The pattern encapsulates the details of the algorithm within the abstract class, separating the high-level algorithm from the specific implementations. This encapsulation enhances modularity.**Maintenance Ease: **Modifications to the common algorithm structure in the template method automatically affects all subclasses. This simplifies maintenance efforts, limiting modifications to the abstract class only.

**Disadvantages of the Template Method Design Pattern in C++ **

**Inflexibility of Inheritance: **The pattern relies on inheritance, and excessive use of inheritance can lead to inflexible designs. Subclasses are bound to the structure defined in the abstract class, and changes to the overall structure may require modifications in multiple places.**Limited Runtime Modifications: **The template method is defined at compile-time, and changes to the algorithm structure may require modifying the abstract class. This can limit the ability to make runtime changes to the algorithm.**Code Duplication in Concrete Classes: **While the template method promotes reuse, there might still be cases where concrete subclasses share common code that cannot be abstracted into the template method. This can lead to code duplication in the concrete classes.**Potential for Large Hierarchies: **As the number of concrete subclasses increases, the template method may become more complex, resulting in large class hierarchies. This can make the system harder to understand and maintain.**Difficulty in Understanding the Flow:** For developers unfamiliar with the pattern, understanding the flow of control between the template method and abstract methods in different subclasses might be challenging. This can impact the readability of the code.

**Conclusion**

The Template Method Pattern in C++ is a is a powerful and flexible design pattern for creating robust and adaptable software designs, that facilitates the creation of algorithms with a common structure while allowing specific steps to be customized by subclasses. By understanding its principles and using its key components, developers can build frameworks and systems that can efficiently handle variations in algorithm while maintaining a structured and organized codebase.
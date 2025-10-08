# Facade Method Design Pattern

**Facade Design Pattern** is a **Structural pattern** from the Gang of Four that simplifies interactions with complex subsystems. It provides a unified, easy-to-use interface while hiding internal details, reducing complexity for clients and promoting cleaner, more maintainable code.

Let's understand this with the help of Diagram:

- Structuring a system into subsystems helps reduce complexity.
- A common design goal is to minimize the communication and dependencies between subsystems.
- One way to achieve this goal is to introduce a Facade object that provides a single simplified interface to the more general facilities of a subsystem.

**Note **: Facade Method Design Pattern provides a unified interface to a set of interfaces in a subsystem. Facade defines a high-level interface that makes the subsystem easier to use.

## Real Life Use of Fcade Design Pattern

**Home Automation Systems**

Simplifies control of lights, heating, and security through a single interface.

**Video Streaming Platforms**

Provides a unified interface for video encoding, buffering, and playback.

**Banking Systems**

Offers easy access to complex operations like fund transfers and balance inquiries.

**Car Engine Start-up**

Coordinates multiple subsystems (fuel, ignition, starter) with one simple method call.

## Use of Facade Method Design Pattern

**Simplifying Complex External Systems** – Encapsulates database handling and hides API complexities.**Layering Subsystems** – Defines clear boundaries and offers simplified subsystem interfaces.**Providing a Unified Interface to Diverse Systems** – Combines multiple APIs and modernizes older systems.**Protecting Clients from Unstable Systems** – Maintains a stable interface and shields clients from external changes.

## Advantages of Facade Method Design Pattern

**Simplified Interface** – Provides a clear interface while hiding system complexities.**Reduced Coupling** – Minimizes client dependency on system internals and promotes modularity.**Encapsulation** – Shields clients from subsystem changes by wrapping complex interactions.**Improved Maintainability** – Enables easier system changes, refactoring, and extensions without affecting clients.

## Disadvantages of Facade Method Design Pattern

**Increased Complexity** – Adds another abstraction layer, making code harder to understand and debug.**Reduced Flexibility** – Limits direct access to specific subsystem functionalities.**Overengineering** – Can add unnecessary complexity in simple systems.**Potential Performance Overhead** – Extra indirection may impact performance in critical scenarios.

## Key Components of Facade Method Design Pattern

In the above diagram, Consider for example a programming environment that gives applications access to its compiler subsystem.

- This subsystem contains classes such as Scanner,Parser, ProgramNode, BytecodeStream, and ProgramNodeBuilder that implement the compiler.
- Compiler class acts as a facade: It offers clients a single, simple interface to the compilersubsystem.
- It glues together the classes that implement compilerfunctionality without hiding themcompletely.
- The compiler facade makes life easier for most programmers without hiding the lower-level functionality from the few that need it.

### 1. Facade (Compiler)

- Facade knows which subsystem classes are responsible for a request.
- It delegate client requests to appropriate subsystem objects.

### 2. Subsystem classes (Scanner, Parser, ProgramNode, etc.)

- It implement subsystem functionality.
- It handle work assigned by the Facade object.
- It have no knowledge of the facade; that is, they keep no references to it.

### 3. Interface

- The Interface in the Facade Design Pattern refers to the set of simplified methods that the facade exposes to the client.
- It hides the complexities of the subsystem, ensuring that clients interact only with high-level operations, without dealing with the underlying details of the system.

### Facade Method Design Pattern collaborate in different way

- Client communicate with the subsystem by sending requests to Facade, which forwards them to the appropriate subsystem objects.
- The Facade may have to do work of its own to translate it inheritance to subsystem interface.
- Clients that use the Facade don't have to access its subsystem objects directly.

## Steps to implement Facade Design Pattern

Below are the simple steps to implement the Facade Design Pattern:

**Step 1:** First, determine the complex subsystems or components that the client needs to interact with.**Step 2: **Build a facade class that serves as the middle layer between the client and the subsystems. This class should offer simplified methods that wrap the interactions with the subsystems.**Step 3:** Expose a clear, high-level interface in the facade class. This interface will include the methods that the client will use, hiding the internal complexity.**Step 4: **Inside the facade methods, delegate the requests to the appropriate subsystem classes to perform the actual operations.**Step 5:** The client now interacts only with the facade, which manages the underlying calls to the subsystems, simplifying the client’s experience.

## Example for the Facade Method Design Pattern (with implementation)

**Problem Statement:**

Let’s consider a hotel. This hotel has a hotel keeper. There are a lot of restaurants inside the hotel e.g. Veg restaurants, Non-Veg restaurants, and Veg/Non Both restaurants. You, as a client want access to different menus of different restaurants.

- You do not know what are the different menus they have. You just have access to a hotel keeper who knows his hotel well.
- Whichever menu you want, you tell the hotel keeper and he takes it out of the respective restaurants and hands it over to you.


So here, **Hotel-Keeper** is Facade and respective **Restaurants **is system. Below is the step-by-step Implementation of above problem.

**1. Interface of Hotel**

C++
package structural.facade;
public interface Hotel {
public Menus getMenus();
}


Java
package structural.facade;
public interface Hotel {
public Menus getMenus();
}


Python
from abc import ABC, abstractmethod
class Hotel(ABC):
@abstractmethod
def get_menus(self):
pass


JavaScript
// JavaScript does not have interfaces, but we can simulate one using a class with abstract methods
class Hotel {
getMenus() {
throw new Error("Method getMenus() must be implemented.");
}
}


**Note** : The hotel interface only returns Menus. Similarly, the Restaurant are of three types and can implement the hotel interface. Let’s have a look at the code for one of the Restaurants.

**2. NonVegRestaurant**

C++
package structural.facade;
public class NonVegRestaurant implements Hotel {
public Menus getMenus()
{
NonVegMenu nv = new NonVegMenu();
return nv;
}
}


Java
package structural.facade;
public class NonVegRestaurant implements Hotel {
public Menus getMenus()
{
NonVegMenu nv = new NonVegMenu();
return nv;
}
}


Python
from structural.facade import Hotel, Menus, NonVegMenu
class NonVegRestaurant(Hotel):
def get_menus(self):
nv = NonVegMenu()
return nv


JavaScript
class NonVegRestaurant {
getMenus() {
let nv = new NonVegMenu();
return nv;
}
}


**3. VegRestaurant**

C++
package structural.facade;
public class VegRestaurant implements Hotel {
public Menus getMenus()
{
VegMenu v = new VegMenu();
return v;
}
}


Java
package structural.facade;
public class VegRestaurant implements Hotel {
public Menus getMenus() {
VegMenu v = new VegMenu();
return v;
}
}


Python
class VegRestaurant:
def getMenus(self):
v = VegMenu()
return v


JavaScript
class VegRestaurant {
getMenus() {
let v = new VegMenu();
return v;
}
}


**4. VegNonBothRestaurant**

C++
package structural.facade;
public class VegNonBothRestaurant implements Hotel {
public Menus getMenus()
{
Both b = new Both();
return b;
}
}


Java
package structural.facade;
public class VegNonBothRestaurant implements Hotel {
public Menus getMenus() {
Both b = new Both();
return b;
}
}


Python
class VegNonBothRestaurant:
def getMenus(self):
b = Both()
return b


JavaScript
class VegNonBothRestaurant {
getMenus() {
let b = new Both();
return b;
}
}



**Now let’s consider the facade Design Pattern with the help of code:**

**1. HotelKeeper**

C++
/*package whatever //do not write package name here */
package structural.facade;
public interface HotelKeeper {
public VegMenu getVegMenu();
public NonVegMenu getNonVegMenu();
public Both getVegNonMenu();
}


Java
/*package whatever //do not write package name here */
package structural.facade;
public interface HotelKeeper {
public VegMenu getVegMenu();
public NonVegMenu getNonVegMenu();
public Both getVegNonMenu();
}


Python
"""package whatever //do not write package name here """
from abc import ABC, abstractmethod
class HotelKeeper(ABC):
@abstractmethod
def getVegMenu(self):
pass
@abstractmethod
def getNonVegMenu(self):
pass
@abstractmethod
def getVegNonMenu(self):
pass


JavaScript
/*package whatever //do not write package name here */
// Assuming the existence of classes VegMenu, NonVegMenu, and Both
class HotelKeeper {
getVegMenu() {
throw new Error("Method not implemented.");
}
getNonVegMenu() {
throw new Error("Method not implemented.");
}
getVegNonMenu() {
throw new Error("Method not implemented.");
}
}


**2. HotelKeeperImplementation**

C++
package structural.facade;
public class HotelKeeperImplementation implements HotelKeeper {
public VegMenu getVegMenu()
{
VegRestaurant v = new VegRestaurant();
VegMenu vegMenu = (VegMenu)v.getMenus();
return vegMenu;
}
public NonVegMenu getNonVegMenu()
{
NonVegRestaurant v = new NonVegRestaurant();
NonVegMenu NonvegMenu = (NonVegMenu)v.getMenus();
return NonvegMenu;
}
public Both getVegNonMenu()
{
VegNonBothRestaurant v = new VegNonBothRestaurant();
Both bothMenu = (Both)v.getMenus();
return bothMenu;
}
}


Java
package structural.facade;
public class HotelKeeperImplementation implements HotelKeeper {
public VegMenu getVegMenu()
{
VegRestaurant v = new VegRestaurant();
VegMenu vegMenu = (VegMenu)v.getMenus();
return vegMenu;
}
public NonVegMenu getNonVegMenu()
{
NonVegRestaurant v = new NonVegRestaurant();
NonVegMenu NonvegMenu = (NonVegMenu)v.getMenus();
return NonvegMenu;
}
public Both getVegNonMenu()
{
VegNonBothRestaurant v = new VegNonBothRestaurant();
Both bothMenu = (Both)v.getMenus();
return bothMenu;
}
}


Python
from abc import ABC, abstractmethod
class HotelKeeper(ABC):
@abstractmethod
def getVegMenu(self):
pass
@abstractmethod
def getNonVegMenu(self):
pass
@abstractmethod
def getVegNonMenu(self):
pass
class VegRestaurant:
def getMenus(self):
return VegMenu()
class NonVegRestaurant:
def getMenus(self):
return NonVegMenu()
class VegNonBothRestaurant:
def getMenus(self):
return Both()
class HotelKeeperImplementation(HotelKeeper):
def getVegMenu(self):
v = VegRestaurant()
vegMenu = v.getMenus()
return vegMenu
def getNonVegMenu(self):
v = NonVegRestaurant()
nonVegMenu = v.getMenus()
return nonVegMenu
def getVegNonMenu(self):
v = VegNonBothRestaurant()
bothMenu = v.getMenus()
return bothMenu
class VegMenu:
pass
class NonVegMenu:
pass
class Both:
pass


JavaScript
class HotelKeeper {
getVegMenu() {
throw new Error('Method not implemented.');
}
getNonVegMenu() {
throw new Error('Method not implemented.');
}
getVegNonMenu() {
throw new Error('Method not implemented.');
}
}
class VegRestaurant {
getMenus() {
return new VegMenu();
}
}
class NonVegRestaurant {
getMenus() {
return new NonVegMenu();
}
}
class VegNonBothRestaurant {
getMenus() {
return new Both();
}
}
class HotelKeeperImplementation extends HotelKeeper {
getVegMenu() {
let v = new VegRestaurant();
let vegMenu = v.getMenus();
return vegMenu;
}
getNonVegMenu() {
let v = new NonVegRestaurant();
let nonVegMenu = v.getMenus();
return nonVegMenu;
}
getVegNonMenu() {
let v = new VegNonBothRestaurant();
let bothMenu = v.getMenus();
return bothMenu;
}
}
class VegMenu {}
class NonVegMenu {}
class Both {}


**Note**:From this, It is clear that the complex implementation will be done by HotelKeeper himself. The client will just access the HotelKeeper and ask for either Veg, NonVeg or VegNon Both Restaurant menu.

**How will the client program access this facade?**

C++
package structural.facade;
public class Client
{
public static void main (String[] args)
{
HotelKeeper keeper = new HotelKeeperImplementation();
VegMenu v = keeper.getVegMenu();
NonVegMenu nv = keeper.getNonVegMenu();
Both = keeper.getVegNonMenu();
}
}


Java
package structural.facade;
public class Client
{
public static void main (String[] args)
{
HotelKeeper keeper = new HotelKeeperImplementation();
VegMenu v = keeper.getVegMenu();
NonVegMenu nv = keeper.getNonVegMenu();
BothMenu both = keeper.getVegNonMenu();
}
}


Python
from structural.facade import HotelKeeperImplementation, VegMenu, NonVegMenu, BothMenu
def main():
keeper = HotelKeeperImplementation()
v = keeper.get_veg_menu()
nv = keeper.get_non_veg_menu()
both = keeper.get_veg_non_menu()
if __name__ == "__main__":
main()


JavaScript
const { HotelKeeperImplementation, VegMenu, NonVegMenu, BothMenu } = require('./structural/facade');
function main() {
const keeper = new HotelKeeperImplementation();
const v = keeper.getVegMenu();
const nv = keeper.getNonVegMenu();
const both = keeper.getVegNonMenu();
}
main();



In this way, the implementation is sent to the façade. The client is given just one interface and can access only that. This hides all the complexities.


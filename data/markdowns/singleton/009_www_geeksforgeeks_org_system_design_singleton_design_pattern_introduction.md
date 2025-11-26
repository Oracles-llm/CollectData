# Singleton Method Design Pattern in JavaScript

Singleton Method or Singleton Design Pattern is a part of the **Gang of Four design pattern** and it is categorized under **creational** design patterns. It is one of the most simple design patterns in terms of modeling but on the other hand, this is one of the most controversial patterns in terms of complexity of usage.

Important Topics for the Singleton Method Design Pattern in JavaScript

## 1. What is Singleton Method Design Pattern in JavaScript?

Singleton pattern is a design pattern which restricts a class to instantiate its multiple objects. It is nothing but a way of defining a class. Class is defined in such a way that only one instance of the class is created in the complete execution of a program or project.


## 2. When to use the Singleton Method Design Pattern in JavaScript?

Here are some situations in JavaScript where the Singleton pattern may be applicable:

**Logging Service:** For a logging service that needs to capture and centralize log entries across the entire application, a Singleton can ensure that there's only one logging instance.**Managing Shared Resources:** In scenarios where you need to manage shared resources like database connections, network connections, or thread pools, a Singleton can help coordinate and control access to these resources.**Service Classes:** For services that should have a single instance, such as a data service, API service, or utility service, a Singleton pattern can provide a consistent interface.**Preventing Multiple Instantiations:** When instantiating multiple instances of a class would cause issues or inefficiencies, a Singleton ensures that there is only one instance in the entire application.**Lazy Initialization:** If the instantiation of an object is resource-intensive and you want to delay the creation until it is actually needed, a Singleton can provide lazy initialization.**Preventing Cloning:** If you want to prevent the cloning of an object, which could lead to multiple instances, a Singleton can include logic to prohibit cloning.

## 3. Key Component of Singleton Method Design Pattern in JavaScript:

**3.1. Private Constructor:**

The class should have a private constructor to prevent instantiation of the class from external classes.

JavaScript
const Singleton = (function () {
// Private variable to store the instance
let instance;


**3.2. Private Static Instance:**

- The class should have a private static instance of itself. This instance is the single instance that the pattern ensures.

JavaScript
function Singleton() {
if (instance) {
// If an instance already exists, return that instance
return instance;
}
// Initialization code
// ...
// Assign `this` to the `instance` variable
instance = this;
}


**3.3. Public Static Method to Access the Instance:**

- The class provides a public static method that returns the instance of the class. If an instance does not exist, it creates one; otherwise, it returns the existing instance.

JavaScript
Singleton.prototype.getInstance = function () {
return instance;
};


**3.4. Lazy Initialization:**

- The instance is created only when it is first requested. This is known as lazy initialization. It helps improve performance by avoiding the unnecessary creation of the instance.

JavaScript
Singleton.getInstance = function () {
if (!instance) {
// Lazy initialization: create the instance only when needed
instance = new LazySingleton();
}
return instance;
};


**3.5. Prevention of Cloning and Serialization:**

- To maintain the Singleton property, you may need to override the
`clone`

method to throw an exception and ensure that the class is not serializable or provide custom serialization logic.

JavaScript
function revive(key, value) {
if (key === '' && value && value.__isSingleton) {
return instance;
}
return value;
}


## 4. Implementation of Singleton Method Design Pattern in JavaScript

**Problem Statement: **

Implement a Singleton pattern in JavaScript, ensuring that only one instance of a class is created and providing a mechanism to access that instance. Additionally, prevent cloning and serialization of the Singleton instance.


### Step wise explaination of above Problem Statement

**Immediately Invoked Function Expression (IIFE):**The pattern uses an IIFE to create a closure, providing a private scope for the `instance`

variable and functions within it.**Private Instance Variable:** The `instance`

variable is used to store the single instance of the Singleton class. It's private to the closure, preventing direct access from outside.**Private Constructor:** The `Singleton`

constructor is defined inside the closure and checks if an instance already exists. If it does, it throws an error to prevent the creation of additional instances.**Static ****getInstance**

** Method:** The `getInstance`

method is a static method of the Singleton class, providing a way to access the single instance. If the instance doesn't exist, it creates a new one; otherwise, it returns the existing instance.**Clone and Deserialize Prevention:** The `clone`

and `customDeserialize`

methods are defined to throw errors, preventing cloning and deserialization of the Singleton instance.**JSON Serialization Prevention:** The `toJSON`

method is overridden to return a JSON string with a marker property (`__isSingleton`

). This marker is later used in the `revive`

function to identify the Singleton instance during deserialization.**Reviver Function for Deserialization:** The `revive`

function is used as the reviver function for `JSON.parse`

to check for the marker property and return the existing instance, preventing the creation of a new instance during deserialization.

### Overall Code for Above Problem Statement in JavaScript:

JavaScript
const Singleton = (function () {
let instance;
function Singleton() {
if (instance) {
throw new Error("Singleton instance already exists. Use getInstance method.");
}
// Initialization code
this.data = Math.random(); // Example: Initialization with random data
}
Singleton.getInstance = function () {
if (!instance) {
instance = new Singleton();
}
return instance;
};
Singleton.prototype.clone = function () {
throw new Error("Cloning of singleton instance is not allowed.");
};
Singleton.prototype.customDeserialize = function () {
throw new Error("Deserialization of singleton instance is not allowed.");
};
// JSON.parse reviver function to prevent deserialization
function revive(key, value) {
if (key === '' && value && value.__isSingleton) {
return instance;
}
return value;
}
Singleton.prototype.toJSON = function () {
return JSON.stringify({ __isSingleton: true, data: this.data });
};
return Singleton;
})();
// Usage
try {
const singletonInstance1 = Singleton.getInstance();
console.log(singletonInstance1);
// Attempting to create another instance should throw an error
const singletonInstance2 = new Singleton();
} catch (error) {
console.error(error.message); // Singleton instance already exists. Use getInstance method.
}
// Cloning prevention
try {
const clonedInstance = Object.create(singletonInstance1);
console.log(clonedInstance); // Will throw an error
} catch (error) {
console.error(error.message); // Cloning of singleton instance is not allowed.
}
// Serialization prevention
try {
const serializedInstance = JSON.stringify(singletonInstance1);
console.log(serializedInstance); // Will throw an error
} catch (error) {
console.error(error.message); // Serialization of singleton instance is not allowed.
}
// Deserialization prevention
const jsonString = JSON.stringify(singletonInstance1);
const deserializedInstance = JSON.parse(jsonString, revive);
console.log(deserializedInstance); // Will be the same instance as singletonInstance1


**Output: **

Singleton instance already exists.

singletonInstance1 is not defined

singletonInstance1 is not defined

## 5. Use Case of Singleton Method Design Pattern in JavaScript

There is a application of singleton pattern like cache-memory, database connection, drivers, logging. Some major of them are :-

**Hardware interface access:** Singleton classes are also used to prevent concurrent access of class. Practically singleton can be used in case external hardware resource usage limitation required e.g. Hardware printers where the print spooler can be made a singleton to avoid multiple concurrent accesses and creating deadlock.**Logger :** Singleton classes are used in log file generations. Log files are created by the logger class object. - Suppose an application where the logging utility has to produce one log file based on the messages received from the users.
- If there is multiple client application using this logging utility class they might create multiple instances of this class and it can potentially cause issues during concurrent access to the same logger file.

**Configuration File:** This is another potential candidate for Singleton pattern because this has a performance benefit as it prevents multiple users to repeatedly access and read the configuration file or properties file. It creates a single instance of the configuration file which can be accessed by multiple calls concurrently as it will provide static config data loaded into in-memory objects. **Cache:** We can use the cache as a singleton object as it can have a global point of reference and for all future calls to the cache object the client application will use the in-memory object.

## 6. Advantages of Singleton Method Design Pattern in JavaScript:

The Singleton method design pattern has several benefits:

**Controlled access to sole instance:** Because the Singleton class encapsulates its sole instance, it can have strict control over how and when clients access it.**Reduced name space:** The Singleton pattern is an improvement over global variables. It avoids polluting the name space with global variables that store sole instances. **Permits refinement of operations and representation:** The Singleton class may be subclassed, and it's easy to configure an application with an instance of this extended class. You can configure the application with an instance of the class you need at run-time. **Permits a variable number of instances:** The pattern makesit easy to change your mind and allow more than one instance of the Singleton class. Moreover, you can use the same approach to control the number of instances that the application uses. Only the operation that grants access to the Singleton instance needs to change. **More flexible than class operations:** Another way to package a singleton's functionality is to use class operations (that is,static member functions in C++ or class methods in Smalltalk).But both of these language techniques make it hard to change a design to allow more than one instance of a class.Moreover, static member functions inC++are never virtual, so subclasses can't override them polymorphically.

## 7. Disadvantages Of Singleton Method Design Pattern in JavaScript

The Singleton Method Design Pattern have different disadvantage:

**Concurrency Issues**: If not implemented carefully, Singletons can introduce concurrency issues in multi-threaded applications. You may need to use synchronization mechanisms, like locks or mutexes, to ensure safe access to the Singleton instance, which can add complexity to your code.**Singleton Pattern Overuse:** Due to its convenience, developers might overuse the Singleton pattern, leading to an abundance of Singleton instances in an application. This can defeat the purpose of the pattern and result in increased memory usage.**Initialization Overhead**: Lazy initialization, while often an advantage, can introduce some overhead when the Singleton instance is first accessed. If the initialization process is resource-intensive, it can affect the application’s startup time.**Difficulties in Debugging**: Debugging a Singleton-based codebase can be challenging, especially when issues related to the Singleton’s state arise. It can be hard to trace the source of problems when multiple parts of the code may have modified the Singleton’s data.**Limited Dependency Injection**: Using dependency injection and inversion of control becomes less straightforward when relying on Singleton instances. It may be challenging to inject alternative implementations or configurations because the Singleton instance is typically accessed globally.

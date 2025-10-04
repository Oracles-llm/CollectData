# What is Singleton Design Pattern?

Singleton Pattern is a creational design pattern that guarantees a class has only one instance and provides a global point of access to it.


It involves only one class which is responsible for instantiating itself, making sure it creates not more than one instance.

### Implementation

To implement the singleton pattern, we must prevent external objects from creating instances of the singleton class. Only the singleton class should be permitted to create its own objects.

Additionally, we need to provide a method for external objects to access the singleton object.

This can be achieved by making the **constructor private** and providing a **static method** for external objects to access it.

The `instance`

class variable holds the one and only instance of the Singleton class.

The `Singleton()`

constructor is declared as private, preventing external objects from creating new instances.

The `getInstance()`

method is a static class method, making it accessible to the external world.

There are several ways to implement the Singleton Pattern, each with its own advantages and disadvantages.

# 1. Lazy Initialization

This approach creates the singleton instance only when it is needed, saving resources if the singleton is never used in the application.

Checks if an instance already exists (

`instance == null`

).If not, it creates a new instance.

If an instance already exists, it skips the creation step.


This implementation is not thread-safe. If multiple threads call `getInstance()`

simultaneously when `instance`

is null, it's possible to create multiple instances.

# 2. Thread-Safe Singleton

This approach is similar to lazy initialization but also ensures that the singleton is thread-safe.

This is achieved by making the `getInstance()`

method **synchronized** ensuring only one thread can execute this method at a time.

When a thread enters the synchronized method, it acquires a lock on the class object. Other threads must wait until the method is executed.

The

**synchronization**keyword ensures that only one thread can perform the (`instance == null)`

check and create the object.

If calling the `getInstance() `

method isn’t causing substantial overhead, this approach is straightforward and effective.

But, using `synchronized`

can decrease performance, which can be a bottleneck if called frequently.

# 3. Double-Checked Locking

This approach minimizes performance overhead from synchronization by only synchronizing when the object is first created.

It uses the `volatile`

keyword to ensure that changes to the instance variable are immediately visible to other threads.

If the first check (

`instance == null)`

passes, we synchronize on the class object.We check the same condition one more time because multiple threads may have passed the first check.

The instance is created only if both checks pass.


Although this method is a bit complex to implement, it can drastically reduce the performance overhead.

# 4. Eager Initialization

In this method, we rely on the JVM to create the singleton instance when the class is loaded. The JVM guarantees that the instance will be created before any thread access the instance variable.

This implementation is one of the simplest and inherently thread-safe without needing explicit synchronization.

`static`

variable ensures there's only one instance shared across all instances of the class.`final`

prevents the instance from being reassigned after initialization.

This approach is suitable if your application always creates and uses the singleton instance, or the overhead of creating it is minimal.

While it is inherently thread-safe, it could potentially waste resources if the singleton instance is never used by the client application.

# 5. Bill Pugh Singleton

This implementation uses a static inner helper class to hold the singleton instance. The inner class is not loaded into memory until it's referenced for the first time in the `getInstance() `

method.

It is thread-safe without requiring explicit synchronization.

When the

`getInstance()`

method is called for the first time, it triggers the loading of the SingletonHelper class.When the inner class is loaded, it creates the INSTANCE of BillPughSingleton.

The

`final`

keyword ensures that the INSTANCE cannot be reassigned.

The Bill Pugh Singleton implementation, while more complex than Eager Initialization provides a perfect balance of lazy initialization, thread safety, and performance, without the complexities of some other patterns like double-checked locking.

# 6. Enum Singleton

In this method, the singleton is declared as an enum rather than a class.

Java ensures that only one instance of an enum value is created, even in a multithreaded environment.

The Enum Singleton pattern is the most robust and concise way to implement a singleton in Java.

Many Java experts, including **Joshua Bloch**, recommend Enum Singleton as the best singleton implementation in Java.

However, it's not always suitable, especially if you need to extend a class or if lazy initialization is a strict requirement.

# 7. Static Block Initialization

This is similar to eager initialization, but the instance is created in a static block.

It provides the ability to handle exceptions during instance creation, which is not possible with simple eager initialization.

The static block is executed when the class is loaded by the JVM.

If an exception occurs, it's wrapped in a RuntimeException.


It is thread safe but not lazy-loaded, which might be a drawback if the initialization is resource-intensive or time-consuming.

# Real-World Examples of Singleton Design Pattern

Singleton is useful in scenarios like:

**Managing Shared Resources**(database connections, thread pools, caches, configuration settings)**Coordinating System-Wide Actions**(logging, print spoolers, file managers)**Managing State (**user session, application state**)**

#### Specific Examples:

**Logger Classes**: Many logging frameworks use the Singleton pattern to provide a global logging object. This ensures that log messages are consistently handled and written to the same output stream.**Database Connection Pools**: Connection pools help manage and reuse database connections efficiently. A Singleton can ensure that only one pool is created and used throughout the application.**Cache Objects**: In-memory caches are often implemented as Singletons to provide a single point of access for cached data across the application.**Thread Pools:**Thread pools manage a collection of worker threads. A Singleton ensures that the same pool is used throughout the application, preventing resource overuse.**File System**: File systems often use Singleton objects to represent the file system and provide a unified interface for file operations.**Print Spooler**: In operating systems, print spoolers manage printing tasks. A single instance coordinates all print jobs to prevent conflicts.

# Pros and Cons of Singleton Design Pattern

It's important to note that the Singleton pattern should be used judiciously, as it introduces global state and can make testing and maintenance more challenging. Consider alternative approaches like **dependency injection** when possible to promote loose coupling and testability.
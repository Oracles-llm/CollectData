One of the most well-known design patterns, singleton ensures the existence of a single instance of a given class during the life of an application. What makes this pattern important and useful? Moreover, what is a design pattern? How do they work? How and when should I use singleton? These questions, plus use cases and examples are covered in detail in this detailed guide. But first, the basics.

Design patterns are well-established resolutions for repetitive challenges in software design, functioning as frameworks that developers can use to address typical architectural difficulties. In addition, patterns guarantee dependability, adaptability, and ease of code maintenance.

Design patterns also serve as a form of documentation, communicating design decisions within a project. If you use a given pattern – and especially if you name it according to the classic names – a reader of your code that knows that pattern will understand immediately what’s going on.

Singleton is a design pattern that restricts a class to having only one instance during the life cycle of your application. The pattern also ensures a unique point of access to the instance. In this way, everyone who needs to use singleton can reach that unique instance.

Singleton makes sense when you have a single instance of a class and need to prevent more instances from being created. Using singleton, you give the class itself the capability to restrict the creation of, and access to, a single instance of the class.

Singleton is about simplifying the reuse of a tried-and-true approach to solve a common problem and clearly communicating that design intent.

For instance, let’s imagine you’re learning how to use dependency injection (DI) in .NET and then, in the context of life cycle management of registered dependencies, you see a line like this:

`services.AddSingleton<IService, ServiceImplementation>();`


If you understand what a singleton design pattern is, from reading the line above you could easily infer that only a single instance of the **IService** interface is created and provided to the clients.

Let’s now take a closer look at the components of the singleton design pattern to understand how it works and how you can use it in your code.

The classic book Design Patterns: Elements of Reusable Object-Oriented Software, by Erich Gamma, Richard Helm, Ralph Johnson, and John Vlissides (aka the Gang of Four) categorizes singleton as a creational pattern. That is, it belongs to the group of patterns that handle the creation of objects. Unlike some of the other creational patterns, though, singleton is quite simple, since it only requires a single class.

To understand how singleton works in practice, let’s create one, step by step, using C#. Let’s begin with a humble class that does something:

```
public class SingletonExample
{
public void PerformSomeAction()
{
Console.WriteLine("I'm doing something!");
}
}
```


For the next step, let’s ensure clients can’t use the constructor to instantiate it[SM1] . We do this by creating a private constructor:

```
public class SingletonExample
{
private SingletonExample()
{
}
public void PerformSomeAction()
{
Console.WriteLine("I'm doing something!");
}
}
```


Let’s now create the unique instance of the class and make it available:

```
public class SingletonExample
{
private static readonly SingletonExample instance = new SingletonExample();
private SingletonExample()
{
}
public static SingletonExample Instance
{
get
{
return instance;
}
}
public void PerformSomeAction()
{
Console.WriteLine("I'm doing something!");
}
}
```


Now, client code can retrieve the unique instance of the singleton by using the **Instance** property:

```
var a = SingletonExample.Instance;
var b = SingletonExample.Instance;
if (a == b)
{
Console.WriteLine("The references are the same!");
}
```


This is a simple yet functional implementation of the singleton pattern in C#. There are ways to make the pattern more sophisticated, such as adding lazy initialization of the instance. For scenarios in which the initialization is costly, however, adding sophistication doesn’t makes sense.

We’ve just seen a simple implementation of singleton using C#. Now, let’s walk through an implementation that’s a bit more involved. This new implementation will have lazy initialization of the instance, and as a consequence, we’ll need to implement thread safety explicitly.

Let’s write this implementation in three languages: C# again, Java, and then Python.

```
public class SingletonExample
{
private static readonly Lazy<SingletonExample> _instance = new Lazy<SingletonExample>(() => new SingletonExample());
private SingletonExample()
{
}
public static SingletonExample Instance
{
get
{
return _instance.Value;
}
}
public void PerformSomeAction()
{
Console.WriteLine("I'm doing something!");
}
}
```


As you can see, the new C# implementation isn’t all that different from the original one. The main difference is how we initialize the **_instance** private field, using the **Lazy<T>** class of the .NET BCL, which is an easy way to implement lazy initialization with thread safety built in.

Now let’s see the implementation for Java:

```
public final class SingletonExample {
private static class InstanceHolder {
private static final SingletonExample INSTANCE = new SingletonExample();
}
private SingletonExample() {}
public static SingletonExample getInstance() {
return InstanceHolder.INSTANCE;
}
public void performSomeAction() {
System.out.println("I'm doing something!");
}
}
```


While Java doesn’t have a direct equivalent to C#’s **Lazy<T>**, we can leverage the fact that the JVM (Java Virtual Machine) guarantees the class loading is thread safe. That way, we create a nested static class to hold the instance for our singleton, but that class will only be loaded when the **getInstance()** method is called for the first time, ensuring a form of lazy initialization.

Finally, let’s see a possible implementation in Python:

```
from threading import Lock
from typing import Optional
class SingletonExample:
_instance: Optional['SingletonExample'] = None
_lock: Lock = Lock()
def __new__(cls) -> 'SingletonExample':
raise TypeError('This is a singleton class - use get_instance() instead')
def __init__(self):
raise TypeError('This is a singleton class - use get_instance() instead')
@classmethod
def get_instance(cls) -> 'SingletonExample':
if not cls._instance:
with cls._lock:
if not cls._instance:
cls._instance = super().__new__(cls)
# Do initialization here
cls._instance._initialized = True
return cls._instance
def perform_some_action(self):
print("I'm doing something!")
```


Here, we use the double-checked locking pattern to ensure thread safety and lazy initialization. Python doesn’t really have private members like C# does; what we do here is to override the **__new__ ** and **__init__** methods, which are Python’s special method for creating and initializing objects, throwing errors if someone attempts to call them.

In the **get_instance** method, we use the lock from Python’s threading module so we can get thread safety.

Thread safety is a crucial concern when it comes to singleton. After all, you’ll have a single instance that gets shared by all threads in a multi-threading scenario.

As you’ve seen, there’s nothing in the singleton pattern that makes it inherently thread safe. To adhere to the classic definition of the pattern, your code must only ensure that:

Different languages handle the singleton design pattern in different ways, but at the end of the day, it’s the programmer’s responsibility to implement the necessary level of thread safety.

What’s a singleton used for in the real world? The aforementioned *Design Patterns* book mentions some uses:

More common uses include:

The singleton pattern has acquired somewhat of a bad reputation with some people going as far as considering singleton an anti-pattern. This criticism is a bit overblown, as the pattern has legitimate uses. However, singleton does have some drawbacks all programmers should know.

Here’s a non-exhaustive list:

Whenever you find yourself with a class that should have only a single instance throughout the life of your application, that class is a great candidate for the singleton design pattern. As you’ve read in this post, the singleton pattern was created for this exact scenario, offering an easy way to ensure access to a single instance.

Unfortunately, there’s no silver bullet; the usage of singleton comes with potential pitfalls that you must be aware of.

Regardless of whether you use singletons in your application, you’ll need a solid monitoring strategy to detect any issues as early as possible. There’s where a solution like Stackify Retrace comes in handy. Stackify helps you preemptively identify performance issues, track down bottlenecks, and leverage centralized logging features with drill-down and search capabilities to uncover and quickly resolve issues with singleton, as well as other aspects of application performance. See for yourself, and start your free trial today.
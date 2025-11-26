# Java Program to Demonstrate the Nested Initialization For Singleton Class

A** ****Singleton Class** is capable of producing just a single instance. Every Singleton class has a getInstance method which returns its object. When the getInstance method is called for the first time, an object of the class is generated, stored, and then returned. On subsequent calls to getInstance, the same object generated earlier gets returned.

**Nested Initialization** can be used for making Singleton classes.

In the below implementation we are creating a Singleton class using Nested Initialization. Make the following observations:

- The default no-arg constructor of this class is made private to prevent other classes from directly accessing it and making objects of Singleton.
- The Singleton class has a static public getInstance method with Singleton as the return type. This will be used by other classes to get the object of Singleton.
- There is a
**Nested class** inside Singleton class. This Nested class has an Instance variable that stores the object of the Singleton class. - The getInstance method takes value from this Instance variable and returns it to the call site.

**Demonstration of the creation of a Singleton class using Nested Initialization**

Java
// Java Program to demonstrate Singleton Class
// using Nested Initialization
class Singleton {
// a member variable
String str = "GFG!";
// Nested class has just 1 role i.e.creation of the
// Singleton object and storing it in Instance variable
private static class Nested {
static Singleton Instance = new Singleton();
}
// The getInstance() method returns the object of
// Singleton class stored in Instance variable
public static Singleton getInstance()
{
return Nested.Instance;
}
// no-argument constructor has to be made private
// this forces other classes to use getInstance() method
// in order to obtain the instance of Singleton class
private Singleton()
{
System.out.println("Object made");
}
}
public class Main {
public static void main(String[] args)
{
Singleton obj1 = Singleton.getInstance();
Singleton obj2 = Singleton.getInstance();
// make changes to obj1.str and output obj2.str
obj1.str = "geeksforgeeks!";
System.out.println(obj2.str);
}
}


**Output**Object made
geeksforgeeks!

**Advantages of Nested Initialization:**

- Lazy loading
- Thread-Safety

**Lazy loading****:**

- Lazy loading is simply postponing the object creation until it is actually needed.
- It results in increased performance as the overhead during program startup is reduced.
- In our case, the object of the Singleton class is not created until the getInstance method is called for the first time.

**Thread-Safety:**** **Thread-Safety is essential, else multi-threaded programs can yield unexpected random results.

**A non Thread-Safe implementation of Singleton class **

Java
// Java Program to demonstrate need of Thread-Safety
class Singleton1 {
static Singleton1 obj;
private Singleton1()
{
System.out.println("Object made");
}
// This method returns obj
// If both the threads enter getInstance simultaneously
// then both see obj as null, hence 2 objects of
// Singleton1 are created this defeats purpose of
// Singleton class
static Singleton1 getInstance()
{
if (obj == null)
obj = new Singleton1();
return obj;
}
}
public class Main {
public static void main(String[] args)
{
// Thread 1 will call getInstance
Thread t1 = new Thread(new Runnable() {
public void run()
{
Singleton1 a = Singleton1.getInstance();
}
});
// Thread 2 will also call getInstance
Thread t2 = new Thread(new Runnable() {
public void run()
{
Singleton1 b = Singleton1.getInstance();
}
});
// Start both the Threads
t1.start();
t2.start();
}
}


**Output**Object made
Object made

- The
**Nested Initialization** is **thread-safe**, this is because unlike the above implementation in Nested Initialization the getInstance method does not create an object, it simply returns it. The object is created when the Nested Class is initialized and this happens only once when the getInstance method is called for the very first time.

**Thread-Safe implementation of Singleton class**

Java
// Java Program to demonstrate Thread-Safety
// in NestedInitialization
class Singleton {
private static class Nested {
static Singleton Instance = new Singleton();
}
// This method returns Object, does not create it
// Object is created on initialization of Nested class
// which happens only once.
public static Singleton getInstance()
{
return Nested.Instance;
}
private Singleton()
{
System.out.println("Object made");
}
}
public class SingletonDemo {
public static void main(String[] args)
{
// Thread 1 will call getInstance
Thread t1 = new Thread(new Runnable() {
public void run()
{
Singleton a = Singleton.getInstance();
}
});
// Thread 2 will also call getInstance
Thread t2 = new Thread(new Runnable() {
public void run()
{
Singleton b = Singleton.getInstance();
}
});
// Start both the Threads
t1.start();
t2.start();
}
}


**Note: **In the above implementation we have achieved thread-safety without using the synchronized keyword. This is a plus point since the synchronized keyword is known to affect performance noticeably.
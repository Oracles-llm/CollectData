# Singleton Method Design Pattern in Java

In object-oriented programming, a **Java singleton class** is a class that can have only one object (an instance of the class) at a time. After the first time, if we try to instantiate the Java Singleton classes, the new variable also points to the first instance created. So, whatever modifications we do to any variable inside the class through any instance, affect the variable of the single instance created and are visible if we access that variable through any variable of that class type defined.

**Note: **While designing a singleton class then remember to make a private constructor and a static method that returns an object of this singleton class using the Lazy Initialization method.


## Purpose of Singleton Class

The primary purpose of a Java Singleton class is to restrict the limit of the number of object creations to only one. This often ensures that there is access control to resources, for example, a socket or a database connection.

**Memory Efficient:** As the object creation will take place only once instead of creating it each time a new request is made, which reduces the overhead and makes it memory efficient.**Resource Control: **Restrict the new object creation in multi-threaded and database applications mostly make use of the Singleton pattern in Java for caching, logging, thread pooling, configuration settings, etc.**Thread Safety: **For example, there is a license with us, and we have only one database connection or suppose our JDBC driver does not allow us to do multithreading, then the Singleton class comes into the picture and makes sure that at a time, only a single connection or a single thread can access the connection.

**Creating a Singleton Class in Java**

To create a singleton class, we must follow the steps, given below:

- First, we create the
**private constructor** of the singleton class which prevent from the direct instantiation. - Then create the
**static method** also called as **getInstance() **method which return the single instance of the class. This ensure that the only one object is created using lazy intialization - Store the instance in the
**private static variable** which make sure that the only single instance is created.

Example of singleton classes is **Runtime class, Action Servlet, and Service Locator**. Private constructors and factory methods are also an example of the singleton class.

## Difference Between Normal Class and Singleton Class

We can differentiate a Singleton class from the usual classes with respect to the process of instantiating the object of the class. To instantiate a normal class, we use a Java constructor. On the other hand, to instantiate a singleton class, we use the getInstance() method.

The other difference is that a normal class vanishes at the end of the lifecycle of the application while the singleton class does not destroy with the completion of an application.

There are two forms of singleton design patterns, which are:

**Early Instantiation:** The object creation takes place at the load time.**Lazy Instantiation:** The object creation is done according to the requirement.

**Implementation: **Let us briefly how the singleton class varies from the normal class in Java. Here, the difference is in terms of instantiation as for normal class we use a constructor, whereas for singleton class we use the getInstance() method which we will be peeking out in example 1 as depicted below. In general, in order to avoid confusion, we may also use the class name as the method name while defining this method which will be depicted in example 2 below as follows.

**Example 1: **Creating a singleton class using the **getInstance() method**.

Java
// Java program implementing Singleton class
// with using getInstance() method
// Helper class
class Singleton
{
// Static variable reference of single_instance
// of type Singleton
private static Singleton single_instance = null;
// Declaring a variable of type String
public String s;
// Constructor
// Here we will be creating private constructor
// restricted to this class itself
private Singleton()
{
s = "Hello I am a string part of Singleton class";
}
// Static method
// Static method to create instance of Singleton class
public static synchronized Singleton getInstance()
{
if (single_instance == null)
single_instance = new Singleton();
return single_instance;
}
}
// Main class
class Geeks
{
// Main driver method
public static void main(String args[])
{
// Instantiating Singleton class with variable x
Singleton x = Singleton.getInstance();
// Instantiating Singleton class with variable y
Singleton y = Singleton.getInstance();
// Instantiating Singleton class with variable z
Singleton z = Singleton.getInstance();
// Printing the hash code for above variable as
// declared
System.out.println("Hashcode of x is "
+ x.hashCode());
System.out.println("Hashcode of y is "
+ y.hashCode());
System.out.println("Hashcode of z is "
+ z.hashCode());
// Condition check
if (x == y && y == z) {
System.out.println(
"Three objects point to the same memory location on the heap i.e, to the same object");
}
else {
System.out.println(
"Three objects DO NOT point to the same memory location on the heap");
}
}
}


**Output**Hashcode of x is 1995265320
Hashcode of y is 1995265320
Hashcode of z is 1995265320
Three objects point to the same memory location on the heap i.e, to the same object

**Explanation:**

- In the above Java code, we use the
**getInstance()** method to instantiate the singleton class and then when we again call with new key word it return the same instance which is created only once. - The
**single_instance** is static. so it shared the shared the shared among all it's instances. That is why the object x, y and z having the same object. - Then we print the hashcode of all the object which is same which means they are sharing the same referrence and pointing to the same object.



In a singleton class, when we first-time call the **getInstance() method**, it creates an object of the class with the name single_instance and returns it to the variable. Since single_instance is static, it is changed from null to some object. Next time, if we try to call the getInstance() method since single_instance is not null, it is returned to the variable, instead of instantiating the Singleton class again. This part is done by if condition.

In the main class, we instantiate the singleton class with 3 objects x, y, and z by calling the static method getInstance(). But actually, after the creation of object x, variables y and z are pointed to object x as shown in the diagram. Hence, if we change the variables of object x, that is reflected when we access the variables of objects y and z. Also if we change the variables of object z, that is reflected when we access the variables of objects x and y.

**Example 2: **Creating a singleton class with the same method name as class.

Java
// Java program implementing Singleton class
// with method name as that of class
// Helper class
class Singleton
{
// Static variable single_instance of type Singleton
private static Singleton single_instance = null;
// Declaring a variable of type String
public String s;
// Constructor of this class
// Here private constructor is used to
// restricted to this class itself
private Singleton()
{
s = "String from Singleton class";
}
// Method
// Static method to create instance of Singleton class
public static Singleton Singleton()
{
// To ensure only one instance is created
if (single_instance == null) {
single_instance = new Singleton();
}
return single_instance;
}
}
// Main class
class Geeks
{
// Main driver method
public static void main(String args[])
{
// Instantiating Singleton class with variable x
Singleton x = Singleton.Singleton();
// Instantiating Singleton class with variable y
Singleton y = Singleton.Singleton();
// Now changing variable of instance x
// via toUpperCase() method
x.s = (x.s).toUpperCase();
// Print and display commands
System.out.println("String from x: " + x.s + ", y: " + y.s);
// Now again changing variable of instance y
y.s = (y.s).toLowerCase();
System.out.println("String from x: " + x.s + ", y: " + y.s);
}
}


**Output**String from x: STRING FROM SINGLETON CLASS, y: STRING FROM SINGLETON CLASS
String from x: string from singleton class, y: string from singleton class

**Explanation: **In the singleton class, when we first-time call **Singleton()** method, it creates an object of class Singleton with the name single_instance and returns it to the variable. Since single_instance is static, it is changed from null to some object. Next time if we try to call **Singleton()** method, since **single_instance** is not null, it is returned to the variable, instead of instantiating the Singleton class again.

Singleton Method Design Pattern in Java
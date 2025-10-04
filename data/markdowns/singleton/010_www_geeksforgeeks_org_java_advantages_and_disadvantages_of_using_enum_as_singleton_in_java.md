# Advantages and Disadvantages of using Enum as Singleton in Java

Enum Singletons are new ways of using Enum with only one instance to implement the Singleton pattern in Java. While there has been a Singleton pattern in Java for a long time, Enum Singletons are a comparatively recent term and in use since the implementation of Enum as a keyword and function from Java 5 onwards.

**Advantages of using Enum as Singleton:**

**1. Enum Singletons are easy to write:** If you have been writing Singletons before Java 5, this is by far the greatest benefit that you realize that you can have more than one instance even with double-checked locking. While this problem is solved by improving the Java memory model and guaranteeing volatile variables from Java 5 onwards, it is still difficult for many beginners to write.

Compared to double-checked locking with synchronization, Enum singletons are very easy. If you don't think that the following code for traditional singleton with double-checked locking and Enum Singletons are compared:

Singleton using Enum in Java: By default creation of the Enum instance is thread-safe, but any other Enum method is the programmer's responsibility.

public enum EasySingleton{
INSTANCE;
}

You can access it by EasySingleton.INSTANCE, far simpler than calling getInstance() function on Singleton.

**2. Enum Singletons handled Serialization by themselves**

Another problem with conventional Singletons is that they are no longer Singleton once you implement a serializable interface because the method readObject() always returns a new instance just like the Java constructor. By using the readResolve() method and discarding newly created instances, you can avoid that by substituting Singleton, as shown in the example below:

private Object readResolve(){
return INSTANCE;
}

If your Singleton Class maintains state, this can become even more complex, as you need to make them transient, but JVM guarantees serialization with Enum Singleton.

**3. Creation of Enum instance is thread-safe**

By default, the Enum instance is thread-safe, and you don't need to worry about double-checked locking.

In summary, the Singleton pattern is the best way to create Singleton in Java 5 world, given the Serialization and thread-safety guaranteed and with some line of code enum.

Java
// Java program to demonstrate the example
// of using Enum as Singleton
enum SingletonEnum {
INSTANCE;
int value;
public int getValue() {
return value;
}
public void setValue(int value) {
this.value = value;
}
}
class Main {
public static void main(String[] args) {
SingletonEnum singleton = SingletonEnum.INSTANCE;
System.out.println(singleton.getValue());
singleton.setValue(2);
System.out.println(singleton.getValue());
}
}


**Disadvantages of using Enum as a singleton:**

**1. Coding Constraints**

In regular classes, there are things that can be achieved but prohibited in enum classes. Accessing a static field in the constructor, for example. Since he's working at a special level, the programmer needs to be more careful.

**2. Serializability**

For singletons, it is very common to be stateful. In general, those singletons should not be serializable. There is no real example where transporting a stateful singleton from one VM to another VM makes sense; a singleton means "unique within a VM" not "unique in the universe"

If serialization really makes sense for a stateful singleton, the singleton should specify explicitly and accurately what it means in another VM to deserialize a singleton where there may already be a singleton of the same type.

We save some lines of code on enum, but the price is too high, we have to carry all the baggage and enum limitations, we inadvertently inherit enum "features" that have unintended consequences. A disadvantage turns out to be the only alleged benefit - automatic serializability.

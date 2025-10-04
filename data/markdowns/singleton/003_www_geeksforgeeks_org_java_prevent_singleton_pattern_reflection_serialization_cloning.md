# How to prevent Singleton Pattern from Reflection, Serialization and Cloning?

Prerequisite: Singleton Pattern In this article, we will see what various concepts can break the singleton property of a class and how to avoid them. There are mainly 3 concepts that can break the singleton property of a class. Let's discuss them one by one.

**Reflection:** Reflection can be caused to destroy singleton property of the singleton class, as shown in the following example:

Java
// Java code to explain effect of Reflection
// on Singleton property
import java.lang.reflect.Constructor;
// Singleton class
class Singleton {
// public instance initialized when loading the class
public static Singleton instance = new Singleton();
private Singleton()
{
// private constructor
}
}
public class GFG {
public static void main(String[] args)
{
Singleton instance1 = Singleton.instance;
Singleton instance2 = null;
try {
Constructor[] constructors
= Singleton.class.getDeclaredConstructors();
for (Constructor constructor : constructors) {
// Below code will destroy the singleton
// pattern
constructor.setAccessible(true);
instance2
= (Singleton)constructor.newInstance();
break;
}
}
catch (Exception e) {
e.printStackTrace();
}
System.out.println("instance1.hashCode():- "
+ instance1.hashCode());
System.out.println("instance2.hashCode():- "
+ instance2.hashCode());
}
}


**Output**instance1.hashCode():- 1995265320
instance2.hashCode():- 1746572565

After running this class, you will see that hashCodes are different which means, 2 objects of the same class are created and the singleton pattern has been destroyed.

**Overcome reflection issue:** To overcome issues raised by reflection, enums are used because java ensures internally that the enum value is instantiated only once. Since java Enums are globally accessible, they can be used for singletons. Its only drawback is that it is not flexible i.e it does not allow lazy initialization.

Java
// Java program for Enum type singleton
public enum Singleton {
INSTANCE;
}


As the constructor for an enum is **package-private** or **private access**, It automatically creates the constants that are defined at the beginning of the enum body. You cannot invoke an enum constructor yourself, so it is not possible for Reflection to utilize it. Hence, reflection can't break singleton property in the case of enums.

**Serialization:-** Serialization can also cause breakage of singleton property of singleton classes. Serialization is used to convert an object of a byte stream and save in a file or send it over a network. Suppose you serialize an object of a singleton class. Then if you de-serialize that object it will create a new instance and hence break the singleton pattern.

Java
// Java code to explain effect of
// Serialization on singleton classes
import java.io.FileInputStream;
import java.io.FileOutputStream;
import java.io.ObjectInput;
import java.io.ObjectInputStream;
import java.io.ObjectOutput;
import java.io.ObjectOutputStream;
import java.io.Serializable;
class Singleton implements Serializable {
// public instance initialized
// when loading the class
public static Singleton instance = new Singleton();
private Singleton()
{
// private constructor
}
}
public class GFG {
public static void main(String[] args)
{
try {
Singleton instance1 = Singleton.instance;
ObjectOutput out = new ObjectOutputStream(
new FileOutputStream("file.text"));
out.writeObject(instance1);
out.close();
// deserialize from file to object
ObjectInput in = new ObjectInputStream(
new FileInputStream("file.text"));
Singleton instance2
= (Singleton)in.readObject();
in.close();
System.out.println("instance1 hashCode:- "
+ instance1.hashCode());
System.out.println("instance2 hashCode:- "
+ instance2.hashCode());
}
catch (Exception e) {
e.printStackTrace();
}
}
}


**Output**instance1 hashCode:- 1721931908
instance2 hashCode:- 193064360

As you can see, the hashCode of both instances is different, hence there are 2 objects of a singleton class. Thus, the class is no more singleton.

**Overcome serialization issue:-** To overcome this issue, we have to implement the method readResolve() method.

Java
// Java code to remove the effect of
// Serialization on singleton classes
import java.io.FileInputStream;
import java.io.FileOutputStream;
import java.io.ObjectInput;
import java.io.ObjectInputStream;
import java.io.ObjectOutput;
import java.io.ObjectOutputStream;
import java.io.Serializable;
class Singleton implements Serializable {
// public instance initialized when loading the class
public static Singleton instance = new Singleton();
private Singleton()
{
// private constructor
}
// implement readResolve method
protected Object readResolve() { return instance; }
}
public class GFG {
public static void main(String[] args)
{
try {
Singleton instance1 = Singleton.instance;
ObjectOutput out = new ObjectOutputStream(
new FileOutputStream("file.text"));
out.writeObject(instance1);
out.close();
// deserialize from file to object
ObjectInput in = new ObjectInputStream(
new FileInputStream("file.text"));
Singleton instance2
= (Singleton)in.readObject();
in.close();
System.out.println("instance1 hashCode:- "
+ instance1.hashCode());
System.out.println("instance2 hashCode:- "
+ instance2.hashCode());
}
catch (Exception e) {
e.printStackTrace();
}
}
}


Output:-

instance1 hashCode:- 1550089733

instance2 hashCode:- 1550089733


Above both hashcodes are the same hence no other instance is created.

**Cloning:** Cloning is the concept to create duplicate objects. Using clone we can create copy of object. Suppose, we create clone of a singleton object, then it will create a copy that is there are two instances of a singleton class, hence the class is no more singleton.

Java
// Java code to explain cloning
// issue with singleton
class SuperClass implements Cloneable {
int i = 10;
@Override
protected Object clone()
throws CloneNotSupportedException
{
return super.clone();
}
}
// Singleton class
class Singleton extends SuperClass {
// public instance initialized when loading the class
public static Singleton instance = new Singleton();
private Singleton()
{
// private constructor
}
}
public class GFG {
public static void main(String[] args)
throws CloneNotSupportedException
{
Singleton instance1 = Singleton.instance;
Singleton instance2 = (Singleton)instance1.clone();
System.out.println("instance1 hashCode:- "
+ instance1.hashCode());
System.out.println("instance2 hashCode:- "
+ instance2.hashCode());
}
}


**Output**instance1 hashCode:- 746292446
instance2 hashCode:- 989110044

Two different hashCode means there are 2 different objects of the singleton class.

**Overcome Cloning issue: **To overcome this issue, override clone() method and throw an exception from clone method that is CloneNotSupportedException. Now, whenever user will try to create clone of singleton object, it will throw an exception and hence our class remains singleton.

Java
// Java code to explain overcome
// cloning issue with singleton
class SuperClass implements Cloneable {
int i = 10;
@Override
protected Object clone()
throws CloneNotSupportedException
{
return super.clone();
}
}
// Singleton class
class Singleton extends SuperClass {
// public instance initialized when loading the class
public static Singleton instance = new Singleton();
private Singleton()
{
// private constructor
}
@Override
protected Object clone()
throws CloneNotSupportedException
{
throw new CloneNotSupportedException();
}
}
public class GFG {
// Main driver method
public static void main(String[] args)
throws CloneNotSupportedException
{
Singleton instance1 = Singleton.instance;
Singleton instance2 = (Singleton)instance1.clone();
System.out.println("instance1 hashCode:- "
+ instance1.hashCode());
System.out.println("instance2 hashCode:- "
+ instance2.hashCode());
}
}


Output:-

Exception in thread "main" java.lang.CloneNotSupportedException

at GFG.Singleton.clone(GFG.java:29)

at GFG.GFG.main(GFG.java:38)


Now we have stopped users to create clones of the singleton class. If you don't want to throw an exception you can also return the same instance from the clone method.

Java
// Java code to explain overcome
// cloning issue with singleton
class SuperClass implements Cloneable {
int i = 10;
@Override
protected Object clone()
throws CloneNotSupportedException
{
return super.clone();
}
}
// Singleton class
class Singleton extends SuperClass {
// public instance initialized when loading the class
public static Singleton instance = new Singleton();
private Singleton()
{
// private constructor
}
@Override
protected Object clone()
throws CloneNotSupportedException
{
return instance;
}
}
// Main class
public class GFG {
// Main driver method
public static void main(String[] args)
throws CloneNotSupportedException
{
Singleton instance1 = Singleton.instance;
Singleton instance2 = (Singleton)instance1.clone();
System.out.println("instance1 hashCode:- "
+ instance1.hashCode());
System.out.println("instance2 hashCode:- "
+ instance2.hashCode());
}
}


**Output:**

instance1 hashCode:- 366712642

instance2 hashCode:- 366712642


Now, as hashcode of both instances is the same that means they represent a single instance.

# Implementation of Singleton Class in C++
A singleton class is a special type of class in object-oriented programming which can have only one object or instance at a time. In other words, we can instantiate only one instance of the singleton class. The new variable also points to the initial instance created if we attempt to instantiate the Singleton class after the first time. This is implemented by using the core concepts of object-oriented programming namely access modifiers, constructors & static methods.

**Steps to Implement Singleton Class in C++:**

- Make all the constructors of the class private.
- Delete the copy constructor of the class.
- Make a private static pointer that can point to the same class object (singleton class).
- Make a public static method that returns the pointer to the same class object (singleton class).

Below is the implementation of the singleton class in C++:

C++
// Implementation of Singleton Class
// in C++
#include <iostream>
#include <mutex>
using namespace std;
class Singleton {
private:
// Member variables
string name, loves;
// Static pointer to the Singleton instance
static Singleton* instancePtr;
// Mutex to ensure thread safety
static mutex mtx;
// Private Constructor
Singleton() {}
public:
// Deleting the copy constructor to prevent copies
Singleton(const Singleton& obj) = delete;
// Static method to get the Singleton instance
static Singleton* getInstance() {
if (instancePtr == nullptr) {
lock_guard<mutex> lock(mtx);
if (instancePtr == nullptr) {
instancePtr = new Singleton();
}
}
return instancePtr;
}
// Method to set values
void setValues(const string& name, const string& loves) {
this->name = name;
this->loves = loves;
}
// Method to print values
void print() const {
cout << name << " Loves " << loves << "." << endl;
}
};
// Initialize static members
Singleton* Singleton::instancePtr = nullptr;
mutex Singleton::mtx;
// Driver code
int main() {
Singleton* s1 = Singleton::getInstance();
s1->setValues("Manish", "GeeksForGeeks");
s1->print();
Singleton* s2 = Singleton::getInstance();
s2->setValues("Vartika", "GeeksForGeeks");
s2->print();
return 0;
}


**Output**Manish Loves GeeksForGeeks.
Vartika Loves GeeksForGeeks.

**Explanation:**

- Firstly, we made all the constructor private so that an instance of the Singleton class can't be instantiated from outside of it.
- We deleted copy constructor so that copy of the instance cannot be created.
- Created a static member
**instancePtr** and initialized it with *NULL*. It points to the instance of Singleton class. - Created a
**getInstance()** method which returns an instance of the Singleton class. It is a static method because static variables are accessed by only static methods and we have to access *instancePtr* which is a static member. - If there already exists an instance of the Singleton class then
*getInstance()* will return a pointer to that instance as we can have only one instance of the Singleton class. - If
*instancePtr == NULL* that means there exists no instance of the Singleton class. So, *getInstance()* will instantiate an instance of the Singleton class and return a pointer to it. - We cannot create an instance of the Singleton class as all constructors are private. We have to use the
*getInstance()* method to get an instance of it.

**Case 1: An instance of the Singleton Class is created beforehand.**

In this implementation, we are creating an instance of the Singleton class beforehand (i.e. initializing *instancePtr* with an instance instead of NULL using a new keyword) and returning it when *getInstance()* is invoked.

Below is the C++ program to implement the above approach:

C++
// C++ program to implement
// the above approach
#include <bits/stdc++.h>
using namespace std;
class Singleton{
private:
// member variables
string name, loves;
// initializing instancePtr with an
// instance(outside of this class we
// are initializing instancePtr with
// an object.)
static Singleton *instancePtr;
// Default constructor
Singleton()
{
}
public:
// deleting copy constructor.
Singleton(const Singleton &obj) = delete;
// returns instancePtr and instancePtr
// is pointing to an instance of
// Singleton class
static Singleton *getInstance()
{
return instancePtr;
}
void setValues(string name,
string loves)
{
this->name = name;
this->loves = loves;
}
void print()
{
cout << name << " Loves " <<
loves << "." << endl;
}
};
// initializing instancePtr with an instance
Singleton *Singleton ::instancePtr
= new Singleton();
// Driver code
int main()
{
Singleton *gfg
= Singleton::getInstance();
gfg->setValues("Learner",
"GeeksForGeeks");
gfg->print();
cout << "Address of gfg : " <<
gfg << endl;
// for output indentation
cout << endl;
Singleton *geeksForGeeks
= Singleton::getInstance();
geeksForGeeks->setValues("Everyone",
"GeeksForGeeks");
geeksForGeeks->print();
cout << "Address of geeksForGeeks : " <<
geeksForGeeks << endl;
return 0;
}


**Output**Learner Loves GeeksForGeeks.
Address of gfg : 0xd63010
Everyone Loves GeeksForGeeks.
Address of geeksForGeeks : 0xd63010

**Explanation:**

- Firstly, we made all the constructor private so that an instance of the Singleton class can't be instantiated from outside of it.
- We deleted copy constructor so that copy of the instance cannot be created.
- Created a static member
*instancePtr* and initialized it with an instance using the new keyword. It is pointing to the instance of the Singleton class. - Created a
**getInstance()** method which returns *instancePtr* of the Singleton class. It is a static method because static variables are accessed by only static methods and we have to access *instancePtr* which is a static member. - We cannot create an instance of the Singleton class as all constructors are private. We have to use the
*getInstance()* method to get an instance of it.

**Case 2: When the instance is created without using the ****getInstance()**** method to create the Singleton Class.**

Below is the C++ program to implement the singleton class without using getinstance() method:

C++
// C++ program to create singleton class
// without using getinstance() method
#include<bits/stdc++.h>
using namespace std;
class Singleton{
private:
// member variables
string name, loves;
// static pointer which points
// to the instance of this class.
static Singleton *instancePtr;
// Default constructor
Singleton()
{
}
//same as above
Singleton(string name,
string loves)
{
this->name = name;
this->loves = loves;
}
public:
// deleting copy constructor.
Singleton(const Singleton &obj) = delete;
static Singleton *getInstance()
{
// If there is no instance of class
// then we can create an instance.
if(instancePtr == NULL)
{
// We can access private members
// within the class.
instancePtr = new Singleton();
// returning the instance pointer.
return instancePtr;
}
else
{
// if instancePtr != NULL that means
// the class already has an instance.
// So, we are returning that instance
// and not creating new one.
return instancePtr;
}
}
// sets values of member variables.
void setValues(string name,
string loves)
{
this->name = name;
this->loves = loves;
}
// prints values of member variables.
void print()
{
cout << name << " Loves " <<
loves << "." << endl;
}
};
// initializing instancePtr with NULL
Singleton *Singleton ::instancePtr = NULL;
// Driver code
int main()
{
// Gives error
Singleton *geeksForGeeks
= new Singleton();
// Cannot create object of Singleton class
// as default constructor is private &
// no method is used to access it.
return 0;
}



**Output**

**Explanation: **As shown in the above output we are not able to instantiate an instance of the Singleton class by using the constructor. We can have only one instance of the Singleton class which we will get by using the *getInstance()* method.

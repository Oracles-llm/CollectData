# Template method pattern

This article includes a list of general references, but it lacks sufficient corresponding inline citations. (March 2012) |

In object-oriented programming, the **template method** is one of the behavioral design patterns identified by Gamma et al.[1] in the book *Design Patterns*. The template method is a method in a superclass, usually an abstract superclass, and defines the skeleton of an operation in terms of a number of high-level steps. These steps are themselves implemented by additional *helper methods* in the same class as the *template method*.

The *helper methods* may be either *abstract methods*, in which case subclasses are required to provide concrete implementations, or *hook methods,* which have empty bodies in the superclass. Subclasses can (but are not required to) customize the operation by overriding the hook methods. The intent of the template method is to define the overall structure of the operation, while allowing subclasses to refine, or redefine, certain steps.[2]

## Overview

[edit]This pattern has two main parts:

- The "template method" is implemented as a method in a base class (usually an abstract class). This method contains code for the parts of the overall algorithm that are invariant. The template ensures that the overarching algorithm is always followed.
[1]In the template method, portions of the algorithm that may*vary*are implemented by sending self messages that request the execution of additional*helper*methods. In the base class, these helper methods are given a default implementation, or none at all (that is, they may be abstract methods). - Subclasses of the base class "fill in" the empty or "variant" parts of the "template" with specific algorithms that vary from one subclass to another.
[3]It is important that subclasses do*not*override the*template method*itself.

At run-time, the algorithm represented by the template method is executed by sending the template message to an instance of one of the concrete subclasses. Through inheritance, the template method in the base class starts to execute. When the template method sends a message to self requesting one of the helper methods, the message will be received by the concrete sub-instance. If the helper method has been overridden, the overriding implementation in the sub-instance will execute; if it has not been overridden, the inherited implementation in the base class will execute. This mechanism ensures that the overall algorithm follows the same steps every time while allowing the details of some steps to depend on which instance received the original request to execute the algorithm.

This pattern is an example of inversion of control because the high-level code no longer determines what algorithms to run; a lower-level algorithm is instead selected at run-time.

Some of the self-messages sent by the template method may be to *hook methods.* These methods are implemented in the same base class as the template method, but with empty bodies (i.e., they do nothing). Hook methods exist so that subclasses can override them, and can thus fine-tune the action of the algorithm *without* the need to override the template method itself. In other words, they provide a "hook" on which to "hang" variant implementations.

## Structure

[edit]### UML class diagram

[edit]In the above UML class diagram, the `AbstractClass`

defines a `templateMethod()`

operation that defines the skeleton (template) of a behavior by

- implementing the invariant parts of the behavior and
- sending to
**self**the messages`primitive1()`

and`primitive2()`

, which, because they are implemented in`SubClass1`

, allow that subclass to provide a variant implementation of those parts of the algorithm.

## Usage

[edit]The *template method* is used in frameworks, where each implements the invariant parts of a domain's architecture, while providing hook methods for customization. This is an example of inversion of control. The template method is used for the following reasons.[3]

- It lets subclasses implement varying behavior (through overriding of the hook methods).
[6] - It avoids duplication in the code: the general workflow of the algorithm is implemented once in the abstract class's template method, and necessary variations are implemented in the subclasses.
[6] - It controls the point(s) at which specialization is permitted. If the subclasses were to simply override the template method, they could make radical and arbitrary changes to the workflow. In contrast, by overriding only the hook methods, only certain specific details of the workflow can be changed,
[6]and the overall workflow is left intact.

### Use with code generators

[edit]The template pattern is useful when working with auto-generated code. The challenge of working with generated code is that changes to the source code will lead to changes in the generated code; if hand-written modifications have been made to the generated code, these will be lost. How, then, should the generated code be customized?

The Template pattern provides a solution. If the generated code follows the template method pattern, the generated code will all be an abstract superclass. Provided that hand-written customizations are confined to a subclass, the code generator can be run again without risk of over-writing these modifications. When used with code generation, this pattern is sometimes referred to as the generation gap pattern.[7]

## C++ example

[edit]This C++23 implementation is based on the pre C++98 implementation in the book.

```
import std;
using std::unique_ptr;
// abstract class
class View {
private:
void setFocus() {
std::println("View::setFocus called");
}
void resetFocus() {
std::println("View::resetFocus called");
}
public:
// defines abstract primitive operations that concrete subclasses define to implement steps of an algorithm.
virtual void doDisplay() = 0;
// implements a template method defining the skeleton of an algorithm. The template method calls primitive operations as well as operations defined in AbstractClass or those of other objects.
void display() {
setFocus();
doDisplay();
resetFocus();
}
virtual ~View() = default;
};
// concrete class
class MyView : public View {
public:
// implements the primitive operations to carry out subclass-specific steps of the algorithm.
void doDisplay() override {
// render the view's contents
std::println("MyView::doDisplay called");
}
};
int main(int argc, char* argv[]) {
unique_ptr<View> myview = std::make_unique<MyView>();
myview->display();
}
```

The program output is

```
View::setFocus called
MyView::doDisplay called
View::resetFocus called
```

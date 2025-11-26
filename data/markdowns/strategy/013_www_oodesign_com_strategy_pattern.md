There are common situations when classes differ only in their behavior. For this cases is a good idea to isolate the algorithms in separate classes in order to have the ability to select different algorithms at runtime.

Define a family of algorithms, encapsulate each one, and make them interchangeable. Strategy lets the algorithm vary independently from clients that use it.

The implementation of the strategy design pattern consists of 2 type of classes: the **Strategy**,
which encapsulates interchangeable algorithms and the **Context** which acts as the orchestrator
that delegates to the strategy, allowing behaviors to be switched dynamically without
altering the clients that rely on them.


**IStrategy** defines an interface common to all supported algorithms. Each algorithm/behavior is defined in concrete
implementation of the strategy interface: ConcreteStrategyA, ConcreteStrategyB, ConcreteStrategyC. The Context uses this interface
to call the implemented algorithms.

**ConcreteStrategy** - each concrete strategy implements an algorithm/behavior.

The **Context** objects contains a reference to the **ConcreteStrategy** that should be
used. When an operation is required then the algorithm is run from the strategy object. The **Context** is
not aware of the strategy implementation. If necessary, addition objects can be defined to pass data from context
object to strategy.

The context object receives requests from the client and delegates them to the strategy object. Usually the ConcreteStartegy is created by the client and passed to the context. From this point the clients interact only with the context.

Let's consider the following class diagram:

Let's consider an application used to simulate and study robots interaction. For the beginning a simple application is created to simulate an arena where robots are interacting. We have the following classes:

**IBehaviour** (**Strategy**) - an interface that defines the behavior of a robot

**Concrete Strategies**: **AggressiveBehaviour**, **DefensiveBehaviour**,
**NormalBehaviour**; each of them defines a specific behavior. In order to decide
the action this class needs information that is passed from robot sensors like position, close obstacles, etc.

**Robot** - The robot is the **context** class. It keeps or gets context information such as position, close obstacles
, etc, and passes necessary information to the Strategy class.

In the main section of the application the several robots are created and several different behaviors are created. Each robot has a different behavior assigned: 'Big Robot' is an aggressive one and attacks any other robot found, 'George v.2.1' is really scared and run away in the opposite direction when it encounter another robot and 'R2' is pretty calm and ignore any other robot. At some point the behaviors are changed for each robot.

Usually each strategy need data from the context have to return some processed data to the context. This can be achieved in 2 ways.

When data should be passed the drawbacks of each method should be analyzed. For example, if some classes are created to encapsulate additional data, a special care should be paid to what fields are included in the classes. Maybe in the current implementation all required fields are added, but maybe in the future some new strategy concrete classes require data from context which are not include in additional classes. Another fact should be specified at this point: it's very likely that some of the strategy concrete classes will not use field passed to the in the additional classes.

On the other side, if the context object is passed to the strategy then we have a tighter coupling between strategy and context.

The strategies can be defined as a hierarchy of classes offering the ability to extend and customize the existing algorithms from an application. At this point the composite design pattern can be used with a special care.

It's possible to implement a context object that carries an implementation for default or a basic algorithm. While running it, it checks if it contains a strategy object. If not it will run the default code and that's it. If a strategy object is found, it is called instead (or in addition) of the default code. This is an elegant solution to exposing some customization points to be used only when they are required. Otherwise the clients don't have to deal with Strategy objects.

In the classic implementation of the pattern the client should be aware of the strategy concrete classes. In order to decouple the client class from strategy classes is possible to use a factory class inside the context object to create the strategy object to be used. By doing so the client has only to send a parameter (like a string) to the context asking to use a specific algorithm, being totally decoupled of strategy classes.

Both of the patterns have the same UML diagram. But they differ in their intent since the strategy is related with the behavior and bridge is for structure. Further more, the coupling between the context and strategies is tighter than the coupling between the abstraction and implementation in the bridge pattern.

The strategy design pattern splits the behavior (there are many behaviors) of a class from the class itself. This has some advantages, but the main draw back is that a client must understand how the S trategies differ. Since clients get exposed to implementation issues the strategy design pattern should be used only when the variation in behavior is relevant to them.
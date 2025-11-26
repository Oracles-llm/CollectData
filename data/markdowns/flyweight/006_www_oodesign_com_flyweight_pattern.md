
The **Flyweight Pattern** is a structural design pattern that allows programs to efficiently share a large number of objects by minimizing memory usage. It achieves this by separating the intrinsic state (shared) from the extrinsic state (external) of the object.

Some programs require a large number of objects that have some shared state among them. Consider for example a game of war, where there is a large number of soldier objects; a soldier object maintain the graphical representation of a soldier, soldier behavior such as motion, and firing weapons, in addition soldier's health and location on the war terrain. Creating a large number of soldier objects is a necessity however it would incur a huge memory cost. Note that although the representation and behavior of a soldier is the same their health and location can vary greatly.


A client needs a flyweight object; it calls the factory to get the flyweight object. The factory checks a pool of flyweights to determine if a flyweight object of the requested type is in the pool, if there is, the reference to that object is returned. If there is no object of the required type, the factory creates a flyweight of the requested type, adds it to the pool, and returns a reference to the flyweight. The flyweight maintains intrinsic state (state that is shared among the large number of objects that we have created the flyweight for) and provides methods to manipulate external state (State that vary from object to object and is not common among the objects we have created the flyweight for).

The flyweight pattern applies to a program using a huge number of objects that have part of their internal state in common where the other part of state can vary. The pattern is used when the larger part of the object's state can be made extrinsic (external to that object).

The war game instantiates 5 Soldier clients, each client maintains its internal state which is extrinsic to the soldier flyweight. And Although 5 clients have been instantiated only one flyweight Soldier has been used.

Consider a coffee shop that offers customization for drinks. The intrinsic state might be the base drink like "latte" or "cappuccino," while the extrinsic state can be the customizations like "extra shot" or "almond milk." Instead of creating a unique object for every possible combination, the coffee shop can use a base drink (intrinsic) and apply customizations (extrinsic) as needed.

Object oriented text editors need to create Character Objects to represent each character that is in the document. A Character object maintains information about what is the character, what is its font, what is the size of the character, as well as character location inside the document. A document typically consists of extremely large number of character objects which requires large memory. Note that the number of characters in general (Digits, Letters, Other special characters) is known and is fixed, and the fonts that can be applied to each character are also known, thus by creating a Letter flyweight that maintains Character Type (letter, digit, etc, ...), as well as font, and by creating a Letter Client object that only maintains each character's location inside the document, we have reduced the editor's memory requirements drastically.

Using the Flyweight pattern can offer significant memory savings, especially in scenarios where programs need to manage a large number of objects that share considerable amounts of information. However, it's essential to be aware of potential pitfalls and challenges:

It's crucial to weigh these potential challenges against the benefits the Flyweight pattern offers. Properly analyzing the problem domain and understanding the pattern can help in its successful implementation.

Flyweight pattern saves memory by sharing flyweight objects among clients. The amount of memory saved generally depends on the number of flyweight categories saved (for example a soldier category and a lieutenant category as discussed earlier).

**Factory and Singleton patterns** - Flyweights are usually created using a factory and the singleton is applied to that factory so that for each type or category of flyweights a single instance is returned.

**State and Strategy Patterns** - State and Strategy objects are usually implemented as Flyweights.

Games with graphics as discussed with the War Game Example

Text Editors as discussed in the Text Editors example.
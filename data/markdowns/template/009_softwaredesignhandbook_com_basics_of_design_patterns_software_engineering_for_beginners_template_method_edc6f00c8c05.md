# Basics of Design Patterns: Template Method ☕

## Create basic structures for algorhitmns in one main abstract class

Template Method is a Design Pattern that helps you create a structure for an algorithm in one main abstract class. You can then make changes to specific steps of the algorithm in other classes, without breaking the main structure.

## Real-World Analogy 🌍

The main template for making coffee involves coffee grounds, placing filter and then pouring hot water. However, there are different variations of coffee that use different types of coffee beans, have different amounts of grounds and sugar, or require the addition of milk or cream.

Each coffee-making step, such as boiling water, grounding coffee, adding sugar and adding milk can be slightly changed to make the resulting coffee a bit different from the others.

## Problem 🤔

Let’s say you’re making an app that can read different types of documents. This app can help users find important information in documents, even if they’re in different formats like .pdf, .doc, or .csv.

When you first released the app, it only worked with .doc-files. But then you added .csv support in the next update. And later, you added .pdf support.

At a certain point, you realized that there was a lot of similar code in all the classes created. Although each class had different code to handle different data formats, the code for analyzing and processing the data was almost identical. So, you thought it would be great to remove the duplicated code, yet keeping the structure of the algorithm unchanged.

Another issue you noticed was that the client code that used these classes had a lot of conditionals to decide which class to use. To make things simpler and eliminate the conditionals, you could create a common interface or base class for all three processing classes. This would allow you to use polymorphism in client code and call methods on a processing object without having to worry about which specific class it belongs to.

## Solution 💡

The *Template Pattern* allows to create a joint base class for all DataMiner implementations. Differences to the base class will be implemented in concrete implementation classes.

`/** GOOD EXAMPLE: DataMinerBase and specific implementations */`


public abstract class DataMinerBase {

public FileStream OpenFile(string fullPath)

{

// implementation

}



public AnalyzedData AnalyzeData(InterpretedData interpretedData)

{

// implementation

}



public void SaveData(AnalyzedData analyzedData)

{

// implementation

}



public abstract RawData ExtractData(FileStream fileStream);

public abstract InterpretedData InterpretData(RawData rawData);


// generic 'workflow' for data extraction

public void MineData(string fullPath)

{

var file = OpenFile(fullPath);

var rawData = ExtractData(file);

var data = InterpretData(rawData);

var analysis = AnalyzeData(data);



SaveData(analysis);

}

}



public sealed class DataMinerDoc : DataMinerBase {

public override RawData ExtractData(FileStream fileStream)

{

// doc extraction

}



public override InterpretedData InterpretData(RawData rawData)

{

// doc interpretation

}

}



public sealed class DataMinerCsv : DataMinerBase {

public override RawData ExtractData(FileStream fileStream)

{

// csv extraction

}



public override InterpretedData InterpretData(RawData rawData)

{

// csv interpretation

}

}

## Structure 🏗️

- The
**Abstract Class**is a type of code that has a set of steps to complete a task, like a recipe with different instructions. The main method, which is called the template method, follows these steps in a specific order. **Concrete Classes**can override all of the steps, but not the template methods themselves.

## How to Implement

To implement the* Template Design Pattern*, you’ll need to create both an

- abstract class and
- concrete subclass.

In the example of travel planning, the abstract class (*TravelPlanner*) will contain the basic workflow for planning trips, while the concrete subclasses (such as *TravelPlannerTrain *or *TravelPlannerBike*) will contain any overridden or additional methods required for each specific implementation.

It’s possible to create new concrete subclasses that aren’t covered by the abstract base implementation.

## Pros and Cons

**Pros**

✅ *Robust Code. *You can let clients override only certain parts of a large algorithm, making them less affected by changes that happen to other parts of the algorithm.

✅ *Deduplication. *You can pull the duplicate code into a superclass.

**Cons**

❌ *Limitations. *Some clients may be limited by the provided skeleton of an algorithm.

❌ *Liskov Substitution Principle. *You might violate the Liskov Substitution Principle by suppressing a default step implementation via a subclass.

❌* Maintainability.* Template methods tend to be harder to maintain the more steps they have.

## Relation with other patterns

**The***Factory pattern*comes from the Template pattern, used in object-oriented programming. It’s a step within a larger Template Method.*Strategy Pattern*lets you customize code at the object level, making it more adaptable.**The**can be used with the Observer pattern to ensure consistency and lower unnecessary processing.*Template pattern***The**can be combined with the Template pattern to add or remove features.*Decorator pattern***The**pattern is related to the*Hook and Template Method**Template pattern*, creating a structured framework that subclasses can fill in.**The***Composite pattern**i*nvolves defining hierarchical structures, which can be done with the Template pattern by allowing subclasses to complete the details.

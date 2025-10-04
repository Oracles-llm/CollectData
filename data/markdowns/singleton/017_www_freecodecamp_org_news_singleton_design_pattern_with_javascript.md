## What is the Singleton Design Pattern?

*Singleton design pattern exposes a single instance that can be used by multiple components*

Singleton is a design pattern that tells us that we can create only one instance of a class and that instance can be accessed globally.

This is one of the basic types of design pattern. It makes sure that the class acts as a single source of entry for all the consumer components that want to access this state. In other words, it provides a common entry point for using global state.

So a singleton class should be one which:

Ensures that it creates only one instance of the class

Provides a global access point to the state.

Makes sure that the instance is only created the first time.


### Example of the Singleton Design Pattern

To understand this concept in a better way, let's look at an example. This example is a simple React application that demonstrates how the global state value is used across the components, how it is being changed, and how the same value gets updated in all the components. Let's get started.

Before we start with the actual implementation, let's have a look at the folder structure:

```
.
├── index.html
├── package.json
└── src
├── componentA.js
├── componentB.js
├── globalStyles.js
├── index.js
├── styles.css
└── utilities.js
```


Here are the details of each file:

`componentA.js`

is a consumer component that uses the singleton class to access the global state object and manipulate it.`componentB.js`

is similar to above component, as it has to access the global state object and can manipulate it.`globalStyles.js`

is a module that consists of the singleton class and exports the instance of this class.`index.js`

manages global JS operations, that is JavaScript changes that are required for other DOM elements.`styles.css`

manages the styling of the application. Consists of basic CSS.`utilities.js`

is a module that exports some utility functions.`index.html`

consists of HTML code for the components that are required in the project.`package.json`

is a boilerplate configuration emitted by the`npm init`

command.

Now that we know what each file does, we can start off by implementing them one by one.

But before we dive into this example, we need to understand the code flow. The aim of our example is to build a JavaScript application that demonstrates how the global style `color`

is consumed by each of the components and how each component changes it.

Each component consists of a `color-picker`

. When you change the global style `color`

property via the color picker present inside each component, it automatically appears in other components and in the global state.

First, let's create a file: `index.html`

. Then paste the below code into this file:

```
<!DOCTYPE html>
<html>
<head>
<title>Parcel Sandbox</title>
<meta charset="UTF-8" />
<link rel="stylesheet" href="./src/styles.css" />
</head>
<body>
<div class="global-state">
<h3>Global State</h3>
<h4>Color</h4>
<span id="selected-color"></span>
</div>
<div class="contents">
<div class="component-a">
<strong>Component A</strong>
<div>Pick color</div>
<span id="selected-color">black</span>
<input type="color" id="color-picker-a" />
</div>
<div class="component-b">
<strong>Component B</strong>
<div>Pick color</div>
<span id="selected-color">black</span>
<input type="color" id="color-picker-b" />
</div>
</div>
<script src="src/index.js"></script>
<script src="src/componentA.js"></script>
<script src="src/componentB.js"></script>
</body>
</html>
```


Here at the top, we load our CSS via `<link rel="stylesheet" href="./src/styles.css" />`

.

Then we have divided our application in two parts via two classes:

`.global-state`

: This will represent the HTML code for showcasing the current global state of the application.`.contents`

: This will represent the HTML code that represents the two components.

Each of the components (`component-a`

and `component-b`

) has a color picker input element.

Both of these components have a `span`

with class `selected-color`

element that will help display the current value of global state variable `color`

.

As you can see on a change of the color picker inside `componentA`

, the following values are also changing:

Value inside the

`.selected-color`

span element inside the`componentB`

and Global state.Value of the color picker of

`componentA`

and`componentB`

.

We will see later how all these values are changing. But for now it is important for us to understand that if we change the global state value from one component, then the singleton classes make sure that the instance value is updated and all the components that are consuming this instance get the same value since they are referring to the same instance.

Next, we create a file named `globalStyles.js`

. Copy-paste the below code in it:

```
let instance;
let globalState = {
color: ""
};
class StateUtility {
constructor() {
if (instance) {
throw new Error("New instance cannot be created!!");
}
instance = this;
}
getPropertyByName(propertyName) {
return globalState[propertyName];
}
setPropertyValue(propertyName, propertyValue) {
globalState[propertyName] = propertyValue;
}
}
let stateUtilityInstance = Object.freeze(new StateUtility());
export default stateUtilityInstance;
```


The above piece of code is a module that has a singleton class `StateUtility`

and default exports the instance of the same class.

Let's dive deeper into the class `StateUtility`

to understand how it resolves to become a singleton class:

It consists of

`constructor`

and two class methods called`getPropertyByName`

and`setPropertyValue`

. Both of these class method are pretty self explanatory: one gets the property's value and the other sets its value.Next, we have the

`constructor`

function. It is a function that gets invoked whenever we create a new of object of this class.But here is a catch: for a class to be a singleton we need to make sure that it creates only one instance, and that's all.

To make sure that this happens, we simply create a global variable called

`instance`

. We define it at the top of the module. This variable acts as a checker. We add a condition in the`constructor`

function such that if`instance`

variable has any value (that is, the object of the`StateUtility`

class) then throw an error or else assign`instance`

to the current class instance (the`this`

object).In this example, we implemented the class

`StateUtility`

so that it can expose and alter the`globalState`

variable.We make sure that we don't expose the

`globalState`

. We expose them using the class methods of`StateUtility`

. In this way, we protect the global state from being altered directly.Finally, we create the instance of the class as follows:

`let stateUtilityInstance = Object.freeze(new StateUtility());`

.We have used

`Object.freeze`

so that no other class/component/module is able to modify the exposed`stateUtilityInstance`

.

Then let's create a file called `componentA.js`

inside the `src`

folder. Copy-paste the below code in this file:

```
import {
setAllSelectedColor
} from "./utilities";
import globalStyle from "./globalStyles";
// Get respective dom elements
const selectedColor = document.querySelectorAll("#selected-color");
const colorPickerA = document.getElementById("color-picker-a");
const colorPickerB = document.getElementById("color-picker-b");
// Event handler whenever a change event occurs
colorPickerA.onchange = (event) => {
// set the color property of the global state with current color picker's value;
globalStyle.setPropertyValue("color", event.target.value);
const color = globalStyle.getPropertyByName("color");
// A function thats sets the value of all the #selection-color dom elements;
setValueOfSimilarElements(selectedColor, color);
// make sure to set the component B's color picker value is set to color picker A;
// this is done to make sure that both of the color picker have same value on change;
colorPickerB.value = color;
};
```


Here is the breakdown of the above piece of code:

The aim of this code is to make sure that we attach the

`onChange`

handler for the color picker that is present inside the`component-a`

. In this case, componentA's color picker is identified by id:`#color-picker-a`

.We need to make sure that this handler:

Sets the value for the property color of the globalState.

Fetches the same property again.

Applies the same value to different areas of the DOM.

Also makes sure that we set the other color picker's value to the global state.



Now, let's take a look at all these steps one-by-one:

First, let's fetch all the required DOM elements.

What we are planning here is to update all the color pickers and span elements with id

`#selected-color`

with the value of the current globalState property color whenever the on change event occurs.In case of

`componentA`

, once we change the color via the color picker we need to update the same value in 2 span elements (`#selected-color`

) – that is, one span element of`componentB`

and one span element present in the`.global-state`

div container.We do this because we want to keep all the components in sync and demosntrate that the value of the global state remains the same across all the components.

We then go ahead and update the

`color`

property of the global state using the`StateUtility`

's class method`setPropertyValue`

. We pass on to it`event.target.value`

as this contains the current value present inside the`#color-picker-a`

color picker input.Once the value is set, we fetch the same property again by using

`getPropertyByName`

. We do this to demonstrate that the property`color`

of the global state has been updated and is ready to be used.Then, we use the

`setValueOfSimilarElements`

utility function to update all the elements that are having same class/id name with some value. In this case we update all the`#selected-color`

elements with value`color`

.Finally, we update the the value of the opposite color picker, that is componentB's color picker

`#color-picker-b`

.

We do the same thing for `componentB`

. We create a file called `componentB.js`

and update it with the following code:

```
import {
setValueOfSimilarElements
} from "./utilities";
import globalStyle from "./globalStyles";
// Get respective dom elements
const selectedColor = document.querySelectorAll("#selected-color");
const colorPickerA = document.getElementById("color-picker-a");
const colorPickerB = document.getElementById("color-picker-b");
/**
* Event handler whenever a change event occurs
*/
colorPickerB.onchange = (event) => {
// set the color property of the global state with current color picker's value;
globalStyle.setPropertyValue("color", event.target.value);
const color = globalStyle.getPropertyByName("color");
// A function thats sets the value of all the #selection-color dom elements
setValueOfSimilarElements(selectedColor, color);
// make sure to set the component A's color picker value is set to color picker B;
// this is done to make sure that both of the color picker have same value on change;
colorPickerA.value = color;
};
```


We do the same thing as of what we did inside the `componentA`

file, but in this case we update the value of the color picker present inside `componentA`

(that is, we update the value of element `#color-picker-a`

).

Here is how our application will look like:


## Pros and Cons of the Singleton Design Pattern

Here are some of the pros of using the Singleton design pattern:

It makes sure that only a single instance of the class is created.

We get a single access point to the instance that can be accessed globally.


Here are some cons of the Singleton design pattern:

It violates the single responsibility principle. That is, it tries to solve two problems at the same time. It tries to solve the following problems:

*Ensure that a class will have only one instance*, and*assigning a global access point to the singleton class instance.*It is difficult to write unit test cases for singleton classes. This is because the order of execution can change the value present in the global state, so the order of execution is important.

While writing unit tests, there is a risk of another component or a module might be changing the global state value/instance. In such scenarios, it becomes difficult to debug the error.


## Summary

The singleton design pattern can be useful in creating a global state that can be accessed by any component.

So to talk about singleton pattern in brief:

It is a pattern that restricts the class to create only one instance.

Singleton pattern can be considered the basics of global state management libraries such Redux or React Context.

They can be accessed globally and acts as a single access point for accessing the global state.


That's all.

Thank you for reading!
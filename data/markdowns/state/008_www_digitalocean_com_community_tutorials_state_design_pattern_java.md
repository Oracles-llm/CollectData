State design pattern is one of the behavioral design pattern. State design pattern is used when an Object change its behavior based on its internal state.

If we have to change the behavior of an object based on its state, we can have a state variable in the Object. Then use **if-else** condition block to perform different actions based on the state. State design pattern is used to provide a systematic and loosely coupled way to achieve this through `Context`

and `State`

implementations. State Pattern **Context** is the class that has a State reference to one of the concrete implementations of the State. Context forwards the request to the state object for processing. Let’s understand this with a simple example. Suppose we want to implement a TV Remote with a simple button to perform action. If the State is ON, it will turn on the TV and if state is OFF, it will turn off the TV. We can implement it using if-else condition like below; `TVRemoteBasic.java`


```
package com.journaldev.design.state;
public class TVRemoteBasic {
private String state="";
public void setState(String state){
this.state=state;
}
public void doAction(){
if(state.equalsIgnoreCase("ON")){
System.out.println("TV is turned ON");
}else if(state.equalsIgnoreCase("OFF")){
System.out.println("TV is turned OFF");
}
}
public static void main(String args[]){
TVRemoteBasic remote = new TVRemoteBasic();
remote.setState("ON");
remote.doAction();
remote.setState("OFF");
remote.doAction();
}
}
```


Notice that client code should know the specific values to use for setting the state of remote. Further more if number of states increase then the tight coupling between implementation and the client code will be very hard to maintain and extend. Now we will use State pattern to implement above TV Remote example.

First of all we will create State interface that will define the method that should be implemented by different concrete states and context class. `State.java`


```
package com.journaldev.design.state;
public interface State {
public void doAction();
}
```


In our example, we can have two states - one for turning TV on and another to turn it off. So we will create two concrete state implementations for these behaviors. `TVStartState.java`


```
package com.journaldev.design.state;
public class TVStartState implements State {
@Override
public void doAction() {
System.out.println("TV is turned ON");
}
}
```


`TVStopState.java`


```
package com.journaldev.design.state;
public class TVStopState implements State {
@Override
public void doAction() {
System.out.println("TV is turned OFF");
}
}
```


Now we are ready to implement our Context object that will change its behavior based on its internal state.

`TVContext.java`


```
package com.journaldev.design.state;
public class TVContext implements State {
private State tvState;
public void setState(State state) {
this.tvState=state;
}
public State getState() {
return this.tvState;
}
@Override
public void doAction() {
this.tvState.doAction();
}
}
```


Notice that Context also implements State and keep a reference of its current state and forwards the request to the state implementation.

Now let’s write a simple program to test our state pattern implementation of TV Remote. `TVRemote.java`


```
package com.journaldev.design.state;
public class TVRemote {
public static void main(String[] args) {
TVContext context = new TVContext();
State tvStartState = new TVStartState();
State tvStopState = new TVStopState();
context.setState(tvStartState);
context.doAction();
context.setState(tvStopState);
context.doAction();
}
}
```


Output of above program is same as the basic implementation of TV Remote without using state pattern.

The benefits of using State pattern to implement polymorphic behavior is clearly visible. The chances of error are less and it’s very easy to add more states for additional behavior. Thus making our code more robust, easily maintainable and flexible. Also State pattern helped in avoiding if-else or switch-case conditional logic in this scenario. State Pattern is very similar to Strategy Pattern, check out **Strategy Pattern in Java**. Thats all for State design pattern in java, I hope you liked it.

Thanks for learning with the DigitalOcean Community. Check out our offerings for compute, storage, networking, and managed databases.

Java and Python Developer for 20+ years, Open Source Enthusiast, Founder of https://www.askpython.com/, https://www.linuxfordevices.com/, and JournalDev.com (acquired by DigitalOcean). Passionate about writing technical articles and sharing knowledge with others. Love Java, Python, Unix and related technologies. Follow my X @PankajWebDev

Great explanation, but it’s little bit confusing where it changes the object alternative.

- Neal

Hi and thanks for the nice post. The thing that I didn’t understand is what is the purpose of the context its only job is to call doAction() of the provided state, why don’t client code call doAction() of state instead, why do I need to create a Context that its only job is to call doAction() ? Thanks

- Adelin

According to me, this is an anti-pattern. This is like having a method whith a boolean parameter and 2 actions in it, depending on this boolean. It doesn’t respect the seperation of concerns and the single responsability principle : 1 method for 1 action. If i need to do the action 1 in a case and the action 2 in another case i’ll create action 1 and action2 méthods. With the same example : method 1 : public boolean isTheTvOn(); method 2 : public void turnOnTheTv(); method 3 : public void turnOffTheTv(); and determine the action to do in a service layer

- Mednnet

why TVContext needs to implement State interface ? I think its not required.

- Lalit Upadheyay

Please change all the references of “it’s” to “its”. They’re driving me crazy (as I work on my dissertation I am sensitive to these things).

- DrJ

This is just awesome. Explained one of the complex design patterns with such a easy example

- Praveen Srivastava

here TvContext implements State interface if i do TvContext tv=new TvContext(); tv.setState(tv); tv.doAction(); wont it start looping??

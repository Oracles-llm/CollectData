# Understanding the Flyweight Design Pattern

• • 21 min readThere are 23 classic design patterns described in the original book * Design Patterns: Elements of Reusable Object-Oriented Software*. These patterns provide solutions to particular problems often repeated in software development.

In this article, I am going to describe how the * Flyweight* pattern works and when it should be applied.

# Flyweight: Basic Idea

First, let’s see the definition provided by the Gang of Four book:

A flyweight is a shared object that can be used in multiple contexts simultaneously. The flyweight acts as an independent object in each context; it’s indistinguishable from an instance of the object that is not shared.

On the other hand, flyweight objects cannot make assumptions about the context in which they operate. The key concept here is the distinction between * intrinsic* and

*state. Intrinsic state is stored in the flyweight; it consists of information that is independent of the flyweight’s context, allowing it to be shared. Extrinsic state depends on the flyweight’s context and varies with it, therefore, it cannot be shared. Client objects are responsible for passing the extrinsic state to the flyweight when it is needed.*

*extrinsic*Next, let’s take a look at the UML class diagram for this pattern to understand each of its elements.

The * Flyweight* pattern typically includes the following elements:

: Defines the interface for objects that can be shared. It contains the intrinsic states that are shared among several objects.**Flyweight**: Implements the**Concrete Flyweight**interface and stores the intrinsic states. These objects are shared among multiple contexts.*Flyweight*: Represents objects that cannot be shared. Although they do not share their state, they can contain references to other Flyweight objects.**Unshared Concrete Flyweight**: Manages a set of Flyweight objects. It ensures that Flyweight objects are shared properly and provides methods to obtain instances of Flyweights.**Flyweight Factory**: Maintains references to the Flyweights and calculates or stores the extrinsic states (those that are not shared and can vary between objects).**Client**

# Flyweight Pattern: When to Use It

The * Flyweight* pattern is an excellent solution when dealing with systems that need to create and manage a large number of similar objects, which can result in high memory consumption if not managed properly. Below are some common situations where using the

*pattern can be beneficial:*

*Flyweight*When we have a large number of objects that share significant parts of their state with each other, such as text, images, or similar data, the**Objects with shared states:**pattern allows sharing these common states among multiple instances, thereby reducing memory consumption.*Flyweight*: If you want to reduce memory or other resource consumption in your system, the**Reduction of resource consumption**pattern can be an effective solution. By sharing common parts of objects among multiple instances, unnecessary duplication of data is avoided, and system performance is optimized.*Flyweight*: The**Facilitating object creation**pattern facilitates the creation and management of a large number of objects by reusing existing instances instead of creating new ones each time they are needed. This can be especially useful in situations where object creation is resource-intensive in terms of computational resources.*Flyweight*

In summary, the * Flyweight* pattern is useful in situations where it is necessary to optimize memory and resource usage by sharing common parts of objects among multiple instances. Now, let’s look at examples of applying this pattern.

**Flyweight Pattern: Examples**

Next, we will illustrate the * Flyweight* pattern with two examples:

: In this example, we will translate the theoretical UML diagram into TypeScript code to identify each of the classes involved in the pattern.**Basic Structure of the Flyweight Pattern**: We will have statistics for different teams, with hundreds of players where we need to objects to define the positions of the players and the teams they belong to. Here, we can see that we will have many objects that are shared, such as the specific positions of the players or the team.**A football statistics system**

# Example 1: Basic Structure of the Flyweight Pattern

As always, the starting point is the UML class diagram to define each of the elements. This first class diagram is the same one we explained at the beginning of the post, and we will not repeat the explanation here to avoid making the post too long.

However, we will start implementing it step by step using the TypeScript programming language.

Let’s start with the `Flyweight`

interface. This interface defines the contract that any `Flyweight`

in the system must follow. In this case, it only has one method called `operation`

, which receives the extrinsic state of our problem as a parameter. This method is implemented by the concrete flyweights, both the shared and the unshared ones.

```
export interface Flyweight {
operation(extrinsicState: any): void;
}
```


The next class is the `ConcreteFlyweight`

. In this class, we can see that we have a private attribute, which is the * intrinsic* state of our problem. As always, to simplify the example, this attribute is of type

`string`

. This state is received as a constructor parameter to store it internally in this class. Finally, we have the implementation of the `operation`

method, which receives the *state and performs a*

*extrinsic*`console.log`

showing both states. Obviously, here we would have the business logic for our problem.```
import { Flyweight } from "./flyweight";
export class ConcreteFlyweight implements Flyweight {
private intrinsicState: string;
constructor(intrinsicState: string) {
this.intrinsicState = intrinsicState;
}
public operation(extrinsicState: any): void {
console.log(`ConcreteFlyweight: Intrinsic State = ${this.intrinsicState}, Extrinsic State = ${extrinsicState}`);
}
}
```


On the other hand, the `UnsharedConcreteFlyweight`

class is the representation of the objects that are not shared in our problem. If we look at this class, we have a small variation; instead of having the * intrinsic* state stored, we have the entire state of the object. Obviously, again to simplify the example, it has been modeled as a

`string`

, but the conceptual difference is quite significant between `Flyweight`

that share state and those that do not share state. Lastly, we have the implementation of the `operation`

method, which displays the information of the `allState`

attribute and the *state.*

*extrinsic*```
import { Flyweight } from "./flyweight";
// Unshared Concrete Flyweight
export class UnsharedConcreteFlyweight implements Flyweight {
private allState: string;
constructor(allState: string) {
this.allState = allState;
}
public operation(extrinsicState: any): void {
console.log(`UnsharedConcreteFlyweight: All State = ${this.allState}, Extrinsic State = ${extrinsicState}`);
}
}
```


Up to this point, we have the * Flyweight* pattern by definition. However, in most cases, this pattern includes a factory class that is responsible for creating the

`Flyweight`

objects. And it is precisely this class that we will look at next.```
import { ConcreteFlyweight } from "./concrete-flyweight";
import { Flyweight } from "./flyweight";
// Flyweight Factory
export class FlyweightFactory {
private flyweights: Map<string, Flyweight> = new Map();
public getFlyweight(key: string): Flyweight {
if(this.flyweights.has(key)){
console.log(`FlyweightFactory: Reusing existing flyweight for key = ${key}`);
return this.flyweights.get(key)!;
}
this.flyweights.set(key, new ConcreteFlyweight(key));
console.log(`FlyweightFactory: Created new flyweight for key = ${key}`);
return this.flyweights.get(key)!;
}
public listFlyweights(): void {
console.log(`FlyweightFactory: I have ${this.flyweights.size} flyweights:`);
for (const [key, _] of this.flyweights) {
console.log(key);
}
}
}
```


In this class, we need to have a data structure where we store the different `Flyweight`

objects. In our case, we are using a map where the key is a string identifier, and the value is the stored `Flyweight`

object.

The `getFlyweight`

method is the key to this factory because it takes the key as an argument to retrieve the object from the data structure. As we can see in the first control block of the code, the `if`

statement checks whether the data structure contains the object we are looking for, and if it does, we simply return it.

If we do not have the object in the data structure, a new `Flyweight`

object is created using the `ConcreteFlyweight`

constructor and stored in our data structure. The method concludes by returning the object we just created.

Therefore, we are implementing a small cache that will streamline the process of creating and retrieving objects. If the object already exists, we retrieve the one we have in memory and do not create duplicate objects. If the object does not exist, it is created only once.

The next method in the class, `listFlyweights`

, simply iterates over the data structure where we have all the objects and displays the objects contained within it. We could have implemented any other business logic.

```
import { FlyweightFactory } from "./flyweight-factory";
import { UnsharedConcreteFlyweight } from "./unshared-flyweight";
const factory = new FlyweightFactory();
// Create and use shared flyweights
const flyweight1 = factory.getFlyweight('A');
flyweight1.operation('First Call');
const flyweight2 = factory.getFlyweight('B');
flyweight2.operation('Second Call');
const flyweight3 = factory.getFlyweight('A');
flyweight3.operation('Third Call');
// Create and use unshared flyweights
const unsharedFlyweight1 = new UnsharedConcreteFlyweight('Unique State');
unsharedFlyweight1.operation('Fourth Call');
factory.listFlyweights();
```


Finally, let’s look at the client code that uses the design pattern. In the code, the first thing we do is create the factory, which is responsible for managing the `Flyweight`

objects. Next, we retrieve an object with the value `A`

. Internally, the pattern will create this object since it does not exist and store it in the data structure. Then, we can use the `operation`

method. We do the same with the object with the value `B`

. The application of the pattern comes when creating the third object, where we retrieve the value `A`

, and in this case, no more resources are consumed since it is obtained directly from the data structure instead of being instantiated again.

On the other hand, showing that the instance of objects that do not share the state would be as simple as making instances of these objects and using the defined methods. To conclude, we show all the objects instantiated in the data structure through the `listFlyweights`

method, and we can see that the object with the value `A`

appears instantiated only once in our problem

# Example 2: Football Player Statistics Database without the Flyweight Pattern

In this example, we are going to create a database of football players where each player will have instances of other objects such as their positions and the team they belong to. Additionally, the players will have their own statistics on their performance in official matches.

Considering this problem, the UML class design that can be proposed is as follows:

We can observe that we would have the `Player`

class with its own attributes, such as `name`

, `position`

, `team`

, and `statistics`

. The attributes `position`

, `team`

, and `statistics`

are not primitives but objects that have different attributes, which, of course, could have more logic and methods, implement interfaces, etc. However, as always, we are simplifying to properly understand the pattern. But at first glance, we can see that we have the `Player`

class and, through composition, we encounter three classes that are related to it. These classes depend on the `Player`

, meaning that if the `Player`

disappears, the objects in the composition are also destroyed.

The client of this application is called `SportsSimulator`

, which is the class that would have the data structure storing all the instances of the players and some methods to manage this data structure, such as `addPlayer`

, which receives the arguments for creating players, and the `displayPlayers`

method, which lists all the players in the software. We can observe that `SportsSimulator`

is not responsible for creating objects such as position, team, or statistics but rather receives the information from some data source. The only thing we can know and guarantee is that the data has the corresponding attributes to be well-formed. This has been modeled with the package of `interfaces`

, where we find the interfaces for position, team, and statistics.

Let’s proceed to see the implementation of this first solution, which ** does NOT** use the

*pattern, to detect where the resource leak is that we could improve with the pattern.*

*Flyweight*The first class we need to look at is the `Player`

class, which is quite simple. If we observe, we have the four attributes that make up a `Player`

, and through the constructor, we receive the parameters that allow us to internally store each attribute of this object. Additionally, we include a `toString`

method, which we have renamed as `displayInfo`

, that simply shows the information of the object.

```
import { Position } from "./position";
import { Stats } from "./stats";
import { Team } from "./team";
export class Player {
private name: string;
private position: Position;
private team: Team;
private stats: Stats;
constructor(name: string, position: Position, team: Team, stats: Stats) {
this.name = name;
this.position = position;
this.team = team;
this.stats = stats;
}
public displayInfo(): void {
console.log(`Player - Name: ${this.name}, Position: ${this.position.name} (${this.position.role}), Team: ${this.team.name} (Coach: ${this.team.coach}), Stats: [Goals: ${this.stats.goals}, Assists: ${this.stats.assists}, Matches: ${this.stats.matches}]`);
}
}
```


On the other hand, the `Position`

, `Team`

, and `Stats`

classes do not contain any logic. Again, we repeat, this is didactic, and they should make sense as such to exist, but to simplify, we can see that they simply store the corresponding attributes of each type of object when they are constructed.

```
export class Position {
constructor(public name: string, public role: string) {}
}
export class Stats {
constructor(public goals: number, public assists: number, public matches: number) {}
}
export class Stats {
constructor(public goals: number, public assists: number, public matches: number) {}
}
```


The next class is `SportsSimulator`

, which is responsible for storing the data structure. In this case, we would have an array of `Players`

, which are built in the `addPlayer`

method itself. This method receives as a parameter the necessary information to create instances of all the objects. However, what it receives are objects that satisfy the interface of `Position`

, `Team`

, and `Stats`

, but these objects it receives are not instances of classes, but simply data.

Therefore, the three objects that the instance of the `Player`

class required are created, and once created, they are added to the data structure.

```
import { IPosition, IStats, ITeam } from "./interfaces";
import { Player, Position, Stats, Team } from "./models";
export class SportsSimulator {
private players: Player[] = [];
public addPlayer(name: string, position: IPosition, team: ITeam, stats: IStats): void {
const positionPlayer = new Position(position.name, position.role);
const teamPlayer = new Team(team.name, team.coach);
const statsPlayer = new Stats(stats.goals, stats.assists, stats.passes);
const player = new Player(name, positionPlayer, teamPlayer, statsPlayer);
this.players.push(player);
}
public displayPlayers(): void {
this.players.forEach(player => player.displayInfo());
}
}
```


As mentioned earlier, the interfaces simply specify the attributes that the plain objects passed as arguments must contain. We have done it this way because in TypeScript, we can quickly create plain objects, which allows us to avoid having a method signature for `addPlayer`

with all the attributes of player, position, team, and statistics separated, but instead having them grouped by plain objects.

```
export interface IPosition {
name: string;
role: string;
};
export interface ITeam {
name: string;
coach: string;
};
export interface IStats {
goals: number;
assists: number;
passes: number;
};
```


Finally, we need to see the client code that uses all these classes.

```
import { IPosition, IStats, ITeam } from "./interfaces";
import { SportsSimulator } from "./sports-simulator";
// Client Code
const simulator = new SportsSimulator();
const forward: IPosition = {name: 'Forward', role: 'Attacker'};
const midfielder: IPosition = {name: 'Midfielder', role: 'Support'};
const defender: IPosition = { name: 'Defender', role: 'Defender'};
const goalkeeper: IPosition = {name: 'Goalkeeper', role: 'Goalkeeper'};
const positions = [goalkeeper, defender, midfielder, forward]
const teams: ITeam[] = [
{ name: "New Team", coach: "Roberto Sedinho" },
{ name: "Furano FC", coach: "Koujiro Hyuuga" },
{ name: "Toho Academy", coach: "Kira Hiroto" },
{ name: "Nankatsu SC", coach: "Tsubasa Ozora" },
{ name: "Otomo FC", coach: "Shingo Aoi" },
{ name: "Hirado FC", coach: "Hajime Taki" },
{ name: "Mamoru United", coach: "Taro Misaki" },
{ name: "Meiwa FC", coach: "Jun Misugi" }
];
const captainTsubasaCharacters: string[] = [
"Tsubasa Ozora",
"Koujiro Hyuuga",
"Genzo Wakabayashi",
"Taro Misaki",
"Shingo Aoi",
"Hikaru Matsuyama",
"Jun Misugi",
"Ken Wakashimazu",
"Kazuo Tachibana",
"Masao Tachibana",
"Ryo Ishizaki",
"Kojiro Hyuga",
"Teppei Kisugi",
"Hiroshi Jito",
"Shun Nitta",
"Mamoru Izawa",
"Hanji Urabe",
"Shingo Takasugi",
"Mitsuru Sano",
"Makoto Soda"
];
for(let i = 0; i < 25*teams.length -1; i++){
const team = teams[i % teams.length];
const position = positions[i % positions.length];
const playerName = captainTsubasaCharacters[i % captainTsubasaCharacters.length];
const stats: IStats = {
goals: Math.floor(Math.random() * 20),
assists: Math.floor(Math.random() * 20),
passes: Math.floor(Math.random() * 20),
};
simulator.addPlayer(playerName, position, team, stats);
}
simulator.displayPlayers();
```


The first thing we have to do is create the sports simulator. To do this, we simply need to instantiate the `SportsSimulator`

class. Next, we have the data we are going to use in the problem. This data can come from any data source, whether it’s integration files, databases, or even entered by the user. So, first, we define the positions, which would be forward, midfielder, defender, and goalkeeper.

Next, we define exactly the same but for the teams. We would have an array of team objects that satisfy the conditions of having a name and a coach. If you’ve noticed the names of the teams, our database is based on the anime series * Captain Tsubasa*. So, we need to reflect the names of the players as they appeared in the original version of the anime.

The last of our client code is a simple loop that is creating the necessary information for each team to have twenty five players. For that, we simply iterate to retrieve the information and send it to the simulator through the `addPlayer`

method, and that’s where our object-oriented design would begin. Obviously, as we have more and more players, we will have more resources consumed by the instantiation of objects.

So far, there wouldn’t be a problem until one day the software needs more memory and we have to redesign it, which is exactly what we are going to do, but using the * Flyweight* pattern.

# Example 2: Football Player Statistics Database using the Flyweight Pattern

The problems that arise in the solution without the * Flyweight* pattern are as follows:

: When many similar objects are created, each instance occupies its own space in memory. This can lead to very high memory consumption, especially if the objects have attributes that are repeated in multiple instances.**Excessive memory usage**: In the absence of the**Data redundancy**pattern, data that is common to multiple objects is duplicated in each instance. This not only increases memory usage but also introduces redundancy that can complicate data maintenance and updating.*Flyweight*: Handling a large number of individual objects can degrade application performance, both in terms of processing time and resource consumption. Operations involving the manipulation of these objects can become slow and inefficient.**Degradation of the system when used**: Without the**Difficulty in resource management**pattern, managing resources shared among multiple instances of objects becomes more complicated. This can lead to consistency and synchronization problems, especially in concurrent or distributed applications. Implementing the*Flyweight*pattern can mitigate these problems by allowing the sharing of objects where possible, reducing redundancy, and optimizing memory and resource usage. Let’s start by seeing how the UML class diagram evolves.*Flyweight*

Let’s start by looking at the `Player`

class. This class now does not directly relate to the `Position`

and `Team`

classes. Instead, there is now an intermediate class called `PositionFlyweight`

and `TeamFlyweight`

, each of which contains an aggregation of the `Position`

and `Team`

classes. Both flyweight classes implement the flyweight interface, which simply has a method called display to show information. These classes could be omitted if we didn’t have * extrinsic* states, but we’re demonstrating the pattern with different elements that could disappear depending on specific circumstances and problems.

Another key point in the diagram is that we have an abstract class that defines the different object factories. The `flyweightFactory`

class is composed of a `Map`

of objects that satisfy the `Flyweight`

interface. This abstract class is extended by the `PositionFlyweight`

and `TeamFlyweight`

classes, which do have concreteness in their data structure. In one case, they store objects of the `PositionFlyweight`

class, and in the other, objects of the `TeamFlyweight`

class. Both implement the `getFlyweight`

method, which allows us to create a new `PositionFlyweight`

or `TeamFlyweight`

object or retrieve it from the data structure.

As an exercise or appreciation of how design patterns intertwine, this method has an algorithm in which all steps are similar except one, which could allow us to implement the template-method design pattern, as we have seen in another post. However, we will duplicate code to simplify this example, as we are focusing on the * flyweight* pattern and not another. But what’s important is that we understand the purpose of each design pattern so that when they arise, we can think about how to adapt it to our problem.

Finally, we see that we have the `SportsSimulator`

class, which will make use of both factories and will have the data structure of the players. Similarly to the previous example, the data will come from a data source where we only have the attributes without instantiation, and we can only guarantee that they have a series of attributes using the package of interfaces that has been defined.

Alright, let’s proceed to gradually review the implementation and how it has changed compared to the previous example to improve the application’s performance.

Let’s start with the code of the `Player`

class, which instead of directly receiving `Position`

and `Team`

objects, now receives instances of `PositionFlyweight`

and `TeamFlyweight`

objects. Since `Stats`

objects are not reused and are different for each class, they still maintain their direct relationship with the `Player`

class. The `displayInfo`

method is practically the same, only updating the invocation of the display method of the `positionFlyweight`

object.

The `Stats`

class undergoes no modification compared to the previous example since we are not applying any pattern or improvement there. This is because the statistics will not be reused among different players as the probability of reusing an object is low, and we would not benefit from this design pattern.

```
import { PositionFlyweight } from "../position-flyweight";
import { Stats } from "./stats";
import { TeamFlyweight } from "../team-flyweight";
export class Player {
private name: string;
private positionFlyweight: PositionFlyweight;
private teamFlyweight: TeamFlyweight;
private stats: Stats;
constructor(name: string, positionFlyweight: PositionFlyweight, teamFlyweight: TeamFlyweight, stats: Stats) {
this.name = name;
this.positionFlyweight = positionFlyweight;
this.teamFlyweight = teamFlyweight;
this.stats = stats;
}
public displayInfo(): void {
console.log(`Player - Name: ${this.name}, Stats: [Goals: ${this.stats.goals}, Assists: ${this.stats.assists}, Matches: ${this.stats.matches}]`);
this.positionFlyweight.display(this.stats);
}
}
```


So, let’s move on to see the `PositionFlyweight`

and `TeamFlyweight`

classes.

```
import { Flyweight } from "./flyweight";
import { Position } from "./models";
export class PositionFlyweight implements Flyweight {
#position: Position; // Intrinsic State
constructor(position: Position) {
this.#position = position;
}
public display(extrinsicState: any): void {
console.log(`Position: ${this.#position.name} (${this.#position.role})`);
}
public position(): Position {
return this.#position;
}
}
```


```
import { Flyweight } from "./flyweight";
import { Team } from "./models";
export class TeamFlyweight implements Flyweight {
#team: Team; // Intrinsic State
constructor(team: Team) {
this.#team = team;
}
public display(extrinsicState: any): void {
console.log(`Team: ${this.#team.name} (${this.#team.coach})`);
}
public team(): Team {
return this.#team;
}
}
```


Both classes are very similar, as they simply have an object of the class they are encapsulating, `Position`

or `Team`

, which represent the * intrinsic* states of each class. In both cases, we have performed composition through the constructor, receiving the instance of the objects. The next thing we have implemented is the display method, which will receive the

*state, if necessary, and will display information from both states through a*

*extrinsic*`console.log`

.On the other hand, the `Position`

and `Team`

classes remain exactly the same as in the previous example; they are model classes without further changes.

```
import { Flyweight } from "./flyweight";
// Flyweight Factory
export abstract class FlyweightFactory<T> {
protected flyweights: Map<string, Flyweight> = new Map();
public abstract getFlyweight(key: T): Flyweight;
public listFlyweights(): void {
console.log(`FlyweightFactory: I have ${this.flyweights.size} flyweights:`);
for (const [key, _] of this.flyweights) {
console.log(key);
}
}
}
```


This class defines the two object factories that we will have. The data structure that will store the objects will be a `Map`

that uses a string as the key and any object that implements the `Flyweight`

interface as the value, which will be both `Position`

and `Team`

. The `getFlyweight`

method is defined, which varies slightly depending on whether the factory is for `Position`

or `Team`

objects. This method is where we could improve by applying the template-method pattern, and we leave it as an exercise for you to do.

On the other hand, we see the `listFlyweight`

method, which is exactly the same for both factories since all it does is iterate through the data structure.

```
import { FlyweightFactory } from "./flyweight.factory";
import { Position } from "./models";
import { PositionFlyweight } from "./position-flyweight";
export class PositionFlyweightFactory extends FlyweightFactory<Position> {
protected flyweights: Map<string, PositionFlyweight> = new Map();
public getFlyweight(position: Position): PositionFlyweight {
const key = `${position.name}_${position.role}`;
if(this.flyweights.has(key)) {
console.log(`ConcreteFlyweightFactory: Reusing existing flyweight for Position = ${key}`);
return this.flyweights.get(key)!;
}
this.flyweights.set(key, new PositionFlyweight(position));
console.log(`PositionFlyweightFactory: Created new flyweight for Position = ${key}`);
return this.flyweights.get(key)!;
}
}
```


```
import { FlyweightFactory } from "./flyweight.factory";
import { Team } from "./models";
import { TeamFlyweight } from "./team-flyweight";
export class TeamFlyweightFactory extends FlyweightFactory<Team> {
protected flyweights: Map<string, TeamFlyweight> = new Map();
public getFlyweight(team: Team): TeamFlyweight {
const key = `team_${team.name}_coach_${team.coach}`;
if(this.flyweights.has(key)) {
console.log(`ConcreteFlyweightFactory: Reusing existing flyweight for Team = ${key}`);
return this.flyweights.get(key)!;
}
this.flyweights.set(key, new TeamFlyweight(team));
console.log(`PositionFlyweightFactory: Created new flyweight for Team = ${key}`);
return this.flyweights.get(key)!;
}
}
```


If we look at the concrete implementations of the `PositionFlyweightFactory`

and `TeamFlyweightFactory`

classes, we can see that they are exactly the same, except for the type of object they are working with and the key used to select the object in the data structure. So, we’ll focus on one to explain both. Looking at `PositionFlyweight`

, we see that this method first defines the key, which will be unique for each object and is formed by the values of each object. The next thing we need to do is check if this object exists in the data structure. If it does, we return it without needing to create a new object. But if it doesn’t exist in the data structure, what we do is create the object to store, store it, and finally return the object we just created.

```
import { IPosition, IStats, ITeam } from "./interfaces";
import { Player, Stats } from "./models";
import { PositionFlyweightFactory } from "./position-flyweight.factory";
import { TeamFlyweightFactory } from "./team-flyweight.factory";
export class SportsSimulator {
private players: Player[] = [];
private positionFactory: PositionFlyweightFactory = new PositionFlyweightFactory();
private teamFactory: TeamFlyweightFactory = new TeamFlyweightFactory();
public addPlayer(name: string, position: IPosition, team: ITeam, stats: IStats): void {
const positionFlyweight = this.positionFactory.getFlyweight(position);
const teamFlyweight = this.teamFactory.getFlyweight(team);
const statsPlayer = new Stats(stats.goals, stats.assists, stats.passes);
const player = new Player(name, positionFlyweight, teamFlyweight, statsPlayer);
this.players.push(player);
}
public displayPlayers(): void {
this.players.forEach(player => player.displayInfo());
}
}
```


Finally, we arrive at the `SportsSimulator`

class, which is the database of our players. In this new version, in addition to having the data structure of the players, we need the two factories we just defined. The `addPlayer`

method is where, instead of instantiating all the objects and composing them into the `Player`

, we will use the factories to retrieve or create the objects based on the information. In this way, it will be these classes that decide whether new objects are instantiated or whether they are reused in the system.

```
import { IPosition, IStats, ITeam } from "./interfaces";
import { SportsSimulator } from "./sports-simulator";
// Client Code
const simulator = new SportsSimulator();
const forward: IPosition = {name: 'Forward', role: 'Attacker'};
const midfielder: IPosition = {name: 'Midfielder', role: 'Support'};
const defender: IPosition = { name: 'Defender', role: 'Defender'};
const goalkeeper: IPosition = {name: 'Goalkeeper', role: 'Goalkeeper'};
const positions = [goalkeeper, defender, midfielder, forward]
const teams: ITeam[] = [
{ name: "New Team", coach: "Roberto Sedinho" },
{ name: "Furano FC", coach: "Koujiro Hyuuga" },
{ name: "Toho Academy", coach: "Kira Hiroto" },
{ name: "Nankatsu SC", coach: "Tsubasa Ozora" },
{ name: "Otomo FC", coach: "Shingo Aoi" },
{ name: "Hirado FC", coach: "Hajime Taki" },
{ name: "Mamoru United", coach: "Taro Misaki" },
{ name: "Meiwa FC", coach: "Jun Misugi" }
];
const captainTsubasaCharacters: string[] = [
"Tsubasa Ozora",
"Koujiro Hyuuga",
"Genzo Wakabayashi",
"Taro Misaki",
"Shingo Aoi",
"Hikaru Matsuyama",
"Jun Misugi",
"Ken Wakashimazu",
"Kazuo Tachibana",
"Masao Tachibana",
"Ryo Ishizaki",
"Kojiro Hyuga",
"Teppei Kisugi",
"Hiroshi Jito",
"Shun Nitta",
"Mamoru Izawa",
"Hanji Urabe",
"Shingo Takasugi",
"Mitsuru Sano",
"Makoto Soda"
];
for(let i = 0; i < 25*teams.length -1; i++){
const team = teams[i % teams.length];
const position = positions[i % positions.length];
const playerName = captainTsubasaCharacters[i % captainTsubasaCharacters.length];
const stats: IStats = {
goals: Math.floor(Math.random() * 20),
assists: Math.floor(Math.random() * 20),
passes: Math.floor(Math.random() * 20),
};
simulator.addPlayer(playerName, position, team, stats);
}
simulator.displayPlayers();
```


Finally, the client that uses our `SportsSimulator`

class is completely transparent and remains exactly the same, creating the data or receiving it from some data source, and sending it to `SportsSimulator`

. But now, instead of having an explosion of objects consuming hardware resources, many of these objects will be reused, making the software lighter and able to continue providing service. In other words, we have achieved an optimization of RAM memory by making the objects lighter.

**Flyweight Pattern: Relationship with Other Patterns**

The * Flyweight* pattern has connections with several other design patterns, as it can complement and enhance their functionality. Some of the most relevant relationships include:

The**Singleton Pattern:**pattern can be used in conjunction with the*Singleton*pattern to ensure that only one instance of the*Flyweight*Factory exists throughout the application. This ensures centralized management of*Flyweight*objects and prevents unnecessary creation of multiple factories.*Flyweight*The implementation of the**Factory Method Pattern:**Factory can leverage the*Flyweight*pattern to allow flexible and decoupled creation of*Factory Method*`Flyweight`

objects. This facilitates the creation and management of`Flyweight`

object instances as needed in different parts of the system.The**Composite Pattern:**pattern can be used in combination with the*Composite*pattern to represent hierarchical structures where some objects can be shared among multiple components. By using the*Flyweight*pattern for shared objects, memory consumption is significantly reduced, and system efficiency is improved.*Flyweight*The**Proxy Pattern:**pattern can serve as a wrapper around a*Proxy*`Flyweight`

object, allowing additional control over object access or lifecycle management. This can be useful when more granular control over access to`SharedFlyweight`

objects is needed or when additional tasks need to be performed before or after accessing the object.

By leveraging these relationships with other patterns, the * Flyweight* pattern can enhance the efficiency, scalability, and maintainability of a system while optimizing resource usage and promoting a clearer and more modular code structure.

**Differences and Similarities with Other Patterns: Singleton and Prototype**

Let’s examine the similarities and differences between the Singleton and Prototype design patterns since the * Flyweight* pattern is often confused with these two design patterns.

**Singleton Pattern: Differences**

- The Singleton pattern is used to ensure that a class has only one instance and provides a global access point to that instance, while the
pattern is used to efficiently share a large number of objects.*Flyweight* - In the Singleton pattern, the emphasis is on having a single instance of a class, while in the
pattern, the emphasis is on efficiently sharing*Flyweight*states among multiple similar objects.*intrinsic*

*Singleton Pattern: Similarities*

- Both patterns are related to efficient object management and resource optimization.
- Both patterns can be used together to optimize the performance and efficiency of a system.

**Prototype Pattern: Differences**

- The
pattern is used to create new objects by duplicating an existing prototype, while the*Prototype*pattern is used to share existing objects and minimize resource usage.*Flyweight* - In the
pattern, each instance can have its own unique state, while in the*Prototype*pattern, part of the state can be shared among multiple instances.*Flyweight*

*Prototype Pattern: Similarities*

- Both patterns are related to efficient object creation and resource optimization.
- Both patterns can be used to reduce the overhead of object creation and improve system performance.

Although the * Flyweight* pattern shares some similarities with the

*and*

*Singleton**patterns, it is important to understand their fundamental differences and how they can be used complementary to address different design problems.*

*Prototype*# Conclusions

The * Flyweight* pattern provides an efficient and elegant solution for systems that need to manage a large number of similar objects. By sharing common parts of objects among multiple instances, significant resource optimization and system performance improvement are achieved.

The most important thing about the * Flyweight* pattern is not its specific implementation, but the ability to recognize the problem that this pattern can solve and when

**The specific implementation is not that important, as it will vary depending on the programming language used.**

**it can be applied.**See this GitHub repo for the full code.
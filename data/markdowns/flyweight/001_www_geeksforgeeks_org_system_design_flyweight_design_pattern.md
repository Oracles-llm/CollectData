The Flyweight design pattern is a structural pattern that optimizes memory usage by sharing a common state among multiple objects. It aims to reduce the number of objects created and to decrease memory footprint, which is particularly useful when dealing with a large number of similar objects.

## What is a Flyweight Design Pattern?

The Flyweight Design Pattern is a way to save memory in applications that create a large number of similar objects. Instead of creating a new object for each instance, the Flyweight pattern reuses existing ones wherever possible, sharing common parts between objects.

Here’s how it works:

**Shared vs. Unique Data:** Objects are split into shared (intrinsic) data and unique (extrinsic) data. The shared data is stored in a central place and reused, while the unique data is kept separately.**Example:** Imagine a text editor displaying thousands of characters. Using Flyweight, the program can store each unique character style (like font or color) only once and reuse it, rather than duplicating it for every character.

## Components of Flyweight Design Pattern

The Flyweight design pattern typically consists of the following components:

**Flyweight Interface/Class:**- Defines the interface through which flyweight objects can receive and act on extrinsic state.

**Concrete Flyweight Classes:**- Implements the Flyweight interface and represents objects that can be shared.
- Stores intrinsic state (state that can be shared) and provides methods to manipulate intrinsic state if needed.

**Flyweight Factory:**- Manages a pool of flyweight objects.
- Provides methods for clients to retrieve or create flyweight objects.
- Ensures flyweight objects are shared appropriately to maximize reusability.

**Client:**- Uses flyweight objects to perform operations.
- Maintains or passes extrinsic state to flyweight objects when needed.
- Does not manage the lifecycle of flyweight objects directly but interacts with them via the factory.


## How to implement Flyweight Design Pattern?

To implement the Flyweight Design Pattern, follow these simple steps:

**Step 1: Identify Shared and Unique Data**: Arrange the data in your objects first. Determine which information is specific to each object (known as extrinsic data) and which can be shared across objects (known as intrinsic data).**Step 2: Create a Flyweight Class**: This class will hold the intrinsic (shared) data. All instances of this class represent objects with similar data.**Step 3: Build a Flyweight Factory**: This factory class manages instances of the Flyweight objects. When a new object is needed, the factory checks if an object with the same shared data already exists. If it does, it reuses that object; if not, it creates a new one.**Step 4: Pass Unique Data as Needed**: The extrinsic data, or data specific to that instance(extrinsic data), should be passed as a parameter when using an object. In this manner, the object can act in a unique way without storing all of the data.**Step 5: Use Flyweights Instead of Creating New Objects**: Now, instead of creating new objects directly, always request them through the factory. The factory will manage all shared instances and reuse them where possible.

## Example Implementation of Flyweight Design Pattern

Below is the problem statement to understand flyweight design pattern:

Imagine a graphical user interface (GUI) application where multiple icons of different types (e.g., file icons, folder icons) need to be displayed on a screen. Each icon type has a specific appearance and behavior, such as different images and positions on the screen. However, displaying numerous icons of the same type can consume significant memory if each icon object stores its unique properties independently.


### How Flyweight Design Pattern will help to solve this problem?

- The Flyweight design pattern can optimize memory usage by sharing common parts of the icons (intrinsic state), such as the image and basic properties (like size and color), among multiple icon instances.
- Each icon instance then stores only its unique properties (extrinsic state), such as its position on the screen.
- This approach reduces the memory footprint and enhances performance, especially when dealing with a large number of similar objects.

### Component wise code of flyweight design pattern

Below is the component wise code of flyweight design pattern:

### 1. Flyweight Interface:

Java
// Flyweight interface
public interface Icon {
void draw(int x, int y); // Method to draw the icon at given coordinates
}


### 2. Concrete Flyweight Classes

Java
// Concrete Flyweight class representing a File Icon
public class FileIcon implements Icon {
private String type; // Intrinsic state: type of file icon (e.g., document, image)
private Image image; // Intrinsic state: image specific to the file icon
public FileIcon(String type, Image image) {
this.type = type;
this.image = image;
}
@Override
public void draw(int x, int y) {
// Draw logic specific to file icon using intrinsic state (image)
System.out.println("Drawing " + type + " icon at position (" + x + ", " + y + ")");
}
}
// Concrete Flyweight class representing a Folder Icon
public class FolderIcon implements Icon {
private String color; // Intrinsic state: color of the folder icon
private Image image; // Intrinsic state: image specific to the folder icon
public FolderIcon(String color, Image image) {
this.color = color;
this.image = image;
}
@Override
public void draw(int x, int y) {
// Draw logic specific to folder icon using intrinsic state (image)
System.out.println("Drawing folder icon with color " + color + " at position (" + x + ", " + y + ")");
}
}


### 3. Flyweight Factory

Java
import java.util.HashMap;
import java.util.Map;
// Flyweight factory to manage creation and retrieval of flyweight objects
public class IconFactory {
private Map<String, Icon> iconCache = new HashMap<>();
public Icon getIcon(String key) {
// Check if the icon already exists in the cache
if (iconCache.containsKey(key)) {
return iconCache.get(key);
} else {
// Create a new icon based on the key (type of icon)
Icon icon;
if (key.equals("file")) {
icon = new FileIcon("document", loadImage("document.png"));
} else if (key.equals("folder")) {
icon = new FolderIcon("blue", loadImage("folder.png"));
} else {
throw new IllegalArgumentException("Unsupported icon type: " + key);
}
// Store the created icon in the cache
iconCache.put(key, icon);
return icon;
}
}
// Simulated method to load image based on filename
private Image loadImage(String filename) {
// Load image from file system or resource
// Here, returning a dummy Image object
return new Image(filename);
}
}


### 4. Client Code

Java
// Client code to use the flyweight objects (icons)
public class Client {
public static void main(String[] args) {
IconFactory iconFactory = new IconFactory();
// Draw file icons at different positions
Icon fileIcon1 = iconFactory.getIcon("file");
fileIcon1.draw(100, 100);
Icon fileIcon2 = iconFactory.getIcon("file");
fileIcon2.draw(150, 150);
// Draw folder icons at different positions
Icon folderIcon1 = iconFactory.getIcon("folder");
folderIcon1.draw(200, 200);
Icon folderIcon2 = iconFactory.getIcon("folder");
folderIcon2.draw(250, 250);
}
}


### Complete code of the flyweight design pattern:

Java
import java.util.HashMap;
import java.util.Map;
// Flyweight interface
interface Icon {
void draw(int x, int y); // Method to draw the icon at given coordinates
}
// Concrete Flyweight class representing a File Icon
class FileIcon implements Icon {
private String type; // Intrinsic state: type of file icon
private String imageName; // Intrinsic state: image name specific to the file icon
public FileIcon(String type, String imageName) {
this.type = type;
this.imageName = imageName;
}
@Override
public void draw(int x, int y) {
// Simulated logic to load and draw image
System.out.println("Drawing " + type + " icon with image " + imageName + " at position (" + x + ", " + y + ")");
}
}
// Concrete Flyweight class representing a Folder Icon
class FolderIcon implements Icon {
private String color; // Intrinsic state: color of the folder icon
private String imageName; // Intrinsic state: image name specific to the folder icon
public FolderIcon(String color, String imageName) {
this.color = color;
this.imageName = imageName;
}
@Override
public void draw(int x, int y) {
// Simulated logic to load and draw image
System.out.println("Drawing folder icon with color " + color + " and image " + imageName + " at position (" + x + ", " + y + ")");
}
}
// Flyweight factory to manage creation and retrieval of flyweight objects
class IconFactory {
private Map<String, Icon> iconCache = new HashMap<>();
public Icon getIcon(String key) {
// Check if the icon already exists in the cache
if (iconCache.containsKey(key)) {
return iconCache.get(key);
} else {
// Create a new icon based on the key (type of icon)
Icon icon;
if (key.equals("file")) {
icon = new FileIcon("document", "document.png");
} else if (key.equals("folder")) {
icon = new FolderIcon("blue", "folder.png");
} else {
throw new IllegalArgumentException("Unsupported icon type: " + key);
}
// Store the created icon in the cache
iconCache.put(key, icon);
return icon;
}
}
}
// Client code to use the flyweight objects (icons)
public class Client {
public static void main(String[] args) {
IconFactory iconFactory = new IconFactory();
// Draw file icons at different positions
Icon fileIcon1 = iconFactory.getIcon("file");
fileIcon1.draw(100, 100);
Icon fileIcon2 = iconFactory.getIcon("file");
fileIcon2.draw(150, 150);
// Draw folder icons at different positions
Icon folderIcon1 = iconFactory.getIcon("folder");
folderIcon1.draw(200, 200);
Icon folderIcon2 = iconFactory.getIcon("folder");
folderIcon2.draw(250, 250);
}
}




Output
Drawing document icon with image document.png at position (100, 100)
Drawing document icon with image document.png at position (150, 150)
Drawing folder icon with color blue and image folder.png at po...


## When to use Flyweight Design Pattern

**When you need to create a large number of similar objects:** For instance, suppose you have to make hundreds of graphical objects (such as buttons and icons) with similar attributes (such as color and picture) but different positions and other variable features.**When memory consumption is a concern:** By sharing common state, the Flyweight pattern can assist reduce the memory footprint of memory-intensive applications that would otherwise require a large amount of RAM to create several instances of comparable objects.**When performance optimization is needed:** The pattern can enhance efficiency by lowering the overhead related to trash collection, object generation, and destruction by minimizing the number of objects.

## When not to use Flyweight Design Pattern

**When objects have unique intrinsic states:** If each object instance requires a unique set of intrinsic state that cannot be shared with other objects, applying the Flyweight pattern may not provide significant benefits.**When the overhead of implementing the pattern outweighs the benefits:** If the number of objects is relatively small or the shared state is minimal, the complexity introduced by the Flyweight pattern may not justify its implementation.**When mutable objects are involved:** The Flyweight pattern is best suited for immutable objects or objects whose intrinsic state does not change once initialized. If objects frequently change their intrinsic state, managing shared state can become complex and error-prone.**When the application does not have performance or memory constraints:** If memory usage and performance are not critical concerns for your application, implementing the Flyweight pattern may add unnecessary complexity without significant benefits.

## Conclusion

The Flyweight design pattern is valuable in situations where memory usage and performance optimization are crucial, especially when dealing with large numbers of similar objects. It facilitates efficient sharing of common state among multiple objects, thereby reducing memory footprint and improving performance. However, careful consideration should be given to the nature of objects, their state, and the overall design complexity before applying the Flyweight pattern.


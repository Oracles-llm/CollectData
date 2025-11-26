By Pankaj Kumar

Strategy design pattern is one of the **behavioral design pattern**. Strategy pattern is used when we have multiple algorithm for a specific task and client decides the actual implementation to be used at runtime.

Strategy pattern is also known as **Policy Pattern**. We define multiple algorithms and let client application pass the algorithm to be used as a parameter. One of the best example of strategy pattern is `Collections.sort()`

method that takes Comparator parameter. Based on the different implementations of Comparator interfaces, the Objects are getting sorted in different ways. For our example, we will try to implement a simple Shopping Cart where we have two payment strategies - using Credit Card or using PayPal. First of all we will create the interface for our strategy pattern example, in our case to pay the amount passed as argument. `PaymentStrategy.java`


```
package com.journaldev.design.strategy;
public interface PaymentStrategy {
public void pay(int amount);
}
```


Now we will have to create concrete implementation of algorithms for payment using credit/debit card or through paypal. `CreditCardStrategy.java`


```
package com.journaldev.design.strategy;
public class CreditCardStrategy implements PaymentStrategy {
private String name;
private String cardNumber;
private String cvv;
private String dateOfExpiry;
public CreditCardStrategy(String nm, String ccNum, String cvv, String expiryDate){
this.name=nm;
this.cardNumber=ccNum;
this.cvv=cvv;
this.dateOfExpiry=expiryDate;
}
@Override
public void pay(int amount) {
System.out.println(amount +" paid with credit/debit card");
}
}
```


`PaypalStrategy.java`


```
package com.journaldev.design.strategy;
public class PaypalStrategy implements PaymentStrategy {
private String emailId;
private String password;
public PaypalStrategy(String email, String pwd){
this.emailId=email;
this.password=pwd;
}
@Override
public void pay(int amount) {
System.out.println(amount + " paid using Paypal.");
}
}
```


Now our strategy pattern example algorithms are ready. We can implement Shopping Cart and payment method will require input as Payment strategy. `Item.java`


```
package com.journaldev.design.strategy;
public class Item {
private String upcCode;
private int price;
public Item(String upc, int cost){
this.upcCode=upc;
this.price=cost;
}
public String getUpcCode() {
return upcCode;
}
public int getPrice() {
return price;
}
}
```


`ShoppingCart.java`


```
package com.journaldev.design.strategy;
import java.text.DecimalFormat;
import java.util.ArrayList;
import java.util.List;
public class ShoppingCart {
//List of items
List<Item> items;
public ShoppingCart(){
this.items=new ArrayList<Item>();
}
public void addItem(Item item){
this.items.add(item);
}
public void removeItem(Item item){
this.items.remove(item);
}
public int calculateTotal(){
int sum = 0;
for(Item item : items){
sum += item.getPrice();
}
return sum;
}
public void pay(PaymentStrategy paymentMethod){
int amount = calculateTotal();
paymentMethod.pay(amount);
}
}
```


Notice that payment method of shopping cart requires payment algorithm as argument and doesn’t store it anywhere as instance variable. Let’s test our strategy pattern example setup with a simple program. `ShoppingCartTest.java`


```
package com.journaldev.design.strategy;
public class ShoppingCartTest {
public static void main(String[] args) {
ShoppingCart cart = new ShoppingCart();
Item item1 = new Item("1234",10);
Item item2 = new Item("5678",40);
cart.addItem(item1);
cart.addItem(item2);
//pay by paypal
cart.pay(new PaypalStrategy("myemail@example.com", "mypwd"));
//pay by credit card
cart.pay(new CreditCardStrategy("Pankaj Kumar", "1234567890123456", "786", "12/15"));
}
}
```


Output of above program is:

```
50 paid using Paypal.
50 paid with credit/debit card
```


That’s all for Strategy Pattern in java, I hope you liked it.

Thanks for learning with the DigitalOcean Community. Check out our offerings for compute, storage, networking, and managed databases.

Java and Python Developer for 20+ years, Open Source Enthusiast, Founder of https://www.askpython.com/, https://www.linuxfordevices.com/, and JournalDev.com (acquired by DigitalOcean). Passionate about writing technical articles and sharing knowledge with others. Love Java, Python, Unix and related technologies. Follow my X @PankajWebDev

Hello sir thank you very much for this information. Really you are the rock of Java…

- Raja

Hi Pankaj, Just want to say thanks for describing the design pattern so nicely.

- parag

Can we say strategy pattern is replacement for Switch Case / If Else ?

- Aashu

well done , but as i know with Strategy Design Pattern the Object of the class will change his Type i mean change the behaviour of the Object at the runtime ??

# Flyweight design pattern with real world example

Flyweight is a structural design pattern that helps us solve memory problems. Imagine that we have so many objects with common data and that take up much space, and consequently application performance is falling or some memory exception is occurring. The pattern can help us to solve that saving memory, which consequently improves the application performance. This is achieved by creating objects with common data and sharing it (cache) between many objects that use it. This way, application objects can leverage from shared objects that are known as Flyweight.

In the Flyweight, there are two concepts of object states:

**Extrinsic State —**unique state (i.e. state like id, name or something not shared) and mutable;**Intrinsic State**— common state and immutable (it will be shared).

Knowing these states can help us to find out and separate intrinsic state of objects.

Note that shared object must be immutable because many objects can use it. Changing the state can bring concurrency issues.


### Structure:

**Flyweight**is the interface with operations common between objects and that requires extrinsic state as parameter (Not required this interface, but can be used for code flexibility);**UnsharedFlyweight**is a mutable object with a unique state (can have intrisic object) that implements Flyweight and the client can instanciate;**ConcreteFlyweight**is an immutable object with common state (independent of context) that implements Flyweight and client should avoid to instanciate, instead client should call factory;**FlyweightFactory**is responsible for create or get a created Flyweight (cache mechanism). It holds all Flyweights and has a method to return the Flyweight;**Client**interact with factory to get Flyweights, instanciate UnsharedFlyweights and can hold the extrinsic state of them.

There are others variations of pattern some can consider an object called context (unique object) that holds intrinsic object and extrinsic object. And others approaches can consider a object with a immutable field with intrinsic value.

The main principle of pattern is cache common objects states avoiding a lot of same objects/data.


**Implementation:**

Above we saw a class diagram with a common Flyweight implementation. In that implementation, we have a Flyweight interface that defines common methods between Flyweights, some of those methods can receives the extrinsic state and use it for some action. Below the Flyweight interface there are two implementations on the left that ConcreateFlyweight that holds intrisic state, and on the right, the UnsharedFlyweight that holds extrinsic state and can hold intrisinc objects too. On the top of Flyweight interface there is a FlyweightFactory that is responsible for create and manage the cached objects, its main method create or get one of existing Flyweight based on intrinsic state. On the top of the image, there is a Client that can hold extrinsic state of objects, create Unshared object and call factory to create new Flyweights.

### Example:

Ah sheet, here we go again… to use the cosif example (other of my posts i´ve used that as example too). In short, the Cosif is a standard report (like balancesheet) that Central Bank requires for financial entities here in Brazil.

For our example we will create an object with the fields code (**Código**), description (**Descrição**), parentCode (**Conta Superior**), startDate (**Data início**) , endDate (**Data fim**), accountType (**Normal/Retificadora**) , aceeptsAnotherFunds (**Aplicável aos demais fundos**) and aceeptsFidc (**Aplicável a FIDC**) these fields were extracted from Cosif List. Excluding code, description, value and parentCode the others fields have values in common between many cosif objects.

Below we will separate the intrinsics and extrinsics fields.

**Intrinsic fields**— startDate, endDate, accountType, aceeptsAnotherFunds, aceeptsFidc;**Extrinsic fields—**code, description, parentCode, value.

Note that we could use parentCode as intrinsic, but here we won´t use it, because there aren’t many equals values like the other fields.

We could use the pattern with the previous post example using composite pattern, but for simplification a new example will be created.


Below we will see our classes of diagram implementation usign Java. First we will see our Flyweight called CosifFlyweight, which defines the common fields and a method calculateTotal that receives an extrinsic Double value (for our example the calculateTotal do any operation with Double).

`package br.com.design.pattern.flyweight;`


import java.util.Objects;


public class CosifFlyweight

{

private final String startDate;

private final String endDate;

private final String accountType;

private final boolean acceptsAnotherFunds;

private final boolean acceptsFidc;


public CosifFlyweight(

final String startDate,

final String endDate,

final String accountType,

final boolean acceptsAnotherFunds,

final boolean acceptsFidc )

{

this.startDate = startDate;

this.endDate = endDate;

this.accountType = accountType;

this.acceptsAnotherFunds = acceptsAnotherFunds;

this.acceptsFidc = acceptsFidc;

}


public String getStartDate()

{

return startDate;

}


public String getEndDate()

{

return endDate;

}


public String getAccountType()

{

return accountType;

}


public boolean isAcceptsAnotherFunds()

{

return acceptsAnotherFunds;

}


public boolean isAcceptsFidc()

{

return acceptsFidc;

}


public Double calculateTotal(

final Double value )

{

return value / 0.125;

}


@Override

public boolean equals(

final Object o )

{

if( this == o ) {

return true;

}

if( o == null || getClass() != o.getClass() ) {

return false;

}

final CosifFlyweight that = (CosifFlyweight) o;

return acceptsAnotherFunds == that.acceptsAnotherFunds && acceptsFidc == that.acceptsFidc && Objects.equals( startDate,

that.startDate ) && Objects.equals( endDate, that.endDate ) && Objects.equals( accountType, that.accountType );

}


@Override

public int hashCode()

{

return Objects.hash( startDate, endDate, accountType, acceptsAnotherFunds, acceptsFidc );

}

}

Next we will see our FlyweightFactory called CosifFlyweightFactory responsible for cache Flyweights. Here we stores the Flyweights on map with key an Integer (represents an hashcode calculated by intrinsic fields) and value the CosifFlyweight. There are two methods on Factory, first is public and used to get or create Flyweight in a map, and the second is used internally to create our map key using Arrays hashcode.

`package br.com.design.pattern.flyweight;`


import java.util.Arrays;

import java.util.HashMap;

import java.util.Map;


public final class CosifFlyweightFactory

{

private static final Map<Integer,CosifFlyweight> FLYWEIGHT_BY_HASHCODE = new HashMap<>();


public static CosifFlyweight getFlyweight(

final String startDate,

final String endDate,

final String accountType,

final boolean acceptsAnotherFunds,

final boolean acceptsFidc )

{

final Integer hashCode = calculateHashCode( startDate, endDate, accountType,

acceptsAnotherFunds, acceptsFidc );

return FLYWEIGHT_BY_HASHCODE.computeIfAbsent( hashCode,

hash -> new CosifFlyweight( startDate, endDate, accountType, acceptsAnotherFunds, acceptsFidc ) );

}


private static Integer calculateHashCode(

final String startDate,

final String endDate,

final String accountType,

final boolean acceptsAnotherFunds,

final boolean acceptsFidc )

{

return Arrays.hashCode( new Object[] {

startDate,

endDate,

accountType,

acceptsAnotherFunds,

acceptsFidc

} );

}

}

Next we will see our Unshared object here called Cosif that contains the extrinsic fields and the intrinsic object (i.e. our Flyweight). This class has a method with same name that out CosifFlyweight class but only delegate the calculation to CosifFlyweight passing as argument the extrinsic Double value.

`package br.com.design.pattern.flyweight;`


public class Cosif

{

private final Long code;

private final String description;

private final Long parentCode;

private final Double value;

private final CosifFlyweight flyweight;


public Cosif(

final Long code,

final String description,

final Long parentCode,

final Double value,

final CosifFlyweight flyweight )

{

this.code = code;

this.description = description;

this.parentCode = parentCode;

this.value = value;

this.flyweight = flyweight;

}


public Long getCode()

{

return code;

}


public String getDescription()

{

return description;

}


public Long getParentCode()

{

return parentCode;

}


public Double getValue()

{

return value;

}


public CosifFlyweight getFlyweight()

{

return flyweight;

}


public Double calculateTotal()

{

return flyweight.calculateTotal( this.value );

}

}

Finally, on the client was used a code to read a file with Cosifs and to create objects in Flyweight pattern and another without pattern. To see the effectiveness of pattern was comparated the memory usage of the two approaches. After running it we could see that with pattern the economy was of 33.39% of memory. Below we can see an image with logs of memory usage (here was used a lib called java object layout to had an estimate memory usage).

Note that the client can store the extrinsic objects of createCosifs method.


`package br.com.design.pattern.flyweight;`


import org.openjdk.jol.info.GraphLayout;


import java.io.IOException;

import java.util.ArrayList;

import java.util.List;

import java.util.Random;

import java.util.function.Function;

import java.util.logging.Logger;


public class CosifClient

{

private static final Logger LOGGER = Logger.getLogger( CosifClient.class.getName() );

private static final Random RANDOM = new Random();


public static void main(

final String[] args )

throws IOException

{

final List<String> cosifFields = readCosifs();

final long withoutFlyweight = memoryUsageWithoutFlyweight( cosifFields );

final long withFlyweight = memoryUsageWithFlyweight( cosifFields );

LOGGER.info( "Without Flyweight (memory in bytes) = " + withoutFlyweight );

LOGGER.info( "With Flyweight (memory in bytes) = " + withFlyweight );

LOGGER.info( "Diff (memory in bytes) = " + ( withoutFlyweight - withFlyweight ) );

LOGGER.info( String.format( "Economy (percentage) = %.4f", ( 1 - ( withFlyweight / (double) withoutFlyweight ) ) * 100 ) );

}


private static List<String> readCosifs()

throws IOException

{

...

}


private static long memoryUsageWithoutFlyweight(

final List<String> cosifFields )

{

//function to create nonflyweight object

final Function<Integer,CosifNonFlyweight> createFunction = idx -> new CosifNonFlyweight(

Long.valueOf( cosifFields.get( idx ) ),

cosifFields.get( idx + 1 ),

cosifFields.get( idx + 2 ),

cosifFields.get( idx + 3 ),

cosifFields.get( idx + 4 ),

Long.valueOf( cosifFields.get( idx + 5 ) ),

generateRandomDouble(),

isAccepts( cosifFields.get( idx + 6 ) ),

isAccepts( cosifFields.get( idx + 7 ) ) );

return calculateMemoryUsage( createCosifs( cosifFields, createFunction ) );

}


//Created for test memory usage only

//using Java 17

private record CosifNonFlyweight(

Long code,

String description,

String startDate,

String endDate,

String accountType,

Long parentCode,

Double value,

boolean acceptsAnotherFunds,

boolean acceptsFidc )

{

}


private static double generateRandomDouble()

{

return RANDOM.nextDouble();

}


private static boolean isAccepts(

final String value )

{

return value.equalsIgnoreCase( "Sim" );

}


private static <T> List<T> createCosifs(

final List<String> cosifFields,

final Function<Integer,T> createFunction )

{

final int size = cosifFields.size();

final List<T> result = new ArrayList<>();

for( int i = 0; i < size; i += 9) {

result.add( createFunction.apply( i ) );

}

return result;

}


private static long calculateMemoryUsage(

final List<?> values )

{

final GraphLayout graphLayout = GraphLayout.parseInstance( values );

LOGGER.info( graphLayout.toPrintable() );

return graphLayout.totalSize();

}


private static long memoryUsageWithFlyweight(

final List<String> cosifFields )

{

//this function uses the FlyweightFactory

//to get or create intrinsics objects from cache

//and create the object cosif

final Function<Integer,Cosif> createFunction = idx -> {

final CosifFlyweight flyweight = CosifFlyweightFactory.getFlyweight(

cosifFields.get( idx + 2 ),

cosifFields.get( idx + 3 ),

cosifFields.get( idx + 4 ),

isAccepts( cosifFields.get( idx + 6 ) ),

isAccepts( cosifFields.get( idx + 7 ) ) );

return new Cosif(

Long.valueOf( cosifFields.get( idx ) ),

cosifFields.get( idx + 1 ),

Long.valueOf( cosifFields.get( idx + 5 ) ),

generateRandomDouble(),

flyweight );

};

return calculateMemoryUsage( createCosifs( cosifFields, createFunction ) );

}

}

### (Dis)Advantages:

- Reduce quantity of objects and intrinsic state in objects—
;*advantage* - Reduce memory consume—
;*advantage* - Improve application performance—
;*advantage* - Can be overkill when don´t have a lot of objects—
;*disadvantage* - Shared Objects may be immutables—
;*advantage* - Sometimes can be complex implements when associated another pattern like composite —
;*disadvantage* - Mutable shared objects can bring concurrency issues —
*disadvantage;*

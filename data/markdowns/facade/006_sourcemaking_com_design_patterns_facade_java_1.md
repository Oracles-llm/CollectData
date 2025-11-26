Identify the desired unified interface for a set of subsystems

Design a "wrapper" class that can encapsulate the use of the subsystems

The client uses (is coupled to) the Facade

The facade/wrapper "maps" to the APIs of the subsystems

// 1. Subsystem
class PointCartesian {
private double x, y;
public PointCartesian(double x, double y ) {
this.x = x;
this.y = y;
}
public void move( int x, int y ) {
this.x += x;
this.y += y;
}
public String toString() {
return "(" + x + "," + y + ")";
}
public double getX() {
return x;
}
public double getY() {
return y;
}
}
// 1. Subsystem
class PointPolar {
private double radius, angle;
public PointPolar(double radius, double angle) {
this.radius = radius;
this.angle = angle;
}
public void rotate(int angle) {
this.angle += angle % 360;
}
public String toString() {
return "[" + radius + "@" + angle + "]";
}
}
// 1. Desired interface: move(), rotate()
class Point {
// 2. Design a "wrapper" class
private PointCartesian pointCartesian;
public Point(double x, double y) {
pointCartesian = new PointCartesian(x, y);
}
public String toString() {
return pointCartesian.toString();
}
// 4. Wrapper maps
public void move(int x, int y) {
pointCartesian.move(x, y);
}
public void rotate(int angle, Point o) {
double x = pointCartesian.getX() - o.pointCartesian.getX();
double y = pointCartesian.getY() - o.pointCartesian.getY();
PointPolar pointPolar = new PointPolar(Math.sqrt(x * x + y * y),Math.atan2(y, x) * 180 / Math.PI);
// 4. Wrapper maps
pointPolar.rotate(angle);
System.out.println(" PointPolar is " + pointPolar);
String str = pointPolar.toString();
int i = str.indexOf('@');
double r = Double.parseDouble(str.substring(1, i));
double a = Double.parseDouble(str.substring(i + 1, str.length() - 1));
pointCartesian = new PointCartesian(r*Math.cos(a*Math.PI/180) + o.pointCartesian.getX(),
r*Math.sin(a * Math.PI / 180) + o.pointCartesian.getY());
}
}
class Line {
private Point o, e;
public Line(Point ori, Point end) {
o = ori;
e = end;
}
public void move(int x, int y) {
o.move(x, y);
e.move(x, y);
}
public void rotate(int angle) {
e.rotate(angle, o);
}
public String toString() {
return "origin is " + o + ", end is " + e;
}
}
public class FacadeDemo {
public static void main(String[] args) {
// 3. Client uses the Facade
Line lineA = new Line(new Point(2, 4), new Point(5, 7));
lineA.move(-2, -4);
System.out.println( "after move: " + lineA );
lineA.rotate(45);
System.out.println( "after rotate: " + lineA );
Line lineB = new Line( new Point(2, 1), new Point(2.866, 1.5));
lineB.rotate(30);
System.out.println("30 degrees to 60 degrees: " + lineB);
}
}

Output

after move: origin is (0.0,0.0), end is (3.0,3.0)
PointPolar is [4.242640687119285@90.0]
after rotate: origin is (0.0,0.0), end is (2.5978681687064796E-16,4.242640687119285)
PointPolar is [0.9999779997579947@60.000727780827376]
30 degrees to 60 degrees: origin is (2.0,1.0), end is (2.499977999677324,1.8660127018922195)

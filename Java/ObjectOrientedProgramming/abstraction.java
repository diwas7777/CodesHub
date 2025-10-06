// Concept: Hiding internal implementation and showing only the essential features using abstract classes or interfaces.
abstract class Shape {
    abstract void draw();  // abstract method
}

class Circle extends Shape {
    void draw() {
        System.out.println("Drawing a Circle");
    }
}

public class AbstractionExample {
    public static void main(String[] args) {
        Shape shape = new Circle();
        shape.draw();
    }
}

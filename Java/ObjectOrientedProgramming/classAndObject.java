// Concept: A class is the blueprint to which an object serves as the instance to.
class Car { //class
    String brand;
    int year;

    void displayInfo() {
        System.out.println("Brand: " + brand + ", Year: " + year);
    }
}

public class ClassAndObject {
    public static void main(String[] args) {
        Car car1 = new Car();  // object
        car1.brand = "Toyota";
        car1.year = 2020;
        car1.displayInfo();

        Car car2 = new Car();
        car2.brand = "Tesla";
        car2.year = 2023;
        car2.displayInfo();
    }
}

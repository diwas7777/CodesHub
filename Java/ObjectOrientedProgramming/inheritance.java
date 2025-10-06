// Concept: One class inherits the properties and behaviour of another class using extend keyword. ('implements' in case of interfaces)
class Animal {
    void eat() {
        System.out.println("This animal eats food.");
    }
}

class Dog extends Animal {
    void bark() {
        System.out.println("Dog barks.");
    }
}

public class InheritanceExample {
    public static void main(String[] args) {
        Dog dog = new Dog();
        dog.eat();   // inherited
        dog.bark();  // own method
    }
}

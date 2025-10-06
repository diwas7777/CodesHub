//This is method overriding aka runtime polymorphism
class Animal {
    void sound() {
        System.out.println("Animal makes a sound");
    }
}

class Cat extends Animal {
    @Override
    void sound() {
        System.out.println("Cat meows");
    }
}

public class MethodOverriding {
    public static void main(String[] args) {
        Animal myAnimal = new Cat();  // Upcasting
        myAnimal.sound();  // Runtime polymorphism
    }
}

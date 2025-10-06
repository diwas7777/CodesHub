// Concept: Interfaces defines a contract that the implementing classes must follow (no implementation in interface class)
interface Vehicle {
    void start();
    void stop();
}

class Bike implements Vehicle {
    public void start() {
        System.out.println("Bike starting...");
    }
    public void stop() {
        System.out.println("Bike stopped.");
    }
}

public class InterfaceExample {
    public static void main(String[] args) {
        Vehicle v = new Bike();
        v.start();
        v.stop();
    }
}

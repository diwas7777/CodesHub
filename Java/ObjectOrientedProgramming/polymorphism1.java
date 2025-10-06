// Concept: 'poly' means many, 'morphism' means forms
//This is method overloading aka compile-time polymorphism
class MathUtils {
    int add(int a, int b) {
        return a + b;
    }

    double add(double a, double b) {
        return a + b;
    }
}

public class MethodOverloading {
    public static void main(String[] args) {
        MathUtils m = new MathUtils();
        System.out.println(m.add(5, 10));
        System.out.println(m.add(5.5, 3.2));
    }
}

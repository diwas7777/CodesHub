// Concept: 
// Constructors are the special type of methods that initializes a class's object when it's created, automatically called by the new keyword.
// 'this' keyword is used to refer to the current object or context in which the code is executing
class Student {
    String name;
    int age;

    Student(String name, int age) {
        this.name = name;
        this.age = age;
    }

    void show() {
        System.out.println("Name: " + name + ", Age: " + age);
    }
}

public class ConstructorExample {
    public static void main(String[] args) {
        Student s1 = new Student("Rajan", 21);
        s1.show();
    }
}

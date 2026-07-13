// File: TaskManagerApp.java
// A simple OOP-based Task Management (To-Do List) program in Java

import java.util.ArrayList;
import java.util.Scanner;

// Represents a single Task with details
class Task {
    private String title;
    private String description;
    private boolean isCompleted;

    // Constructor
    public Task(String title, String description) {
        this.title = title;
        this.description = description;
        this.isCompleted = false; // Default status: not completed
    }

    // Getter and Setter methods (Encapsulation)
    public String getTitle() {
        return title;
    }

    public String getDescription() {
        return description;
    }

    public boolean isCompleted() {
        return isCompleted;
    }

    public void markAsCompleted() {
        isCompleted = true;
    }

    @Override
    public String toString() {
        return "[ " + (isCompleted ? "✓" : "✗") + " ] " + title + " - " + description;
    }
}

// Manages a list of tasks
class TaskManager {
    private ArrayList<Task> tasks;

    // Constructor initializes the list
    public TaskManager() {
        tasks = new ArrayList<>();
    }

    // Add a new task
    public void addTask(String title, String description) {
        Task newTask = new Task(title, description);
        tasks.add(newTask);
        System.out.println("✅ Task added successfully!");
    }

    // View all tasks
    public void viewTasks() {
        if (tasks.isEmpty()) {
            System.out.println("📭 No tasks available.");
            return;
        }

        System.out.println("\n🗂️  Your Tasks:");
        for (int i = 0; i < tasks.size(); i++) {
            System.out.println((i + 1) + ". " + tasks.get(i));
        }
    }

    // Mark a task as completed
    public void completeTask(int index) {
        if (index < 0 || index >= tasks.size()) {
            System.out.println("❌ Invalid task number!");
            return;
        }
        tasks.get(index).markAsCompleted();
        System.out.println("🎯 Task marked as completed!");
    }

    // Delete a task
    public void deleteTask(int index) {
        if (index < 0 || index >= tasks.size()) {
            System.out.println("❌ Invalid task number!");
            return;
        }
        tasks.remove(index);
        System.out.println("🗑️ Task deleted successfully!");
    }
}

// Main class with menu-driven interface
public class ToDoListApp {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        TaskManager manager = new TaskManager();
        int choice;

        System.out.println("====== 📝 Task Management / To-Do App ======");

        do {
            System.out.println("\nChoose an option:");
            System.out.println("1. Add Task");
            System.out.println("2. View Tasks");
            System.out.println("3. Mark Task as Completed");
            System.out.println("4. Delete Task");
            System.out.println("5. Exit");
            System.out.print("Enter your choice: ");

            choice = sc.nextInt();
            sc.nextLine(); // Consume newline

            switch (choice) {
                case 1:
                    System.out.print("Enter task title: ");
                    String title = sc.nextLine();
                    System.out.print("Enter task description: ");
                    String description = sc.nextLine();
                    manager.addTask(title, description);
                    break;

                case 2:
                    manager.viewTasks();
                    break;

                case 3:
                    manager.viewTasks();
                    System.out.print("Enter task number to mark as completed: ");
                    int completeIndex = sc.nextInt() - 1;
                    manager.completeTask(completeIndex);
                    break;

                case 4:
                    manager.viewTasks();
                    System.out.print("Enter task number to delete: ");
                    int deleteIndex = sc.nextInt() - 1;
                    manager.deleteTask(deleteIndex);
                    break;

                case 5:
                    System.out.println("👋 Exiting... Have a productive day!");
                    break;

                default:
                    System.out.println("⚠️ Invalid choice! Try again.");
            }
        } while (choice != 5);

        sc.close();
    }
}

package javaProjects;

import java.util.Scanner;

public class Main {

	public static void main(String[] args) {
		Scanner scanner = new Scanner(System.in);
		
		System.out.print("Enter m for male , f for female & o for other:"); //Taking input from user
		
		String gender = scanner.nextLine();
		
		switch(gender){
		
		
		case "m":
			System.out.println("You are a male.");
			break;
		
		case "f":
			System.out.println("You are a female.");
			break;
		
		case "o":
			System.out.println("You are other.");
			break;
			
		default:
		System.out.println("Enter the gender correctly!");

	}

}
}

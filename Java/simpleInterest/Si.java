package javaProjects;

import java.util.Scanner;

public class Si {
	
	public static void main(String [] args) {
		Scanner scanner = new Scanner(System.in);
		
		System.out.print("Enter the principal:$");
		int principal = scanner.nextInt();
		
		System.out.print("Enter the time (in year):");
		int time = scanner.nextInt();
		
		System.out.print("Enter the rate:");
		int rate = scanner.nextInt();
		
		int interest = (principal * time * rate) / 100;
		
		System.out.printf("Simple interest:%d per annum",interest);
		
		
		
	}
}

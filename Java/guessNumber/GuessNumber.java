import java.util.Random;
import java.util.Scanner;
public class GuessNumber
{



        public static void main(String[] args) {
        System.out.printf("***Welcome  Guess Number game ****\n");

        Random ra = new Random();
        int gen = ra.nextInt(10);
        System.out.printf("Guess ? \n");
            int number ;
            System.out.printf("Enter the number to guess between 0 to 9 \n");
            Scanner scan = new Scanner(System.in);
            number = scan.nextInt();

    do {
        if (number>gen)
        {
            System.out.printf("Please try again  Number %d > ? \n",number);
            number = scan.nextInt();
        }

        else
        {

            System.out.printf("Please try again  Number %d < ? \n",number);

            number = scan.nextInt();


        }

    }while ( number!=gen);


            System.out.println("Great you won " + " number is " + gen );

        }


}

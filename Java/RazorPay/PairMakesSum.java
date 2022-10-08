package RazorPay;

/*  RAZORPAY Q1 :
    Program to find the sum of Pair of numbers in reverse order of given array.
    Example :
        Input :
            Number of elements : 5
            Enter elements :
                            10
                            5
                            6
                            3
                            8
            Target sum : 11

        Output :
            true
            3,8

     Explanation : given array of 5 elements we can consider the reverse array hence 8 and 3 will be the first pair which
     matches target 11 ( i.e. 8+3=11 )  so output will be true and a pair of numbers.
*/

import java.util.Scanner;

public class PairMakesSum {
    static String result;
    public static void main(String[] args)
    {
        int size,x;
        int[] A;
        Scanner input=new Scanner(System.in);
        System.out.print("Number of elements : ");
        size=input.nextInt();

        A=new int[size];
        System.out.println("Enter elements :");
        for(int i=0;i<size;i++)
        {
            A[i]=input.nextInt();
        }

        System.out.print("Target sum : ");
        x=input.nextInt();

       if(checkPair(A,size,x))
       {
           System.out.println(true);
           System.out.println(result);
       }
       else
       {
           System.out.println(false);
       }
    }

    public static boolean checkPair(int[] A, int size, int x)
    {
        for(int i=size-1;i>=0;i--)
        {
            for(int j=i+1;j<size;j++)
            {
                if(A[i]+A[j]==x)
                {
                   result=A[i]+","+A[j];
                   return true;
                }
            }
        }
        return false;
    }
}

package RazorPay;

/*  RAZORPAY Q2 :
    Program to check below two Cases
    1. Count of 0's and 1's should be equal
    2. Count of 1's should be greater than or equals  0's is every substring

    Example :
        Input :
            110010

        Output :
            true


     Explanation :
       Case 1 : count of 0's and 1's = 3 each ( 3 0's and 3 1's ), hence First condition True
       Case 2 : count of 1's in every substring is greater than or equals to count of 0's.
               i.e. 1 : Count of 1's is =1 count of 0's=0
                   11 : Count of 1's is =2 count of 0's=0
                  110: Count of 1's is =2 count of 0's=1
                 1100: Count of 1's is =2 count of 0's=2
                11001: Count of 1's is =3 count of 0's=2
               110010: Count of 1's is =3 count of 0's=3
*/

import java.util.Scanner;

public class MagicalBinaryString
{
    public static void main(String[] args)
    {
        Scanner input= new Scanner(System.in);
        String s=input.nextLine();
        boolean magicalFirstCase,magicalSecondCase,magical=false;

        magicalFirstCase=s.chars().filter(c->c=='0').count()==s.chars().filter(c->c=='1').count();
        magicalSecondCase=true;

        for(int i=1;i<s.length();i++)
        {
            String temp=s.substring(0,i);
            if(temp.chars().filter(c->c=='0').count()>temp.chars().filter(c->c=='1').count())
            {
                magicalSecondCase=false;
                break;
            }
        }

        System.out.println(magicalFirstCase&magicalSecondCase);

    }
}

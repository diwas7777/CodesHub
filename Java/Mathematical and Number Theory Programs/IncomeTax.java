import  java.util.Scanner ;
public class IncomeTax {
    public static void main(String[] args)
    {
        float Amount  ;
        float tax = 0;
        System.out.println("Enter the income amount to get info of Income  tax");
        Scanner sc = new Scanner(System.in);
        Amount = sc.nextFloat();
        if (Amount>2.5f && Amount<=5f)
        {
           tax = tax + 0.05f*(Amount-2.5f);
        }
       else if (Amount>5f && Amount<10.f)
        {
           tax = tax + 0.05f*(5.0f -2.5f);
           tax = tax + 0.2f*(Amount-5f);

        }
       else if(Amount>10.f)
        {
           tax = tax + 0.05f*(5.0f -2.5f);
           tax = tax + 0.2f*(10.0f  - 5f);
           tax = tax + 0.3f*(Amount - 10.0f);
        }
       else
       {
           tax = 0 ;
       }

        System.out.println("Tax paid by employ " + tax );
    }

}

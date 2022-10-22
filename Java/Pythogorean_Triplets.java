import java.util.Scanner;
public class PythogoreanTriplets {
    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);

        int a = in.nextInt();
        int b = in.nextInt();
        int c = in.nextInt();

        int max=a;
        if(b>a){
            max=b;
        }
        if(c>a){
            max=c;
        }

        if(max==a){
            boolean check = (b*b+c*c)==(a*a);
            System.out.println(check);
        }
        else if(max==b){
            boolean check = (a*a+c*c)==(b*b);
            System.out.println(check);
        }
        else{
            boolean check = (b*b+a*a)==(c*c);
            System.out.println(check);
        }
    }
}

import java.util.*;
public class Main
{
  public static void main(String[] args) {
  Scanner s=new Scanner(System.in);
  int n=s.nextInt();
  int x=palindrom(n); //getting the returned valued and storing it in x
  if(x==1){ // the value which is returned is only present in 0 or 1 
      System.out.println("it is palindrom"); // x is 1 then it is palindrome 
  }
  else{
      System.out.println("it is not palindrom"); //else it is not palindrome
  }
  }
   static int palindrom(int n){
       int r=n; // stroing the original n value into r to check after 
       int t=0; //reversing the integer 
       while(n>0){
           t=t*10+n%10;
           n=n/10;
       }
       
       if(r==t){
           return 1;
       }
       else
       return 0;
    
   }
}

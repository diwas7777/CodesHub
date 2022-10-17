class Main{
    public static void main(String[] args) {
        
       //Declaring the variables.
        
        int a;
        int b;
        
        //We need another variable to shift the values.
        int c;
        
        a = 2;
        b = 3;

        //Printing the assigned values.

      System.out.printf("The old value of a was %d.\n",a);
      System.out.printf("The old value of b was %d.\n",b);

      System. out. println(); //Printing a empty line.
      
        //Shifting the values
        c = b; //First, we will put the value of b in c (Now the b will be empty).
        b = a; //Second, we will put the value of a in b (Now the a will be empty).
        a = c; //At beginning we kept the value of b in c. 
        
        /* Hence, the values of both a and b are successfully exchanged.
        Lets,print the new values. */
        
        System.out.printf("The new value of a is %d.\n",a);
        System.out.printf("The new value of b is %d.",b);
    }
}
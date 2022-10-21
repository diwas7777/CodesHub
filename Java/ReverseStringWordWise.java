
public class ReverseStringWordWise {
	public static String reverseWordWise(String input) {
	    
        StringBuffer str = new StringBuffer();
        input=" "+input;
        int prevPosition=input.length()-1;
        for (int i=input.length()-1;i>=0;i--)
        {
            if (input.charAt(i) == ' ')
            {
                str.append(input.substring(i,prevPosition+1));
                prevPosition=i-1;
            }
        }
        return (str.toString()).trim();

	}
	public static void main(String[] args){
	    
	   String str = "Welcome to Github";
       String result = reverseWordWise(str);
       System.out.println(result); 
	}
}
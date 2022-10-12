public class PascalsTriangle {

    static int[] factorialArray = new int[10];

    public static void main(String[] args) {
        initialization();
        computeFactorial();

        int numberOfLines = 4;

        for (int i = 0; i <= numberOfLines; i++) {
            for (int j = 0; j <= numberOfLines - i; j++) {
                System.out.print(" ");
            }

            for (int j = 0; j <= i; j++)
                System.out.print(" " + factorialArray[i] / (factorialArray[i - j] * factorialArray[j]));

            System.out.println();
        }
    }

    private static void computeFactorial() {
        for (int i = 1; i < factorialArray.length; i++)
            factorialArray[i] = i * factorialArray[i - 1];
    }

    private static void initialization() {
        factorialArray[0] = 1;
        factorialArray[1] = 1;
    }

}

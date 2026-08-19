#include <stdio.h>

int main(){
while (1){
    int num1, num2, res;

        printf("=====Calculator in C=====\n");
        printf("1 - Add\n");
        printf("2 - Subtract\n");
        printf("3 - Multiply\n");
        printf("4 - Divide\n");
        printf("5 - Exit\n");

        printf("=========================\n");
        printf("What type of calculation will you do: ");
        scanf("%d", &res);

        //conditionals
        if (res == 1){
            printf("What is the first number to be calculated: ");
            scanf("%d", &num1);

            printf("What is the second number to be calculated: ");
            scanf("%d", &num2);

            printf("The sum %d + %d is %d\n", num1, num2, num1 + num2);
        }

        else if (res == 2){
            printf("What is the first number to be calculated: ");
            scanf("%d", &num1);

            printf("What is the second number to be calculated: ");
            scanf("%d", &num2);

            printf("The subtraction %d - %d is %d\n", num1, num2, num1 - num2);
        }
        else if (res == 3){
            printf("What is the first number to be calculated: ");
            scanf("%d", &num1);

            printf("What is the second number to be calculated: ");
            scanf("%d", &num2);

            printf("The multiplication %d * %d is %d\n", num1, num2, num1 * num2);
        }
        else if (res == 4){
            printf("What is the first number to be calculated: ");
            scanf("%d", &num1);

            printf("What is the second number to be calculated: ");
            scanf("%d", &num2);

            printf("The division %d / %d is %d\n", num1, num2, num1 / num2);
        }
        else if (res == 5){
            break;
        }
    }
}
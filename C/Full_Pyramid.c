#include<stdio.h>
#include<conio.h>
void main(){
    int x,y,z;
    printf("Enter no. of rows: ");
    scanf("%x",&x);
    for(int i=1;i<=x;i++){
        y=i;
        z=0;
        while (y!=0)
        {
            while (z <= x-y)
            {
                printf(" ");
                ++z;
            }
            printf("x");
            --y;
        }
        printf("\n");
        
    }
}
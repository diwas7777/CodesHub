#include<stdio.h>
#include<math.h>
 
int main()
{
    float a, b, c, s, area;
    printf("\nEnter three sides of triangle\n");
    scanf("%f%f%f",&a,&b,&c);
    s = (a+b+c)/2;
 
    //Calculate area of triangle
    area = sqrt(s*(s-a)*(s-b)*(s-c));
 
    //Area with 2 digits of precision
    printf("\n Area of triangle: %.2f\n",area);
}

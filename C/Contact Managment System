#include<stdio.h>
#include<string.h>
typedef struct contact{
    long long int phoneno;
    char name[100];
}person;
person user[1000];
int main(){
 int choice,index=1,ch;
 char search[100];
 main:printf("**********Welcome to Contacts**********");
 printf("\n*************Main Menu*****************\n[1]Add a new contact \n[2]Search a user \n[3]List contacts \n[4]Exit\n");
 printf("Enter a choice:");
 scanf("%d",&choice);
 switch(choice){
    case 1:
     printf("Enter name:");
     scanf("%s",&user[index].name);
     printf("Enter mobile number:");
     scanf("%lld",&user[index].phoneno);
     printf("\n\nContact successfully created!\n%s now successfully added to your contacts.",user[index].name);
     index++;
     break;
    case 2:
     printf("Enter name:");
     scanf("%s",&search);
     for(int i=0;i<=index;i++){
       if(strcmp(search,user[i].name)==0){
        printf("Mobile Number:%lld",user[i].phoneno);
        break;
       }
     }
     break;
    case 3:
     for(int i=1;i<index;i++){
        printf("Name of contact:%s\t\tPhone number:%lld\n",user[i].name,user[i].phoneno);
     } 
     break;
    case 4:
     printf("Thank you");
     break;
    default:
     printf("Invalid choice");
 }
    printf("\n\n\nTo continue choose:\n[1] Main Menu\n[0] Exit\n");
    scanf("%d",&ch);
    switch (ch)
    {
    case 1:
        goto main;
    case 0:
        printf("Thank you");
        break;
    default:
        printf("Invalid choice");
        break;
    }
    return 0;
}

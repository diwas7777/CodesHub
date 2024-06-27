//login  manager
//login user
//fill inventory
//order menu
#include <stdio.h>
int main(){
    typedef enum {false, true} bool;
    int choice;
    int inventory[3]={100,100,100};
    int prices[3]={89,40,35};
    while(true){
        printf("------------------------------\n");
        printf("|WELCOME TO FOOD ORDER CLI !!|\n");
        printf("|LOGIN TO PROCEED!!          |\n");
        printf("|----------------------------|\n");
        printf("                              \n");
        printf("1) LOGIN AS MANAGER \n");
        printf("2) LOGIN AS USER \n");
        printf("3) EXIT \n");
        printf("ENTER A CHOICE :- ");
        scanf("%d",&choice);
        if(choice==1){
            while(true){
                int password,managerChoice;
                bool isLoggedin=false;

                printf("!! ENTER THE PASSWORD !!\n");
                scanf("%d",&password);
                if(password==1234){
                    isLoggedin=true;
                    printf("LOGGED IN AS MANAGER\n");
                    while(isLoggedin==true){

                        printf("|-----MANAGER---MENU---------| \n");
                        printf("|1) FILL INVENTORY ----------| \n");
                        printf("|2) EXIT           ----------| \n");
                        printf("|----------------------------| \n");
                        printf("ENTER A CHOICE :- ");
                        scanf("%d",&managerChoice);

                        if(managerChoice==1){
                            if((inventory[0]<100)|| (inventory[1]<100) || (inventory[1]<100) ){
                                inventory[0]=100;
                                inventory[1]=100;
                                inventory[2]=100;
                                printf("INVENTORY HAS BEEN REPLINISHED !! \n");

                                }
                                else{
                                printf("INVENTORY IS ALREADY FILLED !! \n");
                                // break;
                                }
                        }
                        else if(managerChoice==2){
                            isLoggedin=false;
                            // break;
                        }
                    }
                }else{
                    break;
                }
            }
        }else if(choice==2){

            while(true){
                int userChoice,burger,fries,cola,total;
                printf("WELCOME USER !!\n");
                printf("1) ORDER FOOD\n");
                printf("2) EXIT\n");
                printf("enter a choice user :- \n");
                scanf("%d",&userChoice);
                if(userChoice==1){
                    printf("enter the number of burgers you want to buy :- \n");
                    scanf("%d",&burger);
                    printf("enter the number of fries you want to buy :- \n");
                    scanf("%d",&fries);
                    printf("enter the number of cola you want to buy:- \n");
                    scanf("%d",&cola);
                    inventory[0]=inventory[0]-burger;
                    inventory[1]=inventory[1]-fries;
                    inventory[2]=inventory[2]-cola;
                    total=burger*prices[0]+fries*prices[1]+cola*prices[2];

                    if(inventory[0]<=0 || inventory[1]<=0 || inventory[2]<=0){
                        printf("STOCK OUT HAI KAL ANA!! ");
                    }else{
                        printf("\n\n");
                        printf("|------------YOUR ORDER IS-------------|\n");
                        printf("|Burgers:- %d | Fries:- %d | Cola:- %d ---|\n",burger,fries,cola);
                        printf("|--------------------------------------|\n");
                        printf("|-----------------------Total:-%d---|\n",total);
                        printf("\n\n");
                        printf(" pay to upi id:-  BajjuFoodChanin@khemkhapay \n\n\n");
                    }
                }
                else if(userChoice==2){
                    break;
                }
            }
        }else if(choice==3){
            printf("BYE BYE USER >_< . COME BACK AGAIN!! ");
            break;
        }
    }
    return 0;
}

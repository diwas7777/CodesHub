// Simple Shopping List CLI App in C

#include <stdio.h>
#include <stdlib.h>
#include <string.h>

char** item_names;       // array of item names
char** item_quantities;  // array of item quantities
char *name;
char *quantity;
int items;               // number of items in the list
int menu;

// Read a single-digit integer (returns -1 for invalid input)
int r_int(){
    char c[3];
    fgets(c,sizeof(c),stdin);
    fflush(stdin);        // undefined behavior, but used here
    if(c[0] != '\n' && c[1] == '\n'){
        return c[0] - '0'; 
    } else {
        return -1;
    }
}

// Read a string, returns "0" if input is empty
char* r_str(){
    char c[30];
    fgets(c, sizeof(c), stdin);
    fflush(stdin);        // undefined behavior, but used here
    c[strcspn(c, "\n")] = '\0';   // remove newline
    if (c[0] == '\0') {
        return strdup("0");       // default value
    } else {
        return strdup(c);
    }
}

int main(){
    items = 0;

    while(1){
        // Menu display
        printf("\n--Shopping List--\n1.Add Item\n2.Delete Item\n3.Show List\n0.Close\nChoice: ");
        menu = r_int();

        switch (menu){
            case 1:  // Add item
                printf("Item name: ");
                name = r_str();
                if(name[0] != '0'){          // if name entered
                    printf("Item quantity: ");
                    quantity = r_str();
                    if(quantity[0] != '0'){ // if quantity entered
                        printf("\nItem added!\n");
                        items++;

                        // Allocate memory for new item
                        item_names = realloc(item_names,items*sizeof(char*));
                        item_names[items-1] = strdup(name);

                        item_quantities = realloc(item_quantities,items*sizeof(char*));
                        item_quantities[items-1] = strdup(quantity);
                    }
                }
                break;

            case 2:  // Delete item
                while(1){
                    if(items > 0){
                        printf("\nChoose item to remove:\n");
                        for(int i=0;i<items;i++){
                            printf("%d.%s\n",i+1,item_names[i]);
                        }
                        printf("0.(Back)\nChoice: ");
                        int choice = r_int();
                        if(choice == 0) break;
                        else if (choice > 0 && choice <= items){
                            printf("\nItem %s removed!\n",item_names[choice-1]);

                            // Create temporary arrays excluding deleted item
                            char** temp_names = malloc((items-1)*sizeof(char*));
                            char** temp_quantities = malloc((items-1)*sizeof(char*));
                            int count = 0;
                            for(int i=0;i<items;i++){
                                if(i+1 != choice){
                                    temp_names[count] = strdup(item_names[i]);
                                    temp_quantities[count] = strdup(item_quantities[i]);
                                    count++;
                                }
                                free(item_names[i]);
                                free(item_quantities[i]);
                            }
                            items--;
                            free(item_names);
                            free(item_quantities);
                            item_names = temp_names;
                            item_quantities = temp_quantities;
                        } else {
                            printf("\nInvalid Input!\n");
                        }
                    } else {
                        printf("\nYou dont have any items in the list...");
                        fflush(stdin);
                        getchar();
                        break;
                    }
                }
                break;

            case 3:  // Show list
                if(items>0){
                    printf("\nYour shopping List:\n");
                    for(int i=0;i<items;i++){
                        printf("%d.%s - %s\n",i+1,item_names[i],item_quantities[i]);
                    }
                    printf("\n(Back)");
                    fflush(stdin);
                    getchar();
                } else {
                    printf("\nYou dont have any items in the list...");
                    fflush(stdin);
                    getchar();
                }   
                break;

            case 0:  // Exit
                break;

            default: // Invalid menu input
                printf("\nInvalid Input!\n");
                break;
        }

        if(menu == 0){
            printf("Exiting...");
            break;
        }
    }
}

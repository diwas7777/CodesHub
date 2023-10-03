#include <stdio.h>
#include <string.h>
#include <time.h>
#include <stdlib.h>

void Encrypt_Decrypt(char *array, char *string, long int key)
{
    int i, j;
    for (i = strlen(array) - 1; i > 0; i--)
    {
        j = key % i;
        char temp = array[i];
        array[i] = array[j];
        array[j] = temp;
    }
}

int main()
{
    char array[100] = " ", sarray[100] = " ", string[1000] = " ", result[1000] = " ", choice = ' ';
    long int key = 0; 
    int i = 0, j = 0;
    for (i = 32; i < 127; i++)
    {
        array[i - 32] = i;
    }
    strcpy(sarray, array);
choose:
    printf("\n1.Encryption\n2.Decryption\n");
    printf("What do you wanna do? ");
    scanf("%c", &choice);
    getchar();
    if (choice == '1')
    {
        printf("\nPress Y if you want to set a custom key\nPress anything else to generate a random key: ");
        scanf("%c", &choice);
        getchar();
        if (choice == 'Y' || choice == 'y')
        {
            printf("\nSet up a number key: ");
            scanf("%ld",&key);
            getchar();
        }
        else
        {
            srand(time(NULL));
            for (i = 0; i <= 500; i++)
            {
                srand(rand() - (i / rand()));
            }
            key = rand();
            printf("\nYour key- %ld\n",key);
            choice = '1';
        }
        printf("\nEnter the string you want to Encrypt: ");
        fgets(string, sizeof(string), stdin);
        Encrypt_Decrypt(sarray, string, key);
    }
    else if (choice == '2')
    {
        printf("\nEnter the string you want to Decrypt: ");
        fgets(string, sizeof(string), stdin);
        printf("\nEnter the key: ");
        scanf("%ld", &key);
        Encrypt_Decrypt(array, string, key);
    }
    else
    {
        printf("\nChoose between 1 and 2\n");
        goto choose;
    }

    for (i = 0; i < strlen(string); i++)
    {
        for (j = 0; j < strlen(array); j++)
        {
            if (string[i] == array[j])
            {
                result[i] = sarray[j];
                continue;
            }
        }
    }
    choice == '2'?printf("\nDecryption : %s", result):printf("\nEncryption : %s", result);
    return 0;
}

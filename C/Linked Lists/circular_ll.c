// Circular Linked List

#include <stdio.h>
#include <conio.h>
#include <stdlib.h>

struct Node {
    int data;
    struct Node *next;
};

struct Node *node = NULL, *list = NULL, *last = NULL, *temp = NULL, *p = NULL;
int count = 0;

struct Node *createNode(int info) {
    node = (struct Node*)malloc(sizeof(struct Node));
    node->data = info;
    node->next = NULL;
    count++;
    return node;
}

void AddAtFront(int info) {
    node = createNode(info);
    if (list == NULL) {
        list = last = node;
        last->next = list; // Point last to the first node
    } else {
        node->next = list;
        list = node;
        last->next = list; // Maintain circular link
    }
}

void AddAtEnd(int info) {
    node = createNode(info);
    if (list == NULL) {
        list = last = node;
        last->next = list; // Point last to the first node
    } else {
        last->next = node;
        last = node;
        last->next = list; // Maintain circular link
    }
}

void AddAtPosition(int info, int pos) {
    if (pos == 1) {
        AddAtFront(info);
    } else if (pos == (count + 1)) {
        AddAtEnd(info);
    } else {
        node = createNode(info);
        temp = list;
        for (int i = 1; i < pos - 1; i++) {
            temp = temp->next;
        }
        node->next = temp->next;
        temp->next = node;
    }
}

void DeleteAtFront() {
    if (list == NULL) {
        printf("\nList is Empty!\n");
    } else {
        temp = list;
        if (list == last) { // Only one node in the list
            list = last = NULL;
        } else {
            list = list->next;
            last->next = list; // Maintain circular link
        }
        printf("\nNode deleted: %d\n", temp->data);
        free(temp);
        count--;
    }
}

void DeleteAtEnd() {
    if (list == NULL) {
        printf("\nList is Empty!\n");
    } else {
        temp = list;
        if (list == last) { // Only one node in the list
            printf("\nNode deleted: %d\n", last->data);
            free(last);
            list = last = NULL;
        } else {
            while (temp->next != last) {
                temp = temp->next;
            }
            printf("\nNode deleted: %d\n", last->data);
            temp->next = list; // Maintain circular link
            free(last);
            last = temp;
        }
        count--;
    }
}

void DeleteAtPosition(int pos) {
    if (pos == 1) {
        DeleteAtFront();
    } else if (pos == count) {
        DeleteAtEnd();
    } else {
        temp = list;
        p = NULL;
        for (int i = 1; i < pos; i++) {
            p = temp;
            temp = temp->next;
        }
        printf("\nNode deleted: %d\n", temp->data);
        p->next = temp->next;
        free(temp);
        count--;
    }
}

int Search(int info) {
    int pos = 1;
    if (list == NULL) {
        printf("\nList is Empty!");
        return -1;
    } else {
        temp = list;
        do {
            if (temp->data == info) {
                return pos;
            }
            temp = temp->next;
            pos++;
        } while (temp != list);
    }
    return -1;
}

void SearchAndDelete(int info) {
    int pos = Search(info);
    if (pos != -1) {
        DeleteAtPosition(pos);
    } else {
        printf("\nNo Data Found!");
    }
}

void Display() {
    if (list == NULL) {
        printf("\nList is Empty!\n");
    } else {
        temp = list;    
        do {
            printf("%d -> ", temp->data);
            temp = temp->next;
        } while (temp != list);
        printf("(back to %d)\n", list->data); // Indicate circular nature
    }
}

void main() {
    int choice, data, pos;
    
    clrscr();
    
    do {
        printf("\nEnter choice: \n1. Add At Front\n2. Add At End\n3. Add At Position\n4. Delete At Front\n5. Delete At End\n6. Delete At Position\n7. Search\n8. Exit\n");
        scanf("%d", &choice);
        switch (choice) {
            case 1: 
                printf("\nEnter data: ");
                scanf("%d", &data);
                AddAtFront(data);
                Display();
                break;
            case 2: 
                printf("\nEnter data: ");
                scanf("%d", &data);
                AddAtEnd(data);
                Display();
                break;
            case 3: 
                printf("\nEnter data: ");
                scanf("%d", &data);
                printf("\nEnter position: ");
                scanf("%d", &pos);
                AddAtPosition(data, pos);
                Display();
                break;
            case 4: 
                DeleteAtFront();
                Display();
                break;
            case 5: 
                DeleteAtEnd();
                Display();
                break;
            case 6: 
                printf("\nEnter position: ");
                scanf("%d", &pos);
                DeleteAtPosition(pos);
                Display();
                break;
            case 7: 
                printf("\nEnter data: ");
                scanf("%d", &data);
                pos = Search(data);
                if (pos != -1) {
                    printf("\nPosition: %d\n", pos);
                } else {
                    printf("\nData Not Found!");
                }
                break;
            case 8: 
                printf("\nExiting...\n");
                break;
            default: 
                printf("\nEnter valid choice!\n");
        }
    } while (choice != 8);
    
    getch();
}

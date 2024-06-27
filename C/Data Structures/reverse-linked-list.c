#include <stdio.h>
struct Node {
   int data;
   struct Node* next;
   Node(int data){
      this->data = data;
      next = NULL;
   }
};
struct LinkedList {
   Node* head;
   LinkedList(){
      head = NULL;
   }
   void interReverseLL(){
      Node* current = head;
      Node *prev = NULL, *after = NULL;
      while (current != NULL) {
         after = current->next;
         current->next = prev;
         prev = current;
         current = after;
      }
      head = prev;
   }
   void print() {
      struct Node* temp = head;
      while (temp != NULL) {
         printf("%d ", temp-> data);
         temp = temp->next;
      }
      printf("\n");
   }
   void push(int data){
      Node* temp = new Node(data);
      temp->next = head;
      head = temp;
   }
};
int main() {
   LinkedList linkedlist;
   linkedlist.push(85);
   linkedlist.push(10);
   linkedlist.push(65);
   linkedlist.push(32);
   linkedlist.push(9);
   printf("Linked List : \t");
   linkedlist.print();
   linkedlist.interReverseLL();
   printf("Reverse Linked List : \t");
   linkedlist.print();
   return 0;
}
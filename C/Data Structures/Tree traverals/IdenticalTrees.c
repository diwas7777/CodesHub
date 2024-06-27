#include <stdio.h>  
#include <stdlib.h>  
#include <stdbool.h>  
   
//Represent a node of binary tree  
struct node{  
    int data;  
    struct node *left;  
    struct node *right;  
};  
   
//Represent the root node of first binary tree  
struct node *rootTree1 = NULL;  
//Represent the root node of second binary tree  
struct node *rootTree2 = NULL;  
      
//createNode() will create a new node  
struct node* createNode(int data){  
    //Create a new node  
    struct node *newNode = (struct node*)malloc(sizeof(struct node));  
    //Assign data to newNode, set left and right children to NULL  
    newNode->data= data;  
    newNode->left = NULL;  
    newNode->right = NULL;  
      
    return newNode;  
}  
   
//areIdenticalTrees() finds whether two trees are identical or not  
bool areIdenticalTrees(struct node *root1, struct node *root2) {  
        
    //Checks if both the trees are empty  
    if(root1 == NULL && root2 == NULL)  
          return true;  
      
    //Trees are not identical if root of only one tree is null thus, return false  
    if(root1 == NULL && root2 == NULL)  
          return true;  
      
    //If both trees are not empty, check whether the data of the nodes is equal  
    //Repeat the steps for left subtree and right subtree  
    if(root1 != NULL  && root2 != NULL) {  
            
          return ((root1->data == root2->data) &&  
                  (areIdenticalTrees(root1->left, root2->left)) &&  
                  (areIdenticalTrees(root1->right, root2->right)));  
    }  
    return false;  
}  
        
   
int main()  
{  
    //Adding nodes to the first binary tree  
    rootTree1 = createNode(1);  
    rootTree1->left = createNode(2);  
    rootTree1->right = createNode(3);  
    rootTree1->left->left = createNode(4);  
    rootTree1->right->left = createNode(5);  
    rootTree1->right->right = createNode(6);  
      
    //Adding nodes to the second binary tree  
    rootTree2 = createNode(1);  
    rootTree2->left = createNode(2);  
    rootTree2->right = createNode(3);  
    rootTree2->left->left = createNode(4);  
    rootTree2->right->left = createNode(5);  
    rootTree2->right->right = createNode(6);    
      
    //Displays whether both the trees are identical or not  
    if(areIdenticalTrees(rootTree1, rootTree2))  
        printf("Both the binary trees are identical");  
    else  
        printf("Both the binary trees are not identical");  
   
    return 0;  
}  
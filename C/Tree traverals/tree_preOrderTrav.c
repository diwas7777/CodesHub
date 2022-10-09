#include <stdio.h> 
#include <stdlib.h>

struct treeNode
{
    int data ;
    struct treeNode * left ;
    struct treeNode *right ;
} ;

struct treeNode  * createNode(int val)
{
    struct treeNode * node = (struct treeNode *) malloc(sizeof(struct treeNode)) ;

    node->data = val ;
    node->left = NULL ;
    node->right = NULL ;
}

void preOrderTraversal(struct treeNode * root) // Root     left subtree       Right Subtree
{
    if(root)
    {
        printf("%d " , root->data) ;
        preOrderTraversal(root->left) ;
        preOrderTraversal(root->right) ;
    }

}

signed main()
{
    /* Binary Tree is a tree with each node having atmost 2 children .

         7
      23   6
    9        8
    
    */
    struct treeNode * root = createNode(7) ;
    struct treeNode *n1 = createNode(23) ;
    struct treeNode *n2 = createNode(6) ;
    struct treeNode *n3 = createNode(9) ;
    struct treeNode *n4 = createNode(8) ;

    root->left = n1 ;
    root->right = n2 ;

    n1->left = n3 ;
    

    n2->right = n4 ;

    
    preOrderTraversal(root) ;

  
    return 0 ;
}
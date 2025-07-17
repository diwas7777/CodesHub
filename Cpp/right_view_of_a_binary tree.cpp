   and a pointer to right child 
struct Node
{
    int data;
    struct Node* left;
    struct Node* right;
    
    Node(int x){
        data = x;
        left = right = NULL;
    }
}; */

// Should return  right view of tree
class Solution
{
    public:
    //Function to return list containing elements of right view of binary tree.
    vector<int> rightView(Node *root)
    {
       // Your Code here
        vector<int>v;
   if(!root)return v;
   queue<Node*>q;
   q.push(root);
   while(!q.empty()){
    //   v.push_back(q.front()->data);
       int sz=q.size();
       while(sz--){
           Node*t=q.front();
           q.pop();
           if(t->left)q.push(t->left);
            if(t->right)q.push(t->right);
            if(sz==0)v.push_back(t->data);
       }
   }
   return v;
    }
};


#include<iostream>
#include<list>  //<forward_list> header is used for singly list
using namespace std;

class Queue{
    int curr_size;
    list<int> l;

   public:
        Queue(){
            curr_size=0;
        } 
        bool isempty(){
            return curr_size==0;
        }
        void push(int data){
            l.push_back(data);
            curr_size++;
        }
        void pop(){
            if (!isempty()){
                curr_size--;
                l.pop_front();
            }
        }
        int front(){
            return l.front();
        }
};

int main(){
    Queue q;
    for (int i=1; i<=10;i++){
        q.push(i);
    }
    while(!q.isempty()){
        cout<<q.front()<<" ";
        q.pop();
    }

}

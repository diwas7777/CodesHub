# include <bits/stdc++.h>
using namespace std;


class Node{

	public:
	int data;
	Node* next;

	Node(int data){
		this->data = data ;
		next = NULL;
	}

};

Node* remove(Node* head){
	if(head==NULL || head->next ==NULL){
		return head;
	}

	head->next = remove(head->next);

	if(head->data >= head->next->data){
		return head;
	}else{
		return head->next;
	}
}



int main(){

	int n;
	cin>>n;

	Node*head = NULL;
	Node*tail = NULL;

	for(int i = 0 ; i < n ; i++){
		int dt;
		cin>>dt;

		Node* newnode = new Node(dt);

		if(head==NULL && tail==NULL){
			head=newnode;
			tail=newnode;
		}else{
			tail->next = newnode;
			tail = tail->next;
		}
	}


	head = remove(head);


	Node* temp = head;
	while(temp){
		cout<<temp->data<<" ";
		temp = temp ->next;
	}
	
	return 0;
}

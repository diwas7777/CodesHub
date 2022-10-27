from asyncio.windows_events import NULL


class Node(object):
    def __init__(self, x):
        self.data = x
        self.NextNode = None


class LinkedList(object):
    def __init__(self):
        self.Hnode = None

    def Insert(self, x):
        NewNode = Node(x)
        if(self.Hnode is not None):
            NewNode.NextNode = self.Hnode
            self.Hnode = NewNode
        else:
            self.Hnode = NewNode

    def Delete(self):
        tnode = self.Hnode
        if(tnode is not None):
            self.Hnode = self.Hnode.NextNode
            x = tnode.data
            del tnode
            return x

    def PrintList(self):
        tnode = self.Hnode
        while(tnode is not None):
            print(tnode.data, end=" ")
            tnode = tnode.NextNode


class stack():
    def __init__(self):
        self.top = -1
        self.l = LinkedList()

    def push(self, val):
        self.top += 1
        self.l.Insert(val)

    def pop(self):
        if(self.top >= 0):
            print(self.l.Delete(), "is the Popped element.")
            self.top -= 1
        else:
            print("Stack is empty.")

    def peek(self):
        if(self.top >= 0):
            print(self.l.Hnode.data, "is the top element.")
        else:
            print("Stack is empty.")

    def print(self):
        if(self.top >= 0):
            print("Stack:", end=" ")
            self.l.PrintList()
            print()
        else:
            print("Stack is empty.")


stac = stack()
while(1):
    print("1.Push \n2.Pop \n3.Peek \n4.Print \n5.Exit \nEnter your choice: ")
    choice = int(input())
    if(choice == 1):
        print("Enter the element: ")
        stac.push(int(input()))
    elif(choice == 2):
        stac.pop()
    elif(choice == 3):
        stac.peek()
    elif(choice == 4):
        stac.print()
    elif(choice == 5):
        break
    else:
        print("Invalid Input\n")

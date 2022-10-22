# Python program to get intersection
# point of two linked list
class Node :
	def __init__(self, d):
		self.data = d;
		self.next = None;

# Function to print the list
def Print(n):
	cur = n;
	while (cur != None) :
		print(cur.data, end=" ");
		cur = cur.next;
	print("");

# Function to find the intersection of two node
def MegeNode(n1, n2):
	
	# Define hashset
	hs = set();

	while (n1 != None):
		hs.add(n1);
		n1 = n1.next;
	while (n2 != None):
		if (n2 in hs):
			return n2;
		n2 = n2.next;
	
	return None;


# Driver code

# list 1
n1 = Node(1);
n1.next = Node(2);
n1.next.next = Node(3);
n1.next.next.next = Node(4);
n1.next.next.next.next = Node(5);
n1.next.next.next.next.next = Node(6);
n1.next.next.next.next.next.next = Node(7);

# list 2
n2 = Node(10);
n2.next = Node(9);
n2.next.next = Node(8);
n2.next.next.next = n1.next.next.next;

Print(n1);
Print(n2);

print(MegeNode(n1, n2).data);

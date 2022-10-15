/*
** Handling of collision via open addressing
** Method for Probing: Double Hashing
*/

#include <iostream>
#include <vector>
#include <bitset>
using namespace std;
#define MAX_SIZE 10000001ll

class doubleHash {

	int TABLE_SIZE, keysPresent, PRIME;
	vector<int> hashTable;
	bitset<MAX_SIZE> isPrime;

	/* Function to set sieve of Eratosthenes. */
	void __setSieve(){
		isPrime[0] = isPrime[1] = 1;
		for(long long i = 2; i*i <= MAX_SIZE; i++)
			if(isPrime[i] == 0)
				for(long long j = i*i; j <= MAX_SIZE; j += i)
					isPrime[j] = 1;

	}

	int inline hash1(int value){
		return value%TABLE_SIZE;
	}
	
	int inline hash2(int value){	
		return PRIME - (value%PRIME);
	}

	bool inline isFull(){
		return (TABLE_SIZE == keysPresent);
	}

	public:

	doubleHash(int n){
		__setSieve();
		TABLE_SIZE = n;

		/* Find the largest prime number smaller than hash table's size. */
		PRIME = TABLE_SIZE - 1;
		while(isPrime[PRIME] == 1)
			PRIME--;

		keysPresent = 0;

		/* Fill the hash table with -1 (empty entries). */
		for(int i = 0; i < TABLE_SIZE; i++)
			hashTable.push_back(-1);
	}

	void __printPrime(long long n){
		for(long long i = 0; i <= n; i++)
			if(isPrime[i] == 0)
				cout<<i<<", ";
		cout<<endl;
	}

	/* Function to insert value in hash table */
	void insert(int value){

		if(value == -1 || value == -2){
			cout<<("ERROR : -1 and -2 can't be inserted in the table\n");
		}

		if(isFull()){
			cout<<("ERROR : Hash Table Full\n");
			return;
		}
		
		int probe = hash1(value), offset = hash2(value); // in linear probing offset = 1;
		
		while(hashTable[probe] != -1){
			if(-2 == hashTable[probe])				
				break;								 // insert at deleted element's location
			probe = (probe+offset) % TABLE_SIZE;
		}

		hashTable[probe] = value;
		keysPresent += 1;
	}

	void erase(int value){
		/* Return if element is not present */
		if(!search(value))
			return;	
		
		int probe = hash1(value), offset = hash2(value);

		while(hashTable[probe] != -1)
			if(hashTable[probe] == value){
				hashTable[probe] = -2;		 // mark element as deleted (rather than unvisited(-1)).
				keysPresent--;
				return;
			}
			else
				probe = (probe + offset) % TABLE_SIZE;

	}

	bool search(int value){
		int probe = hash1(value), offset = hash2(value), initialPos = probe;
		bool firstItr = true;

		while(1){
			if(hashTable[probe] == -1)				 // Stop search if -1 is encountered.
				break;
			else if(hashTable[probe] == value)		 // Stop search after finding the element.
				return true;
			else if(probe == initialPos && !firstItr) // Stop search if one complete traversal of hash table is completed.
				return false;
			else
				probe = ((probe + offset) % TABLE_SIZE); // if none of the above cases occur then update the index and check at it.

			firstItr = false;
		}
		return false;
	}

	/* Function to display the hash table. */
	void print(){
		for(int i = 0; i < TABLE_SIZE; i++)
			cout<<hashTable[i]<<", ";
		cout<<"\n";
	}

};

int main(){
	doubleHash myHash(13); // creates an empty hash table of size 13

	/* Inserts random element in the hash table */
	
	int insertions[] = {115, 12, 87, 66, 123},
		n1 = sizeof(insertions)/sizeof(insertions[0]);
	
	for(int i = 0; i < n1; i++)
		myHash.insert(insertions[i]);
	
	cout<< "Status of hash table after initial insertions : "; myHash.print();
	

	/*
	** Searches for random element in the hash table,
	** and prints them if found.
	*/
	
	int queries[] = {1, 12, 2, 3, 69, 88, 115},
		n2 = sizeof(queries)/sizeof(queries[0]);
	
	cout<<"\n"<<"Search operation after insertion : \n";

	for(int i = 0; i < n2; i++)
		if(myHash.search(queries[i]))
			cout<<queries[i]<<" present\n";
	

	/* Deletes random element from the hash table. */
	
	int deletions[] = {123, 87, 66},
		n3 = sizeof(deletions)/sizeof(deletions[0]);
	
	for(int i = 0; i < n3; i++)
		myHash.erase(deletions[i]);

	cout<< "Status of hash table after deleting elements : "; myHash.print();
	
	return 0;
}

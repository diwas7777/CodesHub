//Input:  
//Enter 1st Binary: 1111
//Enter 2nd Binary: 1111
//Output: 
//Sum of Binary is 11110

//----Star code
#include <math.h>
#include <iostream>
using namespace std;

// create a class
class Binary {
  // private data members
 private:
  int binary_1, binary_2;

  // public member functions
 public:
  // putBinary() function to 
  // insert binary numbers
  void putBinary() {
    cout << "Enter 1st Binary: ";
    cin >> binary_1;

    cout << "Enter 2nd Binary: ";
    cin >> binary_2;
  }

  // sumBinary() function to 
  // add two binary numbers
  void sumBinary() {
    // initializing int type variables 
    // to perform operations
    int index_1 = 0, index_2 = 0, sum[30];

    // while loop to add two binary numbers
    while (binary_1 != 0 || binary_2 != 0) {
      // adding last digits of both 
      // binary numbers and index_2
      sum[index_1++] = (int)((binary_1 % 10 + binary_2 % 10 + index_2) % 2);

      // adding last digits of both binary numbers and
      // index_2 in index_2 after divided by 2
      index_2 = (int)((binary_1 % 10 + binary_2 % 10 + index_2) / 2);

      // discarding last digit by dividing it by 10
      binary_1 = binary_1 / 10;
      binary_2 = binary_2 / 10;
    }

    // if condition to check if the index_2 
    // is empty or not
    if (index_2 != 0) {
      // if it is non zero then it it is placed at
      // the next place in the array
      sum[index_1++] = index_2;
    }

    cout << "Sum of Binary is ";

    // for loop to print the resulting binary number
    for (index_1 = index_1 - 1; index_1 >= 0; index_1--) {
      cout << sum[index_1];
    }
  }
};

int main() {
  // create object
  Binary B;

  // calling putBinary() function to 
  // insert binary numbers
  B.putBinary();

  // calling sumBinary() function to 
  // add binary numbers
  B.sumBinary();

  return 0;
}

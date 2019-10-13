#include <iostream>
#include <cmath>
using namespace std;
int octalToDecimal(int octalNumber);
int main()
{
   int octalNumber;
   cout << "Enter an octal number: ";
   cin >> octalNumber;
   cout << octalNumber << " in octal = " << octalToDecimal(octalNumber) << " in decimal";
   
   return 0;  /* Multiple line 
                  comment 1 */
}
// Function to convert octal number to decimal
int octalToDecimal(int octalNumber)   // Single Line Comment 2
{
    int decimalNumber = 0, i = 0, rem;
    while (octalNumber != 0)
    {
    // Single Line Comment 3
        rem = octalNumber % 10;
        octalNumber /= 10;
        decimalNumber += rem * pow(8, i); // Single Line Comment 4
        ++i;
    }
    return decimalNumber; // Single Line Comment 5
}

/* Multiple line comment 2 */

/* Multiple line 
  comment 3 */

  
  
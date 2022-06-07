
#include <iostream>
using namespace std;


int main()
{
    string name;
    string ID;

    cout << "What is your name?" << endl;
    cin >> name;
    cout << "Hello " << name << " !" << endl;
    cout << "What's your student ID?" << endl;
    cin >> ID;
    cout << "Your ID is " << ID << endl;

int number1,number2,sum,diff,prod;

cout << "Enter a number." << endl;
cin >> number1;
cout << "Enter another number." << endl;
cin >> number2;
sum = number1 + number2;
diff = number1 - number2;
prod = number1 * number2;
cout << "Summation of the numbers is " << sum << endl << "Difference of the numbers is " << diff << endl<<
"Product of the numbers is " << prod << endl;


    for(int i = 1; i <= 3; i++){
        for(int j = 1; j <= i; j++)
        {
            cout << "* ";
        }
        cout << "\n";
    }
    return 0;
}
#include <iostream>
#include <string>

using namespace std;

int ReadNumber() {
	int firstN; 
	int secondN;
	cout << "Please enter a number: ";
	cin >> firstN;
	cout << "Please enter second number: ";
	cin >> secondN;
	return firstN + secondN;

}
int WriteNumber(int result) {
	cout << "Adding those numbers resulted in " << result << endl;
}
int main() {
	int final = ReadNumber();
	WriteNumber(final);
	// return 0;
}
#include <iostream>
using namespace std;

void revstring(char str[]) {
    int length = 0;
    while (str[length] != '\0') {
        length++;
    }
    for (int i = 0; i < length / 2; i++) {
        char temp = str[i];
        str[i] = str[length - i - 1];
        str[length - i - 1] = temp;
    }
}

int main() {
    const int maxStringLength = 100; // Define a maximum string length
    char str[maxStringLength];

    cout << "Enter String to reverse: ";
    cin >> str;

    revstring(str);
    cout << "Reversed String: " << str << endl;

    return 0;
}

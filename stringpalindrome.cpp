#include <iostream>
using namespace std;
void palindrome(char str[]){

    int length=0;
    while (str[length]!='\0')
    {
        length++;
    }
    
    for(int i=0;i<length/2;i++){
        if(str[i]==str[length-1-i]){
            continue;
        }else{
            cout<<"its not palindrome";
            return;
        }
    }
        cout<<"its palindrome";

}
int main(){
    char str[100];
    cout<<"input string::";
    cin>>str;
    palindrome(str);
    return 0;
}
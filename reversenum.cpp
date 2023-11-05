#include<iostream>
using namespace std;
int rev(int n){
    int temp=n;
    int reverse=0;
    while ((n!=0))
    {
        temp=n%10;

        reverse=reverse*10+temp;
        n=n/10;
    }
    return reverse;
    
}
int main()

{
    int num=1234;
    int ans=rev(num);
    cout<< ans;
    return 0;
}

#include<iostream>
using namespace std;
int gcd(int a,int b){
    if(a==0){
        return b;
    }else if(b==0){
        return a;
    }else if(a==b){
        return a;
    }else if(a>b){
        return(gcd(a-b,b));
    }else if(a<b){
        return(gcd(a,b-a));
    }
    return 0;
}
int main(){
    int a=3;
    int b=20;
    cout<<"gcd of "<<a<<" and "<<b<<" is "<<gcd(a,b);
    return 0;
}
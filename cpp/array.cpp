#include<iostream>
using namespace std;
int main(){
    int k;
    int l;
    cout<<"enter the length";
    cin>> l;
    int a[l];
    for(int i=0;i<l;i++){
        cin<<a[i]
    }
    cout<<"enetr k:";
    for(int i=0;i<l;i++){
        if(a[i]==k){
            cout<<i;
            break;
        }
    }
    return 0;
}

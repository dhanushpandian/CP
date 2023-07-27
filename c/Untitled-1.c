#include<stdio.h>

void print(int arr[],int n){
    for(int i=0;i<n;i++){
        printf("%d\n",arr[i]);
    }
}
void insertsort(int arr[],int n){
    int i,key,j;
    for(i=1;i<n;i++){
        key=arr[i];
        j=i-1;
    while(j>=0&&arr[j]>key){
     arr[j+1]=arr[j];
     j=j-1;
     }
     arr[j+1]=key;
  }
print(arr,n);
}


int main()
{
    int arr[]={10,12,3,11,44};
    int n=sizeof(arr)/sizeof(arr[0]);
    print(arr,n);
    printf("\n\n");
    insertsort(arr,n);
    return 0;
}
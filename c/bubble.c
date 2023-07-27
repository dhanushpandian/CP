#include<stdio.h>

int main(){
    int arr[]={54,23,12,5,63,2};
    int l=sizeof(arr)/sizeof(arr[0]);
      for(int i =0;i<l;i++){
        printf("%d",arr[i]);
        printf(" ");
    }
    for(int i=0;i<l;i++){
        for(int j=0;j<l-1-i;j++){
                if(arr[j]>arr[j+1]){
                    int temp=arr[j];
                    arr[j]=arr[j+1];
                    arr[j+1]=temp;
                }
        }
    }
    printf("\n sorted:");
      for(int i =0;i<l;i++){
        printf("%d",arr[i]);
        printf(" ");
    }
    return 0;
}
#include<stdio.h>
int main(){
	int n=3,min=-2,max=2;
	int a[]={-2,5,-1};
	int sum=0,count=0;
	for(int i=0;i<n;i++){
		for(int j;j<=n;j++){
			sum=sum+a[j];
			}			
		if(sum>=min&&sum<=max){
			count++;
		}
		sum=0;	
	}
	printf("%d",count);
	return 0;
}

#include<stdio.h>
int main(){
	int n=6;
	//printf("enter n:");
	//scanf("%d",n);
	long int a[n];
	a[0]=a[1]=a[2]=1;
	for(int i=3;i<=n;i++){
		a[i]=a[i+1]+a[i-3];
//	printf("%d",a[i]);
	}
	printf("%d",a[n]);
}

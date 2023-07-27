#include<stdio.h>
int func(int n){
	int count=0;
	if(n==1){
		count++;
	}
	else{
		count++;
		for(int i=1;i<=n;i++){
			count++;
			count++;
			break;
		}
		count++;
	}
	count++;
return count;
}
void main(){
	printf("%d",func(2));   
}

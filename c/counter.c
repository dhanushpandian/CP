#include<stdio.h>
int func(int n){
	int count=0;
	int i=1;
	count++;
	int s=1;
	count++;
	while(s<=n){
		count++;
		i++;
		s=s+i;
		count++;
	}
	count++;
	return count;
}
int main(){
	int n,c;
	scanf("%d",&n);
	c=func(n);
	printf("%d",c);
	return 0;
}

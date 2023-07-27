#include<stdio.h>
int min(int a, int b){
	if(a<b){
		return a;
	}
	else{
		return b;
	}
}
int euclid(int a, int b){
	int count=0;
	int r;
	while(b>0){
		count++;
		r=a%b;
		a=b;
		b=r;
	}
	printf("%d\n",a);
	return count;
}
int cic(int a,int b){
	int count=0;
	int t=min(a,b);
	while(a%t>0||b%t>0){
		count++;
		t--;
	}
	count++;
	printf("%d\n",t);
	return count;
}
int main(){
	printf("%d\n%d",euclid(10,6),cic(10,6));
	return 0;
}

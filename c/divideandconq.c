#include<stdio.h>
void find(int a[],int x,int l,int h)
{
	int mid=(l+h)/2;
	if(l<=h)
{
		if(a[mid]==x){
			printf("%d",mid);
		}
		else if(a[mid]<x){
			find(a,x,mid+1,h);
		}
		else{
			if (a[mid-1]>x){
				find(a,x,l,mid-1);
			}
			else{
				printf("%d",mid);
			}
		}
	}
	else{
		printf("-1");
	}
}
void main(){
	int a[]={3,5,7,9,11,13,15};
	int x=10;	
	int l=0;
	find(a,x,l,6);
}

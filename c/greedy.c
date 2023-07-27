 #include<stdio.h>
 #include<math.h>
 #include<stdlib.h>
 int main(){
 	int n=3;
	int a[]={1,2,3};

	int t;
	for(int i=0;i<n;i++){
	
	for(int j=0;j<n;j++){
	if(a[i]>a[j]){
		t=a[i];
		a[i]=a[j];
		a[j]=t;
	}		
	}
}
long int sum=0;
for(int i=0;i<n;i++){
	sum=sum+a[i]*pow(3,i);
}
printf("%ld",sum);
return 0;
}

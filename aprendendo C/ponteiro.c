#include <stdio.h>



int main(){

	int x;
	int *pont = &x;

	printf("x = %d\n", x);
	//printf("x = %d\n", &x);
	//printf("x = %d\n", pont);
	//printf("x = %d\n", &pont);
	printf("x = %d\n", *pont);



}
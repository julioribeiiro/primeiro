#include <stdio.h>

void muda(int *i){
	*i = 300;
}


int main(){
	int i = 10;
	muda(&i);
	printf("%d\n", i);

}



/*




*/

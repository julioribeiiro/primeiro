/*
Criar funcao swap que recebe um array de 5 inteiros
esta funcao transforma esse array de tras pra frente
*/


#include <stdio.h>

void swap(int *p){
	int aux;
	for(int i = 0; i<5; i++){
		aux = p[5-i];
		p[5-1] = p[i];
		p[i] = aux;
	}

}



int main(){

int ar[] = {1, 2, 3, 4, 5};

swap(ar);
for(int i=0; i<5; i++)
	printf("%d  ", ar[i]);

}
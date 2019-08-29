/*
Varrer a string salvando na primeira variavel
antes de passar para o outro caractere salvar num caractere auxiliar
*/

#include <stdio.h>
#include <string.h>

int main(){

	char string[10] = {'C','A','R','R','O'};
	int i;
	char a, b;

	for(i=0; i<5; i++){
		b = a;
		a = string[i];

		if (a == b){
			string[i] = ' ';
		}
	}

	printf("%s\n", string);

	printf("\n\n\n\n");
	return 0;
}
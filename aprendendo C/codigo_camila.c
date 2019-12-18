/*

argc = quantidade de argumentos

argv = "nome_do_programa", "argumento_1", "argumento_2"

*/


#include <stdio.h>
#include <string.h>
#include <stdlib.h>


void anagrama(char *palavra_1, char *palavra_2, int len){

	int i;
	int j;
	int contador = 0;

	for(i = 0; i<len; i++){
		for(j = 0; j<len; j++){
			if(palavra_1[i] == palavra_2[j]){
				palavra_2[j] = '0';
				contador++;
				break;
			}


		}


	}

	if(contador == len){
		printf("1\n");
	}

	else{
		printf("0\n");
	}


}


int main(int argc, char *argv[]){

	int len_1;
	int len_2;



	if(argc == 1){
		printf("1\n");
		return 0;
	}


	len_1 = strlen(argv[1]);
	len_2 = strlen(argv[2]);


	if(len_1 != len_2){
		printf("0\n");
		return 0;
	}

	else{

	anagrama(argv[1],argv[2],len_1);

	}

}














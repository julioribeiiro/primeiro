/*
funcao que recebe duas strings
retorna 1 caso seja um anagrama
retorna 0 caso nao seja

exemplos:
cesar acers retorna 1
linguagem nmlguiea retorna 0

PASSO-A-PASSO

1- recebe as duas strings em cada variavel
2- roda a primeira string caracter a caracter
3- soma mais um na variavel tamanho da string
4- apos pegar um caracter da primeira string a segunda string eh rodada e procura um caracter similar
5- se for encontrado este caracter na segunda string o contador soma mais 1
6- o caracter da segunda string eh mudado para 1



*/
#include <stdlib.h>
#include <stdio.h>

void anagrama(char *palavra_1, char *palavra_2){
	int i=0, j=0, tamanho = 0, comparacao = 0;
	while(palavra_1[i] != '\0'){
		tamanho++;
		while(palavra_2[j] != '\0'){
			if (palavra_1[i] == palavra_2[j]){
				comparacao++;
				palavra_2[j] = '1';
				break;
			}
		j++;
		}
		j = 0;
		i++;

	}
	if (comparacao == tamanho)
		printf("1");
	else
		printf("0");



}


int main(int argc, char *argv[]){
	char *palavra_1, *palavra_2;
	if (argc == 1){
		printf("1");
		return 0;
	}

	else if (argc == 2){
		printf("0");
		return 0;
	}
	palavra_1 = argv[1];
	palavra_2 = argv[2];

	anagrama(palavra_1, palavra_2);

}

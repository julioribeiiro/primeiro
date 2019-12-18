
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <ctype.h>

int main(){
FILE *arquivo;
char c;

arquivo= fopen("usuarios.txt", "r+");


while(c != EOF){
	c = fgetc(arquivo);


	if (islower(c)){
		c = toupper(c);
		fseek(arquivo, -1, SEEK_CUR);
		fputc(c, arquivo);
	//	fseek(arquivo, 0, SEEK_CUR);
	}

}

}
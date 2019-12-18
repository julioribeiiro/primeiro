#include <stdio.h>
#include <stdlib.h>

//eh preciso um ponteiro de ponteiro de ponteiros para mudar o conteudo(endereco apontado)do meu ponteiro de ponteiros
void alocateMatrix(int linhas, int colunas, int ***matrix){
	int **aux;
	printf("parou aqui 00\n");
	aux = calloc(linhas, sizeof(int*));

	printf("%d\n", **matrix[0]);

	printf("parou aqui 22\n");
	for (int i = 0; i < linhas; i++){
		aux[i] = calloc(colunas, sizeof(int));
	}

	printf("parou aqui 11\n");
//usando so um * eu mudo o endereco apontado pelo meu ponteiro de ponteiros
	*matrix = aux;//<- aux eh o endereco de um ponteiro de ponteiros do tipo inteiro

/*
	printf("5:%d\n", *matrix[0][0]);
	printf("6:%d\n", *matrix[0][1]);
	printf("7:%d\n", *matrix[1][0]);
	printf("8:%d\n", *matrix[1][1]);
*/

}


void init(int tamanho, char **conteudo, int ***matrix){
	int contador = 3;
	int i=0, j=0;
	printf("1:%d\n", atoi(conteudo[3]));
	printf("2:%d\n", atoi(conteudo[4]));
	printf("3:%d\n", atoi(conteudo[5]));
	printf("4:%d\n", atoi(conteudo[6]));

	printf("5:%d\n", *matrix[0][0]);
	printf("6:%d\n", *matrix[0][1]);
	printf("7:%d\n", *matrix[1][0]);
	printf("8:%d\n", *matrix[1][1]);


	while(*matrix[i][j] != 0){
		while(*matrix[i][j] != 0){
			*matrix[i][j] = atoi(conteudo[contador]);
			printf("%d\n", *matrix[i][j]);
			j++;
			contador++;
		}
		i++;
		j=0;

	}


printf("3\n");
}




int main(int argc, char *argv[]){

	int linhas, colunas, argumentos;
	int **matrix;


	linhas = atoi(argv[1]);
	colunas = atoi(argv[2]);
	printf("Matriz: %dx%d\ntamanho: %d\n", linhas, colunas, argc);


		printf("\n\n\n");
		printf("123\n");
		alocateMatrix(linhas, colunas, &matrix);
		printf("456\n");
		//init(argc, argv, &matrix);
		printf("789\n");

/*
	for (int i = 0; i < linhas; i++)
		for (int j = 0; j < colunas; j++)
			printf("%d\n", matrix[i][j]);

*/
}
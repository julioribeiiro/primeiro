#include <stdlib.h>
#include <stdio.h>
#include <math.h>


void allocateMatrix(int linhas, int colunas, double ***espaco){
	double **aux;
	aux = calloc(linhas, sizeof(double*));

	for (int i = 0; i < linhas; i++)
		aux[i] = calloc(colunas, sizeof(double));

	*espaco = aux;

}


void init(int tamanho, char **conteudo, double ***espaco){
	int contador = 3;
	int linhas;
	tamanho = sqrt(tamanho - 3);


	for(int i=0; i<tamanho; i++){
		for(int j=0; j<tamanho; j++){
			espaco[0][i][j] = atoi(conteudo[contador]);
			contador++;
		}

}

}


int det(double ***espaco, int tamanho){
	tamanho = sqrt(tamanho - 3);
	double determinante = 0;
	int linha = 0, n, contador = 0;
	double multiplicador = 1, aux;


	if(tamanho == 2)
		determinante = espaco[0][0][0]*espaco[0][1][1] - espaco[0][0][1]*espaco[0][1][0];
	
	else if (tamanho == 3)
		determinante = espaco[0][0][0]*espaco[0][1][1]*espaco[0][2][2] + espaco[0][0][1]*espaco[0][1][2]*espaco[0][2][0] + espaco[0][0][2]*espaco[0][1][0]*espaco[0][2][1] - espaco[0][0][2]*espaco[0][1][1]*espaco[0][2][0] - espaco[0][0][0]*espaco[0][1][2]*espaco[0][2][1] - espaco[0][0][1]*espaco[0][1][0]*espaco[0][2][2];


	else{


		for(int k = 0; k<=tamanho-2; k++){

		//CASO O NUMERO A VIRAR 1 JA SEJA 0 UMA INVERSAO DE LINHAS ACONTECE
			if (espaco[0][k][k] == 0){
				multiplicador = -multiplicador;
				n=k;
				while(espaco[0][n][k] == 0){
					n++;
					if (n > tamanho - 1){//-----CASO DE DUAS COLUNAS EQUIVALENTES
						printf("0");
						return 1;
					}

				}
				for(int i=0; i<tamanho; i++){
					aux = espaco[0][n][i];
					espaco[0][n][i] = espaco[0][k][i];
					espaco[0][k][i] = aux;
				}
				k = 0;
			}


			//PRIMEIRO DEIXAMOS O PRIMEIRO ELEMENTO DA MATRIZ = 1;
			multiplicador = multiplicador * espaco[0][k][k];
			for(int i=tamanho-1; i>=k; i--)
				espaco[0][k][i] = espaco[0][k][i] * (1 / espaco[0][k][k]);


			//AGORA ZERAMOS A PRIMEIRA COLUNA DA MATRIZ;
			for(int i=tamanho-1; i>=k+1; i--)
				for(int j=tamanho-1; j>=0; j--)
					espaco[0][i][j] -= (espaco[0][k][j] * espaco[0][i][k]);

			//VERIFICA-SE SE ALGUMA LINHA DA MATRIZ FOI ZERADA
				for(int i=0; i<tamanho; i++){
					for(int j=0; j<tamanho; j++)
						if (espaco[0][i][j] == 0)
							contador++;

						if (contador == tamanho){//CASO DE DUAS LINHAS EQUIVALENTES
							printf("0");
							return 1;
				}
				contador = 0;
						}



}
	
	determinante = 1;
	for (int i=0; i<tamanho; i++)
		determinante *= espaco[0][i][i];
	determinante *= multiplicador;

	}


	printf("%lf", determinante);
	return 1;
}




int main(int argc, char *argv[]){
	double **matrix;
	int linhas, colunas;
	linhas = atoi(argv[1]);
	colunas = atoi(argv[2]);
	allocateMatrix(linhas, colunas, &matrix);
	init(argc, argv, &matrix);


	det(&matrix, argc);
    
    return 0;


}

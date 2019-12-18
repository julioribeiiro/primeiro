/*
0 - FALSE
1 - TRUE


[1,2,3]    [10,20,30,37,50]
[4,5,6]    [15,22]
[7,8,9]    [25]
           [35]
           [45]
           [55]

-Primeiro vemos o elemento [0][0] e o elemento [n][m] se o elemento estiver entre ele significa que ele pode existir
-Caso contrario, FALSE


-Segundo caso
---O numero esta entre o menor e o maior elemento

-Vejo o primeiro e ultimo elemento de cada linha
-caso o numero a ser buscado esteja dentro busco a linha
-se o numero for encontrado retorno true e termino o programa


*/


#include <stdio.h>
#include <stdlib.h>
#include <time.h>


int percorreMatrix(int **mat, int numero, int m, int n){
	for(int i=0; i<m; i++){
		if(numero >= mat[i][0] && numero <= mat[i][n-1]){//CASO ELEMENTO ESTEJA ENTRE PRIMEIRO ELEMENTO DA LINHA E ULTIMO ELEMENTO DA LINHA
			for(int j=0; j<n; j++){
				if (mat[i][j] == numero){
					return 1;
				}
			}

		} 
	}

	return 0;



}


int main(){
	int m = 3;
	int n = 3;
	int nBusca = 10; // DIGITE O NUMERO AQUI 
	int numero;
	int resultado = 0;
	clock_t tempo[2];

	int **mat = malloc(sizeof(int*)*m);
	for(int i=0; i<m; i++){
		mat[i] = malloc(sizeof(int)*n);

	}

	for(int i=0; i<m; i++){
		for(int j=0; j<n; j++){
			scanf("%d", &numero);
			mat[i][j] = numero;
		}
	}

	tempo[0] = clock();

	if (nBusca < mat[0][0] || nBusca > mat[m-1][n-1]){
		resultado = 0;
	}
	else
		resultado = percorreMatrix(mat, nBusca, m, n);

	
	tempo[1] = clock();

	double diferenca = (tempo[1] - tempo[0]) * 1000.0 / CLOCKS_PER_SEC;

	if (resultado == 1){
		printf("TRUE\n");
		printf("\nTempo gasto: %g\n", diferenca);
	}
	else{
		printf("FALSE\n");
		printf("\nTempo gasto: %g\n", diferenca);
	}









}
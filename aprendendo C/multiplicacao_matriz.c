#include <stdio.h>

int main(){
	int matriz_1[3][3];
	int matriz_2[3][3];
	int matriz_mult[3][3];
	int i, j, k;


//------INICIALIZANDO MATRIZ RESULTADO COMO 000------
	for(i=0; i <3; i++){
		for(j=0; j<3; j++){
			matriz_mult[i][j] = 0;
		}
	}

//---------RECEBENDO AS MATRIZES QUE SERAO MULTIPLIZACADAS-------------	

	printf("Digite a primeira matriz: \n");

	for(i=0; i<3; i++){
		for(j=0; j<3; j++){
			printf("Digite o elemento [%d][%d]: ", i, j);
			scanf("%d", &matriz_1[i][j]);
			printf("\n");
		}

	}

	printf("\nDigite a segunda matriz: \n");

	for(i=0; i<3; i++){
		for(j=0; j<3; j++){
			printf("Digite o elemento [%d][%d]: ", i, j);
			scanf("%d", &matriz_2[i][j]);
			printf("\n");
		}

	}


//--------PRINTANDO AS MATRIZES----------------

//--------PRIMEIRA MATRIZ-----------------------
	for(i=0; i<3; i++){
		for(j=0; j<3; j++){
			printf("%d 		", matriz_1[i][j]);
		}
		printf("\n");
	}

	
	printf("\n\n");

//-------SEGUNDA MATRIZ-------------------------
	for(i=0; i<3; i++){
		for(j=0; j<3; j++){
			printf("%d 		", matriz_2[i][j]);
		}
		printf("\n");
	}


//-----MULTIPLICANDO MATRIZES--------------
	for(k=0; k<3; k++){	
		for(i=0; i<3; i++){
			for(j=0; j<3; j++){
					matriz_mult[k][i] += matriz_1[k][j]*matriz_2[j][i];
				}
			}

		}

	printf("\n\nA matriz resultante eh: \n\n");

//-----PRINTANDO MATRIZ RESULTADO------
	for(i=0; i<3; i++){
		for(j=0; j<3; j++){
			printf("%d 		", matriz_mult[i][j]);
		}
		printf("\n");
	}



printf("\n\n\n");
return 0;
}







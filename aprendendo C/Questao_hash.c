
#include <stdio.h>

int main(){
	int N_repeticoes, i, u, k, C_quantidade, M_hash, chave, coluna = 0, contador=0;


	//PEGAMOS A INFORMACAO DE QUANTAS VEZES O PROCESSO SE REPETIRA
	scanf("%d", &N_repeticoes);

	//UM LOOP PARA REPETIR O PROCESSOR N VEZES
	for(i=0; i<N_repeticoes; i++){

		
		//PEGAMOS AS DUAS INFORMACOES NESSES INPUTS
		scanf("%d", &M_hash);
		scanf("%d", &C_quantidade);

		int resultado[M_hash][C_quantidade+1];

		for(u=0; u<M_hash; u++)
			resultado[u][0] = -1;

		//TEREMOS UMA QUANTIDADE DE INPUTS EQUIVALENTE AO NUMERO DE CHAVES
		for(u=0; u<C_quantidade; u++){
			scanf("%d", &chave);
			while (resultado[chave%M_hash][coluna] != -1)
				coluna++;
			resultado[chave%M_hash][coluna] = chave;
			resultado[chave%M_hash][coluna + 1] = -1;
			coluna = 0;
		}

		for(u=0; u<M_hash; u++){
			printf("%d -> ", u);		
			for(k=0; k<=C_quantidade; k++){
				if(resultado[u][k] != -1)
					printf("%d -> ", resultado[u][k]);
				else{
					printf("\\\n");
					break;
			}
		}
	}
	contador++;
	if (contador != N_repeticoes){
		printf("\n");
	}


	}

	return 0;

	}
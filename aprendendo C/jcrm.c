#include <stdio.h>


void tabela_hash(int M, int C, int chaves[]){
	int hash, f=0, j, k, u;
	int resultado[300][400];


	//PRIMEIRO ZERAMOS A MATRIZ RESULTADO INTEIRA
	for(j= 0; j<300; j++)
		for(k = 0; k < 400; k++)
			resultado[j][k] = -2;


	//A PARTIR DAQUI COMECAMOS A ARMAZENAR AS CHAVES NA FUNCAO HASH
	for (u=0; u<C; u++){
		hash = chaves[u]%M;
		while(resultado[hash][f] != -2)
			f++;
		resultado[hash][f] = chaves[u];
		f=0;
	}


	//APOS TERMINAR DE ARMAZENAR, PRINTAMOS A MATRIZ RESULTADO.
	for(u=0; u<M; u++){
		printf("%d -> ", u);		
		for(k=0; k<400; k++){
			if(resultado[u][k] != -2)
				printf("%d -> ", resultado[u][k]);
			else{
				printf("\\\n");
				break;
			}
		}
	}

	printf("\n");
}



int main(){
	int informacoes[300][400];
	int chaves[300][400];
	int N_repeticoes, M_tamanho, C_quantidade, hash, j, k, i, u;


	//PRIMEIRO ZERAMOS A MATRIZ CHAVES INTEIRA
	for(j= 0; j<300; j++)
		for(k = 0; k < 400; k++)
			chaves[j][k] = -2;


	//PEGAMOS A INFORMACAO DE QUANTAS VEZES O PROCESSO SE REPETIRA
	scanf("%d", &N_repeticoes);


	//UM LOOP PARA REPETIR O PROCESSOR N VEZES
	for(i=0; i<N_repeticoes; i++){
		
		//PEGAMOS AS DUAS INFORMACOES NESSES INPUTS
		scanf("%d", &M_tamanho);
		scanf("%d", &C_quantidade);
		informacoes[i][0] = M_tamanho;
		informacoes[i][1] = C_quantidade;

		//TEREMOS UMA QUANTIDADE DE INPUTS EQUIVALENTE AO NUMERO DE CHAVES
		for(u=0; u<C_quantidade; u++)
			scanf("%d", &chaves[i][u]);

	}

	for(i=0; i<N_repeticoes; i++){
		tabela_hash(informacoes[i][0], informacoes[i][1], chaves[i]);


	}

	return 0;

	}






















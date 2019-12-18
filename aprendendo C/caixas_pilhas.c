/*
A entrada é composta de vários casos de teste. A primeira linha de cada
caso de teste contém dois números inteiros N e P , indicando, respectivamente,
o número de caixas e o número de pilhas (1 ≤ P ≤ N ≤ 1.000). As caixas são
numeradas seqüencialmente de 1 a N.

Cada uma das P linhas seguintes descreve uma pilha. Cada linha 
contém um inteiro Qi, indicando quantas caixas há na pilha i, 
seguido de um espaço em branco, seguido de uma lista de Qi números, 
que são os identificadores das caixas. Os elementos da lista são 
separados por um espaço em branco.

Todas as pilhas contêm pelo menos uma caixa, e todas as caixas 
aparecem exatamente uma vez na entrada. As caixas em cada pilha 
são listadas em ordem, da base até o topo da pilha. Todas as 
caixas têm o mesmo formato.

O final da entrada é indicado por N = P = 0.

A entrada deve ser lida da entrada padrão.

Entrada:
4 3
1 3
2 1 2
1 4
4 3
1 3
2 2 1
1 4
0 0

Saída:
2
0
*/
#include <stdio.h>
#include <stdlib.h>

int main(){

	int caixas = 1;
	int pilhas = 1;
	int *fila;
	int i, j;
	int qual_caixa = 0;
	int altura_caixa_1;
	int fila_caixa_1;
	int caixas_esquerda = 0;
	int caixas_direita = 0;
	int n_caixas;



	scanf("%d", &caixas);
	scanf("%d", &pilhas);

	while(caixas != 0 || pilhas != 0){

		fila = malloc(pilhas*sizeof(int));

		for(i=0; i<pilhas; i++){
			scanf("%d", &n_caixas);
			for(j=0; j<n_caixas; j++){
				fila[i] = n_caixas;
				scanf("%d", &qual_caixa);
				if (qual_caixa == 1){
					altura_caixa_1 = j + 1;
					fila_caixa_1 = i;
				}
			}
		}


		caixas_esquerda = fila[fila_caixa_1] - altura_caixa_1;
		for(i=fila_caixa_1-1; i>=0; i--){
			if (fila[i] >= altura_caixa_1)
				caixas_esquerda += fila[i] - altura_caixa_1 + 1;
			else
				break;

		}

		caixas_direita = fila[fila_caixa_1] - altura_caixa_1;

		for(i=fila_caixa_1-1; i<pilhas; i++){
			if(fila[i] >= altura_caixa_1)
				caixas_direita += fila[i] - altura_caixa_1 + 1;
			else
				break;

		}

		if (caixas_direita > caixas_esquerda){
			printf("%d\n", caixas_esquerda);
		}
		else{
			printf("%d\n", caixas_direita);
		}


		free(fila);

		scanf("%d", &caixas);
		scanf("%d", &pilhas);

	}

	return 0;
}
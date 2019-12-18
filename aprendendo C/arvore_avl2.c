/*

			100
		74		152
	21
		33


			100
		33		152
	21		74	

42
1 100
1 74
2 100
2 70
1 152
1 21
1 33
2 100
2 21
2 1
1 32
1 89
1 290
1 23
1 78
2 21
1 190
2 100
1 90
2 33
2 23
1 111
1 71
2 100
2 70
1 187
1 213
1 333
2 100
2 21
2 1
1 32
1 80
1 250
1 237
1 789
2 21
1 191
2 12
1 900
2 33
2 23




saida:
2
Data tidak ada
4
1
Data tidak ada
1
8
4
2
7
Data tidak ada
7
1
Data tidak ada
1
Data tidak ada
5
2







2
Data tidak ada
4
1
Data tidak ada
1
8
4
2
10
Data tidak ada
10
1
Data tidak ada
1
Data tidak ada
5
2

*/


#include <stdio.h>
#include <stdlib.h>

typedef struct folha{
	int info;
	struct folha *esquerda;
	struct folha *direita;
	int filhos_esquerda;
	int filhos_direita;
}folha;

void insere_folha(folha **raiz, int numero){
	if (*raiz == NULL){
		(*raiz) = malloc(sizeof(folha));
		(*raiz)->info = numero;
		(*raiz)->esquerda = NULL;
		(*raiz)->direita = NULL;
		(*raiz)->filhos_esquerda = 0;
		(*raiz)->filhos_direita = 0;
	}
	else if (numero > (*raiz)->info){
		(*raiz)->filhos_direita++;
		insere_folha(&(*raiz)->direita, numero);
	}

	else{
		(*raiz)->filhos_esquerda++;
		insere_folha(&(*raiz)->esquerda, numero);
	}

	}


void busca_arvore(folha *raiz, int numero){
	folha *aux;
	aux = raiz;
	int indice = 1;
	while(aux != NULL){
		if (numero < aux->info){
			aux = aux->esquerda;
		}
		else if (numero == aux->info){
			indice += aux->filhos_esquerda;
			break;
		}

		else{
			indice += aux->filhos_esquerda + 1;
			aux = aux->direita;
		}
	}
	if (aux == NULL)
		printf("Data tidak ada\n");
	else
		printf("%d\n", indice);

}

int main(void){
	int numero, quantidade, tipo;
	folha *raiz = NULL;

	scanf("%d", &quantidade);

	for(int i=0; i<quantidade; i++){
		scanf("%d", &tipo);
		scanf("%d", &numero);
		if (tipo == 1)
			insere_folha(&raiz, numero);
		else if (tipo == 2){
			busca_arvore(raiz, numero);
		}
	}
	return 0;
}
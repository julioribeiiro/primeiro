#include <stdio.h>
#include <stdlib.h>

typedef struct nodo{
	int info;
	struct nodo *esquerda;
	struct nodo *direita;
	int altura;
	int filhos_esquerda;
	int filhos_direita;

}folha;

//----------FUNCOES DE ALTURA--------------------
int altura(folha *raiz){
	if (raiz == NULL)
		return 0;
	else
		return raiz->altura;
}

void atualiza_altura(folha *raiz){
	if (raiz != NULL){
		if (altura(raiz->direita) > altura(raiz->esquerda))
			raiz->altura = altura(raiz->direita) + 1;
		else
			raiz->altura = altura(raiz->esquerda) + 1;
	}

}
//---------FIM FUNCOES DE ALTURA-----------------

//--------ROTACAO SIMPLES PARA A DIREITA-----------

void rot_direita(folha **raiz){
	folha *aux;
	aux = malloc(sizeof(folha));
	aux = (*raiz)->esquerda;
	(*raiz)->esquerda = aux->direita;
	aux->direita = *raiz;
	(*raiz)->filhos_esquerda = aux->filhos_direita;
	aux->filhos_direita = (*raiz)->filhos_direita + (*raiz)->filhos_esquerda + 1;
	atualiza_altura((*raiz)->direita);
	atualiza_altura(*raiz);
	*raiz = aux;
}

//-------ROTACAO SIMPLES PARA A ESQUERDA-------------
void rot_esquerda(folha **raiz){
	folha *aux;
	aux = malloc(sizeof(folha));
	aux = (*raiz)->direita;
	(*raiz)->direita = aux->esquerda;
	aux->esquerda = (*raiz);
	(*raiz)->filhos_direita = aux->filhos_esquerda;
	aux->filhos_esquerda = (*raiz)->filhos_direita + (*raiz)->filhos_esquerda + 1;
	atualiza_altura((*raiz)->esquerda);
	atualiza_altura(*raiz);
	*raiz = aux;
}


void insere_elemento(int numero, folha **raiz){
	if (*raiz == NULL){
		(*raiz) = malloc(sizeof(folha));
		(*raiz)->esquerda = NULL;
		(*raiz)->direita = NULL;
		(*raiz)->altura = 1;
		(*raiz)->info = numero;
		(*raiz)->filhos_direita = 0;
		(*raiz)->filhos_esquerda = 0;

	}

	else if (numero < (*raiz)->info){
		(*raiz)->filhos_esquerda++;
		insere_elemento(numero, &(*raiz)->esquerda);
		if (altura((*raiz)->esquerda) - altura((*raiz)->direita) == 2){
			if (numero < (*raiz)->esquerda->info)
				rot_direita(raiz);
			else{
				rot_esquerda(&(*raiz)->esquerda);
				rot_direita(raiz);
			}
		}
	}
	else{
		(*raiz)->filhos_direita++;
		insere_elemento(numero, &(*raiz)->direita);
		if (altura((*raiz)->direita) - altura((*raiz)->esquerda) == 2){
			if (numero > (*raiz)->direita->info)
				rot_esquerda(raiz);
			else{
				rot_direita(&(*raiz)->direita);
				rot_esquerda(raiz);
			}
		}

	}
	atualiza_altura(*raiz);

}


void percorre_in(folha *raiz, int numero){
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
	int quantidade, operacao, numero, i;
	folha *raiz = NULL;


	scanf("%d", &quantidade);
	for(i=0; i<quantidade; i++){
		scanf("%d", &operacao);
		scanf("%d", &numero);	
		if (operacao == 1)
			insere_elemento(numero, &raiz);
		
		else if (operacao == 2){
			percorre_in(raiz, numero);
		}

	}

	return 0;
}

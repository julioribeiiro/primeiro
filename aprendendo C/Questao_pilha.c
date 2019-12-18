#include <stdio.h>
#include <stdlib.h>
#include <string.h>

typedef struct elementos{
	
	struct elementos *proximo;
	int informacao;

}elemento;


typedef struct pilha{
	elemento *inicio;
	int tamanho;

}pilha;

void imprimir(pilha *pilha){
	elemento *navegador;
	navegador = pilha->inicio;
	while(navegador != NULL){
		if (navegador->proximo == NULL)
			printf("%d", navegador->informacao);
		else
			printf("%d ", navegador->informacao);
		navegador = navegador->proximo;

	}
}



void empilhar(pilha *pilha, int conteudo){
	elemento *novo;
	novo = malloc(sizeof(elemento));
	novo->informacao = conteudo;

	if (pilha->tamanho == 0){
		pilha->tamanho++;
		pilha->inicio = novo;
		novo->proximo = NULL;
	}
	else{
		pilha->tamanho++;
		novo->proximo = pilha->inicio;
		pilha->inicio = novo;
	}


}

void desempilhar(pilha *pilha){
	pilha->inicio = pilha->inicio->proximo;
	pilha->tamanho--;

}


int main(int argc, char const *argv[])

{
	char palavra[12];
	int numero;

	pilha *minha_pilha;

	minha_pilha = malloc(sizeof(pilha));
	minha_pilha->tamanho = 0;
	minha_pilha->inicio = NULL;


	do{
		scanf("%s", palavra);



		if (strcmp(palavra, "Empilhar") == 0){
			scanf("%d", &numero);
			empilhar(minha_pilha, numero);
		}

		else if(strcmp(palavra, "Imprimir") == 0){
			imprimir(minha_pilha);
			printf("\n");
		}

		else if(strcmp(palavra, "Desempilhar") == 0){
			desempilhar(minha_pilha);
		}


	}while(strcmp(palavra, "Finalizar") != 0);



	return 0;
}
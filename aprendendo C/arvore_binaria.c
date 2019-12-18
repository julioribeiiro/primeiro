#include <stdio.h>
#include <stdlib.h>

typedef struct node
{
	struct node *esquerda;
	struct node *direita;
	int dado;

}node;./

node *nova_folha(int numero){
	node *folha = malloc(sizeof(node));
	folha->esquerda = NULL;
	folha->direita = NULL;
	folha->dado = numero;
	return folha;
}

node *cria_arvore(node *raiz, int numero){
	if (raiz == NULL){
		raiz = nova_folha(numero);
		return raiz;
	}
	
	else if (numero <= raiz->dado)
		raiz->esquerda = cria_arvore(raiz->esquerda, numero);

	else if (numero > raiz->dado)
		raiz->direita = cria_arvore(raiz->direita, numero);

	return raiz;
}

void imprime_pre(node *raiz){
	if (raiz != NULL){
		printf(" %d", raiz->dado);
		imprime_pre(raiz->esquerda);
		imprime_pre(raiz->direita);
	}

}

void imprime_in(node *raiz){
	if (raiz != NULL){
		imprime_in(raiz->esquerda);
		printf(" %d", raiz->dado);
		imprime_in(raiz->direita);
	}
}

void imprime_pos(node *raiz){
	if (raiz != NULL){
		imprime_pos(raiz->esquerda);
		imprime_pos(raiz->direita);
		printf(" %d", raiz->dado);
	}

}


int main(){
	node *raiz;
	int casos;
	int qtd_nodes;
	int numero;

//REPETINDO FUNCAO A QUANTIDADE DE VEZES PEDIDAS
	scanf("%d", &casos);
	for(int i=0; i<casos; i++){
		raiz = NULL;
	//CRIANDO ARVORE COM OS NUMEROS DADOS
		scanf("%d", &qtd_nodes);
		for(int j=0; j<qtd_nodes; j++){
			scanf("%d", &numero);
			raiz = cria_arvore(raiz, numero);
		}
//----DEPOIS DE CRIAR A ARVORE, DEVEMOS IMPRIMIR.
	printf("Case %d:\nPre.:", i+1);
	imprime_pre(raiz);
	printf("\nIn..:");
	imprime_in(raiz);
	printf("\nPost:");
	imprime_pos(raiz);
	printf("\n\n");

	free(raiz);


	}


}
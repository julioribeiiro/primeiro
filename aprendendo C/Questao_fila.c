#include <stdio.h>
#include <stdlib.h>

typedef struct pessoas{
	struct pessoas *proximo;
	int info;

}pessoa;


typedef struct fila{
	pessoa *inicio;
	pessoa *fim;
	int tamanho;
	
}fila;



int inserir_elemento(fila *indicador, int dado){
	pessoa *novo_elemento;
	//UM ESPACO EH ALOCADO PARA A NOVA PESSOA
	novo_elemento = (pessoa*) malloc(sizeof(pessoa));

	//CASO SEJA A PRIMEIRA PESSOA A SER ADICIONADA EH PRECISO COLOCAR O PONTEIRO INICIO APONTANDO PARA ELA
	if (indicador->tamanho == 0){
		indicador->inicio = novo_elemento;
		indicador->fim = novo_elemento;
	}

	novo_elemento->proximo = NULL;
	novo_elemento->info = dado;
	indicador->fim->proximo = novo_elemento;
	indicador->fim = novo_elemento;
	indicador->tamanho++;

	return 0;
}



int main(){

	fila *line;
	pessoa *navegador, *navegador_aux;
	pessoa *cabeca;
	int numero_pessoas, elemento, n_removidos;


	//INICIALIZANDO MINHA FILA
	line = (fila*) malloc(sizeof(fila));
	line->inicio = NULL;
	line->fim = NULL;
	line->tamanho = 0;


	//INSERINDO ELEMENTOS NA FILA DE ACORDO COM O NUMERO DADO
	scanf("%d", &numero_pessoas);
	for(int i=0; i<numero_pessoas; i++){
		scanf("%d", &elemento);
		inserir_elemento(line, elemento);

	}

//COMECANDO PARTE DE REMOVER

	scanf("%d", &n_removidos);
	//removendo elemento da lista
	for(int i=0; i<n_removidos; i++){
		navegador = line->inicio;
		navegador_aux = NULL;
		scanf("%d", &elemento);
		while(navegador->info != elemento){
			navegador_aux = navegador;
			navegador = navegador->proximo;
		}
		//CASO O SEJA O PRIMEIRO ELEMENTO O QUE SERA REMOVIDO
		if (navegador_aux == NULL){
			line->inicio = navegador->proximo;
			line->tamanho--;
		}
		//CASO SEJA O ELEMENTO DO FIM QUE SERA REMOVIDO
		else if (navegador->proximo == NULL){
			navegador_aux->proximo = NULL;
			line->fim = navegador_aux;
			line->tamanho--;
		}
		//CASO SEJA O ELEMENTO DO MEIO DA LISTA A SER REMOVIDO
		else{
			navegador_aux->proximo = navegador->proximo;
			line->tamanho--;
		}
	}


	//PRINTANDO A FILA FINAL
	navegador = line->inicio;
	for(int i=0; i<line->tamanho; i++){
		printf("%d ", navegador->info);
		navegador = navegador->proximo;
	}

return 0;

}

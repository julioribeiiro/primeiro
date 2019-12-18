#include <stdio.h>
#include <stdlib.h>


struct node{
int num;
struct node *direita;
struct node *esquerda;
int altura;
int filhos_direita;
int filhos_esquerda;
};



int calcula_altura(struct node *no){
if(no == NULL){
return 0;
}
else{
return no->altura;
}
}

struct node* atualiza_altura(struct node *no){
int alt_direita;
int alt_esquerda;
if(no != NULL){
alt_direita = calcula_altura(no->direita);
alt_esquerda = calcula_altura(no->esquerda);
if(alt_direita>alt_esquerda){
no->altura=alt_direita+1;
}
else if(alt_esquerda>alt_direita){
no->altura=alt_esquerda+1;

}

}

return no;
}


struct node* simples_esquerda(struct node *no){
struct node *aux;
aux = malloc(sizeof(struct node));
aux = no->direita;
no->direita = aux->esquerda;
aux->esquerda = no;
no->esquerda = atualiza_altura(no->esquerda);
no = atualiza_altura(no);
no->filhos_direita = aux->filhos_esquerda;
aux->filhos_esquerda = no->filhos_esquerda + no->filhos_direita + 1;
return aux;
}



struct node* simples_direita(struct node *no){
struct node *aux;
aux = malloc(sizeof(struct node));
aux = no->esquerda;
no->esquerda = aux->direita;
aux->direita = no;
no->direita = atualiza_altura(no->direita);
no = atualiza_altura(no);
no->filhos_esquerda = aux->filhos_direita;
aux->filhos_direita = no->filhos_esquerda + no->filhos_direita + 1;
return aux;
}


//dupla pra DIREITA = simples pra esquerda (alinhar) + simples pra DIREITA (balancear)

struct node* dupla_direita(struct node *no){
struct node *no_resultado;
no_resultado = malloc(sizeof(struct node));
no->esquerda = simples_esquerda(no->esquerda);
no_resultado = simples_direita(no);
return no_resultado;
}


//dupla pra ESQUERDA = simples pra direita (alinhar) + simples pra ESQUERDA (balancear)

struct node* dupla_esquerda(struct node *no){
struct node *no_resultado;
no_resultado = malloc(sizeof(struct node));
no->direita = simples_direita(no->direita);
no_resultado = simples_esquerda(no);
return no_resultado;
}


//num / direita / esquerda / altura / filhos da direita / filhos da esquerda

struct node *inserir_AVL(struct node *no, int numero){
if(no == NULL){
struct node *no_novo;
no_novo = malloc(sizeof(struct node));
no_novo->num = numero;
no_novo->direita = NULL;
no_novo->esquerda = NULL;
no_novo->altura = 1;
no_novo->filhos_direita = 0;
no_novo->filhos_esquerda = 0;
return no_novo;
}


else if(numero<=no->num){
no->filhos_esquerda++;
no->esquerda = inserir_AVL(no->esquerda, numero);
if(calcula_altura(no->esquerda)-calcula_altura(no->direita) == 2){
if(numero<no->esquerda->num){
no = simples_direita(no);
}
else{
no = dupla_direita(no);
}

}

}


else{
no->filhos_direita++;
no->direita  = inserir_AVL(no->direita, numero);
if(calcula_altura(no->direita)-calcula_altura(no->esquerda) == 2){
if(numero>no->direita->num){
no = simples_esquerda(no);
}

else{
no = dupla_esquerda(no);
}
}

}

atualiza_altura(no);

return no;

}



void buscar_AVL(struct node *no, int num_busca){
struct node *aux;
aux = no;
int indice = 1;


while(aux != NULL){
	if(aux->num == num_busca){
		indice += aux->filhos_esquerda;
		break;
	}

	else if(num_busca<aux->num){
		aux = aux->esquerda;
	}

	else{
		indice += aux->filhos_esquerda + 1;
		aux = aux-> direita;
	}

}

	if(aux==NULL){
		printf("Data tidak ada\n");
	}

	else{
		printf("%d\n", indice);
	}


}


int main() {
int vezes;
int comando;
struct node *raiz;
int numero;
scanf("%d", &vezes);
for(int i=0; i<vezes; i++){
scanf("%d", &comando);
scanf("%d", &numero);
if(comando == 1){
raiz = inserir_AVL(raiz, numero);
}
else if(comando == 2){
buscar_AVL(raiz, numero);
}
}
return 0;
}
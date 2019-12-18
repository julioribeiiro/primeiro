/*
1) Pegar o primeiro numero que indica o n de casos teste (n)
2) Criar um for que ira repetir o processo n vezes
3) Receber do usuario um numero que representa o numero de entradas que virao
4) 




*/

#include <stdio.h>
#include <stdlib.h>

//criando estruturas para poder criar uma folha//

struct leaf{
	int num_leaf;
	struct leaf *left;
	struct leaf *right;
};

//função para criar uma nova folha//

struct leaf *create_leaf(int num){
	struct leaf *new_leaf;
	new_leaf = malloc(sizeof (struct leaf));
	new_leaf->num_leaf = num;
	new_leaf->left = NULL;
	new_leaf->right = NULL;

	return new_leaf;

}


//função que cria uma árvore//

struct leaf *create_tree(int num, struct leaf *position_leaf){
	if(position_leaf == NULL){
		position_leaf = create_leaf(num);
	}

	else if(num > position_leaf->num_leaf){
		position_leaf->right = create_tree(num, position_leaf->right);
	}

	else if(num <= position_leaf->num_leaf){
		position_leaf->left = create_tree(num, position_leaf->left);
	}

	return position_leaf;

}

void pre_ordem (struct leaf *root){
	if(root != NULL){
		printf(" %d", root->num_leaf);
		pre_ordem(root->left);
		pre_ordem(root->right);
	}
}

void in_ordem (struct leaf *root){
	if(root != NULL){
		in_ordem(root->left);
		printf(" %d", root->num_leaf);
		in_ordem(root->right);

	}
}

void pos_ordem (struct leaf *root){
	if(root != NULL){
		pos_ordem(root->left);
		pos_ordem(root->right);
		printf(" %d", root->num_leaf);

	}
}


int main () {
	int n;
	int m;
	int i;
	int j;
	int num_arvore;
	struct leaf *root;

	scanf("%d", &n);

	for(i=0; i<n; i++){
		root = NULL;
		scanf("%d", &m);
		for(j=0; j<m; j++){
			scanf("%d", &num_arvore);
			root = create_tree(num_arvore, root);
		}
		printf("Case %d:\n",i+1);
		printf("Pre.:");
		pre_ordem(root);
		printf("\nIn..:");
		in_ordem(root);
		printf("\nPost:");
		pos_ordem(root);
		printf("\n\n");

		free(root);

	}
}


